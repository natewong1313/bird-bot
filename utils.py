import json

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