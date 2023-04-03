if __name__=="__main__":
    # dictObj = {
    #     "name" : "shamyl",
    #     "age" : 26,
    #     "location": {
    #         "area":"westridge",
    #         "city":"Rawalpindi",
    #         "country":"Pakistan"
    #     }
    # }
    # for key in dictObj:
    #     print(key, dictObj[key])
    #     print(type(key))
    #     if isinstance(key, dict):
    #         for x in key:
    #             print(x, key[x])
    #         # alternate way of doing it
    #         for key,value in key.items():
    #             print(key,value)
    lis = [{'ali': '651232', 'sha': '4354687', 'ikn': '3246756'}, {'hgfas': '7652354', 'okfd': '478734'}]
    # obj = {}
    # m = int(input("No of dictionaries you want to make"))
    # for x in range(m):
    #     n = int(input("Enter no of enteries you want to make"))
    #     for i in range(n):
    #         name = str(input("Enter name:"))
    #         obj[name] = str(input("Enter phoneNo:"))
    #     lis.append(obj)
    #     obj = {}
    # print(lis)
    for x in range(len(lis)):
        print(lis[x])
        for key,value in lis[x].items():
            print("key:", key)
            print("value:",value)
    # search = str(input("Enter name you want to search: "))
    # for key,value in obj.items():
    #     if search == key:
    #         print("Match found.")

