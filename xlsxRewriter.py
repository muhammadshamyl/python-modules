import openpyxl, time
count = 0
print_counter = 0
list_headers1 = ['Conversation ID','Conversation Channel','Priority','Topic','Summary','Created At',]
list_headers2 = []
workbook = openpyxl.load_workbook('/home/mshamyl/Downloads/Ghazala Jabeen.xlsx')
sheet = workbook.active
for row in sheet.iter_rows():
    for cell in row:
        if cell.value in list_headers1:    
            for element in list_headers1:
                print(element)
                print_counter = print_counter + 1
            row = sheet.row[row = cell.row + 5]
            count = count + 1

print("Count: ", count)
print("Print Counter: ", print_counter)
        
        
        
        # next_column = sheet[cell.column_letter + str(cell.row)]
        # print(next_column.value)
        # time.sleep(1)
        

