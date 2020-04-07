from colorama import init, Fore, Back, Style
from datetime import datetime
import json, platform, darkdetect
if platform.system == "Windows":
    init(convert=True)
    normal_color = Fore.WHITE
else:
    init()
    normal_color = Fore.WHITE if darkdetect.isDark() else Fore.BLACK

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
