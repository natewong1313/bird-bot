from colorama import init, Fore, Back, Style
from datetime import datetime
import json, platform, darkdetect, random
if platform.system == "Windows":
    init(convert=True)
    normal_color = Fore.WHITE
else:
    init()
    normal_color = Fore.WHITE if darkdetect.isDark() else Fore.BLACK
print(normal_color + "Welcome To Bird Bot")

class BirdLogger:
    def ts(self):
        return str(datetime.now())[:-7]
    def normal(self,task_id,msg):
        print(normal_color + "[{}][TASK {}] {}".format(self.ts(),task_id,msg))
    def alt(self,task_id,msg):
        print(Fore.MAGENTA + "[{}][TASK {}] {}".format(self.ts(),task_id,msg))
    def error(self,task_id,msg):
        print(Fore.RED + "[{}][TASK {}] {}".format(self.ts(),task_id,msg))
    def success(self,task_id,msg):
        print(Fore.GREEN + "[{}][TASK {}] {}".format(self.ts(),task_id,msg))
    
def return_data(path):
    with open(path,"r") as file:
        data = json.load(file)
    file.close()
    return data
def write_data(path,data):
    with open(path, "w") as file:
        json.dump(data, file)
    file.close()
def get_profile(profile_name):
    profiles = return_data("./profiles.json")
    for p in profiles:
        if p["profile_name"] == profile_name:
            return p
    return None
def get_proxy(list_name):
    if list_name == "" or list_name == "None":
        return False
    proxies = return_data("./proxies.json") 
    for proxy_list in proxies:
        if proxy_list["list_name"] == list_name:
            return format_proxy(random.choice(proxy_list["proxies"].splitlines()))
    return None
def format_proxy(proxy):
    try:
        proxy_parts = proxy.split(":")
        ip, port, user, passw = proxy_parts[0], proxy_parts[1], proxy_parts[2], proxy_parts[3]
        return {
            "http": "http://{}:{}@{}:{}".format(user, passw, ip, port),
            "https": "https://{}:{}@{}:{}".format(user, passw, ip, port)
        }
    except IndexError:
        return {"http": "http://" + proxy, "https": "https://" + proxy}