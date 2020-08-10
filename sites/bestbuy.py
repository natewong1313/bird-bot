try:
    from Crypto.PublicKey import RSA
    from Crypto.Cipher import PKCS1_OAEP
except:
    from Cryptodome.PublicKey import RSA
    from Cryptodome.Cipher import PKCS1_OAEP
from base64 import b64encode
from utils import send_webhook
import requests,time,lxml.html,json,sys,settings

class BestBuy:
    def __init__(self,task_id,status_signal,image_signal,product,profile,proxy,monitor_delay,error_delay):
        self.status_signal,self.image_signal,self.product,self.profile,self.monitor_delay,self.error_delay = status_signal,image_signal,product,profile,float(monitor_delay),float(error_delay)
        self.session = requests.Session()
        if proxy != False:
            self.session.proxies.update(proxy)
        self.status_signal.emit({"msg":"Starting","status":"normal"})
        tas_data = self.get_tas_data()
        product_image = self.monitor()
        self.atc()
        self.start_checkout()
        self.submit_shipping()
        self.submit_payment(tas_data)
        while True:
            success,jwt = self.submit_order()
            if not success and jwt != None:
                transaction_id = self.handle_3dsecure(jwt)
                self.submit_card(transaction_id)
            else:
                if success:
                    send_webhook("OP","Bestbuy",self.profile["profile_name"],task_id,product_image)
                else:
                    if settings.browser_on_failed:
                        self.status_signal.emit({"msg":"Browser Ready","status":"alt","url":"https://www.bestbuy.com/checkout/r/fulfillment","cookies":[{"name":cookie.name,"value":cookie.value,"domain":cookie.domain} for cookie in self.session.cookies]})
                        send_webhook("B","Bestbuy",self.profile["profile_name"],task_id,product_image)
                    else:
                        send_webhook("PF","Bestbuy",self.profile["profile_name"],task_id,product_image)
                break
    
    def get_tas_data(self):
        headers={
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
            "content-type": "application/json",
            "referer": "https://www.bestbuy.com/checkout/r/payment",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"
        }
        while True:
            try:
                self.status_signal.emit({"msg":"Getting TAS Data","status":"normal"})
                r = requests.get("https://www.bestbuy.com/api/csiservice/v2/key/tas",headers=headers)
                self.status_signal.emit({"msg":"Got TAS Data","status":"normal"})
                return json.loads(r.text)
            except Exception as e:
                self.status_signal.emit({"msg":"Error Getting TAS Data(line {} {} {})".format(sys.exc_info()[-1].tb_lineno, type(e).__name__, e),"status":"error"})
                time.sleep(self.error_delay)
    def monitor(self):
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
            "cache-control": "max-age=0",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.69 Safari/537.36"
        }
        image_found = False
        product_image = ""
        while True:
            self.status_signal.emit({"msg":"Loading Product Page","status":"normal"})
            try:
                r = self.session.get(self.product,headers=headers)
                if r.status_code == 200:
                    doc = lxml.html.fromstring(r.text)
                    if not image_found:
                        self.sku_id = doc.xpath('//span[@class="product-data-value body-copy"]/text()')[1].strip()
                        product_image = doc.xpath('//img[@class="primary-image"]/@src')[0]
                        self.image_signal.emit(product_image)
                        image_found = True
                    if self.check_stock():
                        return product_image
                    self.status_signal.emit({"msg":"Waiting For Restock","status":"normal"})
                    time.sleep(self.monitor_delay)
                else:
                    self.status_signal.emit({"msg":"Product Not Found","status":"normal"})
                    time.sleep(self.monitor_delay)
            except Exception as e:
                self.status_signal.emit({"msg":"Error Loading Product Page (line {} {} {})".format(sys.exc_info()[-1].tb_lineno, type(e).__name__, e),"status":"error"})
                time.sleep(self.error_delay)
    
    def check_stock(self):
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"
        }
        while True:
            self.status_signal.emit({"msg":"Checking Stock","status":"normal"})
            try:
                url = "https://www.bestbuy.com/api/tcfb/model.json?paths=%5B%5B%22shop%22%2C%22scds%22%2C%22v2%22%2C%22page%22%2C%22tenants%22%2C%22bbypres%22%2C%22pages%22%2C%22globalnavigationv5sv%22%2C%22header%22%5D%2C%5B%22shop%22%2C%22buttonstate%22%2C%22v5%22%2C%22item%22%2C%22skus%22%2C{}%2C%22conditions%22%2C%22NONE%22%2C%22destinationZipCode%22%2C%22%2520%22%2C%22storeId%22%2C%22%2520%22%2C%22context%22%2C%22cyp%22%2C%22addAll%22%2C%22false%22%5D%5D&method=get".format(self.sku_id)
                r = self.session.get(url,headers=headers)
                return "ADD_TO_CART" in r.text 
            except Exception as e:
                self.status_signal.emit({"msg":"Error Checking Stock (line {} {} {})".format(sys.exc_info()[-1].tb_lineno, type(e).__name__, e),"status":"error"})
                time.sleep(self.error_delay)
    
    def atc(self):
        headers={
            "accept": "application/json",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
            "content-length": "31",
            "content-type": "application/json; charset=UTF-8",
            "origin": "https://www.bestbuy.com",
            "referer": self.product,
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"
        }
        body = {"items":[{"skuId":self.sku_id}]}
        while True:
            self.status_signal.emit({"msg":"Adding To Cart","status":"normal"})
            try:
                r = self.session.post("https://www.bestbuy.com/cart/api/v1/addToCart",json=body,headers=headers)
                if r.status_code == 200 and json.loads(r.text)["cartCount"] == 1:
                    self.status_signal.emit({"msg":"Added To Cart","status":"carted"})
                    return
                else:
                    self.status_signal.emit({"msg":"Error Adding To Cart","status":"error"})
                    time.sleep(self.error_delay) 
            except Exception as e:
                self.status_signal.emit({"msg":"Error Adding To Cart (line {} {} {})".format(sys.exc_info()[-1].tb_lineno, type(e).__name__, e),"status":"error"})
                time.sleep(self.error_delay)

    def start_checkout(self):
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36",
        }
        while True:
            self.status_signal.emit({"msg":"Starting Checkout","status":"normal"})
            try:
                r = self.session.get("https://www.bestbuy.com/checkout/r/fufillment",headers=headers)
                if r.status_code == 200:
                    r = json.loads(r.text.split("var orderData = ")[1].split(";")[0])
                    self.order_id = r["id"]
                    self.item_id = r["items"][0]["id"]
                    self.status_signal.emit({"msg":"Started Checkout","status":"normal"})
                    return
                self.status_signal.emit({"msg":"Error Starting Checkout","status":"error"})
                time.sleep(self.error_delay)
            except Exception as e:
                self.status_signal.emit({"msg":"Error Starting Checkout (line {} {} {})".format(sys.exc_info()[-1].tb_lineno, type(e).__name__, e),"status":"error"})
                time.sleep(self.error_delay)

    def submit_shipping(self):
        headers={
            "accept": "application/com.bestbuy.order+json",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
            "content-type": "application/json",
            "origin": "https://www.bestbuy.com",
            "referer": "https://www.bestbuy.com/checkout/r/fulfillment",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36",
            "x-user-interface": "DotCom-Optimized"
        }
        profile = self.profile
        body = {"items":[{"id":self.item_id,"type":"DEFAULT","selectedFulfillment":{"shipping":{"address":{
            "country":"US",
            "saveToProfile":False,
            "street2":profile["shipping_a2"],
            "useAddressAsBilling":False,
            "middleInitial":"",
            "lastName":profile["shipping_lname"],
            "street":profile["shipping_a1"],
            "city":profile["shipping_city"],
            "override":False,
            "zipcode":profile["shipping_zipcode"],
            "state":profile["shipping_state"],
            "firstName":profile["shipping_fname"],
            "isWishListAddress":False,
            "dayPhoneNumber":profile["shipping_phone"],"type":"RESIDENTIAL"}}},"giftMessageSelected":False}],
            "phoneNumber":profile["shipping_phone"],
            "smsNotifyNumber":"",
            "smsOptIn":False,
            "emailAddress":profile["shipping_email"]}
        while True:
            self.status_signal.emit({"msg":"Submitting Shipping","status":"normal"})
            try:
                r = self.session.patch("https://www.bestbuy.com/checkout/orders/{}/".format(self.order_id),json=body,headers=headers)
                if json.loads(r.text)["id"] == self.order_id:
                    self.status_signal.emit({"msg":"Submitted Shipping","status":"normal"})
                    return
                self.status_signal.emit({"msg":"Error Submitting Shipping","status":"error"})
                time.sleep(self.error_delay)
            except Exception as e:
                self.status_signal.emit({"msg":"Error Submitting Shipping (line {} {} {})".format(sys.exc_info()[-1].tb_lineno, type(e).__name__, e),"status":"error"})
                time.sleep(self.error_delay)
    
    def submit_payment(self,tas_data):
        headers={
            "accept": "application/com.bestbuy.order+json",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
            "content-type": "application/json",
            "origin": "https://www.bestbuy.com",
            "referer": "https://www.bestbuy.com/checkout/r/fulfillment",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36",
            "x-user-interface": "DotCom-Optimized"
        }
        profile = self.profile
        card_number = profile["card_number"]
        key = RSA.importKey(tas_data["publicKey"])
        cipher = PKCS1_OAEP.new(key)
        encrypted_card = b64encode(cipher.encrypt(("00926999"+card_number).encode("utf-8"))).decode("utf-8")
        zero_string = ""
        for i in range(len(card_number)-10):
            zero_string+="0"
        self.bin_number = card_number[:6]
        encrypted_card +=":3:"+tas_data["keyId"]+":"+self.bin_number+zero_string+card_number[-4:]
        body = {"billingAddress":{
            "country":"US",
            "saveToProfile":False,
            "street2": profile["billing_a2"],
            "useAddressAsBilling": True,
            "middleInitial":"",
            "lastName": profile["billing_lname"],
            "street": profile["billing_a1"],
            "city":  profile["billing_city"],
            "override":False,
            "zipcode": profile["billing_zipcode"],
            "state": profile["billing_state"],
            "dayPhoneNumber": profile["billing_phone"],
            "firstName": profile["billing_fname"],
            "isWishListAddress":False},
            "creditCard":{
                "hasCID":False,
                "invalidCard":False,
                "isCustomerCard":False,
                "isNewCard":True,
                "isVisaCheckout":False,
                "govPurchaseCard":False,
                "isInternationalCard":False,
                "number": encrypted_card,
                "binNumber": self.bin_number,
                "cardType": profile["card_type"].upper(),
                "cid": profile["card_cvv"],
                "expiration":{"month": profile["card_month"],"year": profile["card_year"]},
                "isPWPRegistered":False}}
        while True:
            self.status_signal.emit({"msg":"Submitting Payment","status":"normal"})
            try:
                r = self.session.patch("https://www.bestbuy.com/checkout/orders/{}/paymentMethods".format(self.order_id),json=body,headers=headers)
                r = json.loads(r.text)
                if r["id"] == self.order_id:
                    self.status_signal.emit({"msg":"Submitted Payment","status":"normal"})
                    return
                self.status_signal.emit({"msg":"Error Submitting Payment","status":"error"})
                time.sleep(self.error_delay)
            except Exception as e:
                self.status_signal.emit({"msg":"Error Submitting Payment (line {} {} {})".format(sys.exc_info()[-1].tb_lineno, type(e).__name__, e),"status":"error"})
                time.sleep(self.error_delay)
    
    def submit_order(self):
        headers = {
            "accept": "application/com.bestbuy.order+json",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
            "content-type": "application/json",
            "origin": "https://www.bestbuy.com",
            "referer": "https://www.bestbuy.com/checkout/r/payment",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36",
            "x-user-interface": "DotCom-Optimized"
        }
        body = {"browserInfo":{"javaEnabled":False,"language":"en-US","userAgent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36","height":"1057","width":"1057","timeZone":"240","colorDepth":"24"}}
        while True:
            self.status_signal.emit({"msg":"Submitting Order","status":"alt"})
            try:
                r = self.session.post("https://www.bestbuy.com/checkout/orders/{}/".format(self.order_id),json=body,headers=headers)
                r = json.loads(r.text)
                try:
                    r = r["errors"][0]
                    if r["errorCode"] == "PAY_SECURE_REDIRECT":
                        self.status_signal.emit({"msg":"3DSecure Found, Starting Auth Process","status":"error"})
                        return False, r["paySecureResponse"]["stepUpJwt"]                        
                except:
                    if r["state"] == "SUBMITTED":
                        self.status_signal.emit({"msg":"Order Placed","status":"success"})
                        return True, None
                self.status_signal.emit({"msg":"Payment Failed","status":"error"})
                return False, None
                    
            except Exception as e:
                self.status_signal.emit({"msg":"Error Submitting Order (line {} {} {})".format(sys.exc_info()[-1].tb_lineno, type(e).__name__, e),"status":"error"})
                time.sleep(self.error_delay)
    
    def handle_3dsecure(self,jwt):
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
            "cache-control": "max-age=0",
            "content-type": "application/x-www-form-urlencoded",
            "origin": "https://www.bestbuy.com",
            "referer": "https://www.bestbuy.com/",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"
        }
        body = {
            "JWT": jwt,
            "TermUrl": "/payment/r/threeDSecure/redirect",
            "MD": ""
        }
        while True:
            self.status_signal.emit({"msg":"Authorizing Card (1)","status":"normal"})
            try:
                r = self.session.post("https://centinelapi.cardinalcommerce.com/V2/Cruise/StepUp",data=body,headers=headers)
                doc = lxml.html.fromstring(r.text)
                pa_req = doc.xpath('//input[@id="payload"]/@value')[0]
                md = doc.xpath('//input[@id="mcsId"]/@value')[0]
                term_url = doc.xpath('//input[@id="termUrl"]/@value')[0]
                acs_url = doc.xpath('//input[@id="acsUrl"]/@value')[0]
                break
            except Exception as e:
                self.status_signal.emit({"msg":"Error Authorizing Card (line {} {} {})".format(sys.exc_info()[-1].tb_lineno, type(e).__name__, e),"status":"error"})
                time.sleep(self.error_delay)
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Host": "1eaf.cardinalcommerce.com",
            "Origin": "https://centinelapi.cardinalcommerce.com",
            "Referer": "https://centinelapi.cardinalcommerce.com/",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"
        }
        body = {
            "PaReq": pa_req,
            "MD": md,
            "TermUrl": term_url
        }
        while True:
            self.status_signal.emit({"msg":"Authorizing Card (2)","status":"normal"})
            try:
                r = self.session.post(acs_url,data=body,headers=headers)
                doc = lxml.html.fromstring(r.text)
                pa_req = doc.xpath('//input[@name="PaReq"]/@value')[0]
                term_url = doc.xpath('//input[@name="TermUrl"]/@value')[0]
                md = doc.xpath('//input[@name="MD"]/@value')[0]
                url = doc.xpath("//form/@action")[0]
                break
            except Exception as e:
                self.status_signal.emit({"msg":"Error Authorizing Card (line {} {} {})".format(sys.exc_info()[-1].tb_lineno, type(e).__name__, e),"status":"error"})
                time.sleep(self.error_delay)
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Host": "secure4.arcot.com",
            "Origin": "https://1eaf.cardinalcommerce.com",
            "Referer": "https://1eaf.cardinalcommerce.com/",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"
        }
        body = {
            "PaReq": pa_req,
            "TermUrl": term_url,
            "MD": md
        }
        while True:
            self.status_signal.emit({"msg":"Authorizing Card (3)","status":"normal"})
            try:
                r = self.session.post(url,data=body,headers=headers)
                doc = lxml.html.fromstring(r.text)
                pa_res = doc.xpath('//input[@name="PaRes"]/@value')[0]
                pa_req = doc.xpath('//input[@name="PaReq"]/@value')[0]
                md = doc.xpath('//input[@name="MD"]/@value')[0]
                device_id = doc.xpath('//input[@name="DeviceID"]/@value')[0]
                locale = doc.xpath('//input[@name="locale"]/@value')[0]
                ABSlog = doc.xpath('//input[@name="ABSlog"]/@value')[0] 
                device_DNA =  doc.xpath('//input[@name="deviceDNA"]/@value')[0] 
                execution_time =  doc.xpath('//input[@name="executionTime"]/@value')[0] 
                dna_error =  doc.xpath('//input[@name="dnaError"]/@value')[0] 
                mesc =  doc.xpath('//input[@name="mesc"]/@value')[0] 
                mesc_iteration_count =  doc.xpath('//input[@name="mescIterationCount"]/@value')[0] 
                desc =  doc.xpath('//input[@name="desc"]/@value')[0] 
                is_DNA_done =  doc.xpath('//input[@name="isDNADone"]/@value')[0] 
                arcot_flash_cookie =  doc.xpath('//input[@name="arcotFlashCookie"]/@value')[0] 
                url = doc.xpath("//form/@action")[0]              
                break
            except Exception as e:
                self.status_signal.emit({"msg":"Error Authorizing Card (line {} {} {})".format(sys.exc_info()[-1].tb_lineno, type(e).__name__, e),"status":"error"})
                time.sleep(self.error_delay)

        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Host": "1eaf.cardinalcommerce.com",
            "Origin": "https://secure4.arcot.com",
            "Referer": "https://secure4.arcot.com/",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"
        }
        body = {
            "PaRes": pa_res,
            "PaReq": pa_req,
            "MD": md,
            "DeviceID": device_id,
            "locale": locale,
            "ABSlog": ABSlog,
            "deviceDNA": device_DNA,
            "executionTime": execution_time,
            "dnaError": dna_error,
            "mesc": mesc,
            "mescIterationCount": mesc_iteration_count,
            "desc": desc,
            "isDNADone": is_DNA_done
        }
        while True:
            self.status_signal.emit({"msg":"Authorizing Card (4)","status":"normal"})
            try:
                r = self.session.post(url,data=body,headers=headers)
                doc = lxml.html.fromstring(r.text)
                pa_res = doc.xpath('//input[@name="PaRes"]/@value')[0]
                md = doc.xpath('//input[@name="MD"]/@value')[0]
                url = doc.xpath("//form/@action")[0]  
                break
            except Exception as e:
                self.status_signal.emit({"msg":"Error Authorizing Card (line {} {} {})".format(sys.exc_info()[-1].tb_lineno, type(e).__name__, e),"status":"error"})
                time.sleep(self.error_delay)
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
            "cache-control": "max-age=0",
            "content-type": "application/x-www-form-urlencoded",
            "origin": "https://1eaf.cardinalcommerce.com",
            "referer": "https://1eaf.cardinalcommerce.com/",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"
        }
        body = {
            "PaRes": pa_res,
            "MD": md
        }
        while True:
            self.status_signal.emit({"msg":"Authorizing Card (5)","status":"normal"})
            try:
                r = self.session.post(url,data=body,headers=headers)
                jwt = r.text.split('parent.postMessage("')[1].split('"')[0]
                break
            except Exception as e:
                self.status_signal.emit({"msg":"Error Authorizing Card (line {} {} {})".format(sys.exc_info()[-1].tb_lineno, type(e).__name__, e),"status":"error"})
                time.sleep(self.error_delay)
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
            "cache-control": "max-age=0",
            "content-type": "application/x-www-form-urlencoded",
            "origin": "https://centinelapi.cardinalcommerce.com",
            "referer": "https://centinelapi.cardinalcommerce.com/V2/Cruise/StepUp",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"
        }
        body = {
            "McsId": md,
            "CardinalJWT": jwt,
            "Error": ""
        }
        while True:
            self.status_signal.emit({"msg":"Authorizing Card (6)","status":"normal"})
            try:
                r = self.session.post("https://centinelapi.cardinalcommerce.com/V1/Cruise/TermRedirection",data=body,headers=headers)
                doc = lxml.html.fromstring(r.text)
                transaction_id = doc.xpath('//input[@name="TransactionId"]/@value')[0]
                # url = doc.xpath("//form/@action")[0] 
                return transaction_id
            except Exception as e:
                self.status_signal.emit({"msg":"Error Authorizing Card (line {} {} {})".format(sys.exc_info()[-1].tb_lineno, type(e).__name__, e),"status":"error"})
                time.sleep(self.error_delay)

    def submit_card(self,transaction_id):
        headers = {
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
            "content-type": "application/json",
            "origin": "https://www.bestbuy.com",
            "referer": "https://www.bestbuy.com/checkout/r/payment",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36",
            "x-user-interface": "DotCom-Optimized",
            "x-native-checkout-version": "__VERSION__"
        }
        body = {"PaRes":"","orderId":self.order_id,"TransactionId":transaction_id}
        while True:
            self.status_signal.emit({"msg":"Submitting Card","status":"normal"})
            try:
                r = self.session.post("https://www.bestbuy.com/checkout/api/1.0/paysecure/submitCardAuthentication",json=body,headers=headers)
                if r.status_code == 200:
                    return
                else:
                    self.status_signal.emit({"msg":"Error Submitting Card","status":"error"})
                    time.sleep(self.error_delay)  
            except Exception as e:
                self.status_signal.emit({"msg":"Error Submitting Card (line {} {} {})".format(sys.exc_info()[-1].tb_lineno, type(e).__name__, e),"status":"error"})
                time.sleep(self.error_delay)



