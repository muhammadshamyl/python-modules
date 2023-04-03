import json

# if __name__=="__main__":
#     jsonObj = {
#         "name":'',
#         "age":None,
#         "city":''
#     }
#     jsonObj2 = {
#         "name":'Shamyl',
#         "age":26,
#         "city":'Islamabad',
#         "alpha":"alpha",
#         "omega":"omega",
#         "zona":"zona"
#     }
#     jsonObj3 = json.dumps(jsonObj2)
#     py_dict = jsonObj
#     py_dict2 = json.loads(jsonObj3)
#     print(py_dict)
#     for key in py_dict2.keys():
#         print(key)
#         for x in py_dict.keys():
#             if x == key:
#                 py_dict[x] = py_dict2[key]
    
#     print(py_dict)
    
class process_json:
    def __init__(self):
        self.json_obj = {
        "name":'',
        "age":None,
        "city":''
    }

    def updateJson(self,jsonObj):
        for x in jsonObj.keys():
            if x in self.json_obj.keys():
                print("Matched.")
                self.json_obj[x] = jsonObj[x]
    
    def print(self):
        print(self.json_obj)

if __name__=="__main__":
    jsonObj2 = {
        "name":'Shamyl',
        "age":26,
        "city":'Islamabad',
        "alpha":"alpha",
        "omega":"omega",
        "zona":"zona"
    }
    pj = process_json()
    pj.updateJson(jsonObj2)
    print(pj.json_obj)
    