import json

jsonVar = '{"name":"shamyl","age":26,"sex":"male"}'
jsonVar2 = '{"Person":[{"name":"Shamyl","age":26,"gender":"male"},{"name":"ali","age":25,"gender":"neutral"}],"location": "Islamabad"}'
json_dict = json.loads(jsonVar)
# for val in json_dict:
#     print(val , ":" , json_dict[val])

json_dict2 = json.loads(jsonVar2)
   
for val in json_dict2:
    if isinstance(json_dict2[val],list):
        print("parent reculsive list condition")
        # recursive(json_dict2[val])
    
    if isinstance(json_dict2[val],dict):
        print("parent reculsive dict condition")
        
    
    if type(json_dict2[val]) == type(list):
        print("Nested object entered via list")
    if type(json_dict2[val]) == type(dict):
        print("Nested object entered via dict")
    print(val, ":" , json_dict2[val])




def recursive(list):
    for val in list:
        if isinstance(list[val],list):
            print("reculsive func condition.")
            recursive(list)
        else:
            print(val, ":", list[val]) 