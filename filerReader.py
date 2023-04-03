import pandas as pd
# from openpyxl import load_workbook


# counter = 0
# data = pd.read_excel(r'/home/mshamyl/Downloads/Ghazala Jabeen.xlsx')
# header = (pd.read_excel(r'/home/mshamyl/Downloads/Ghazala Jabeen.xlsx').columns)
# conversation_id = data[(data['Conversation ID'] == 'Conversation ID')]
# print(conversation_id)
# print(len(conversation_id))
# conversation_id.to_excel('/home/mshamyl/Downloads/Conversation ID.xlsx')
df = pd.read_json('/home/mshamyl/Downloads/food_data.json')
print(df.head(100))
# # print(data.head(100))
# # print(data)
# print("----------------------------------------------------------------------------")
# # print(data.loc[data['Conversation ID'] == "Type"])
# # if c:
# #     counter = counter + 1
# for index,row in data.iterrows():
#     if row['Conversation ID'] == 'Type':
#         counter = counter+1
    
# print("Total conversations: ", counter)

# # conversation_id = data.loc[data['Conversation ID'] == "Conversation ID"]
# # print(conversation_id)
# for index,row in data.iterrows():
#     print(index,row)
# book = load_workbook('/home/mshamyl/Downloads/Ghazala Jabeen.xlsx')
# sheet = book.active
# rows = sheet.rows
# # print(rows)
# headers = [cell.value for cell in next(rows)]
# # print(headers)
# data = []
# for row in rows:
#     for cell in row:
#         # print(cell.value)
#         data.append(cell.value)
        
#     # print("-------------------------------------------------------------------")

# # print(data[0])
# # print("-----------------------------------------------------------------------")
# for row in range(len(data)):
#     # print(data[row])
#     # print("--------------------------------------------------------------------------")
#     if data[row] == "Conversation ID":
#         counter = counter + 1
#         print(data[row],":")
#         print(data[row + 1])
# # for col in data:
# #     if col[1] == 'Conversation ID':
# #         counter = counter  + 1

# # print("Conversations: ", counter)