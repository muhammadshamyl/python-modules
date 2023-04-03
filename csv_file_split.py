from dataclasses import dataclass
from itertools import count
from operator import index
from re import X
import pandas as pd
import xlsxwriter

def csv():
    data = pd.read_excel(r'/home/mshamyl/python practise/python basic/ubl.xlsx')
    df = pd.DataFrame(data, columns=['Topic',
        'Question#',
        'Question_English',
        'Question_UR',
        'Question_RU',
        'Answer_English',
        'Answer_UR',
        'Answer_RU'
        ])
    counter = '1'
    file_string = '/home/mshamyl/faq'+counter+'.xlsx'
    print(file_string)
    workbook = xlsxwriter.Workbook(file_string)
    print(workbook)
    worksheet = workbook.add_worksheet(str("faq") + str(counter))
    i = 0
    col_list = ['Topic', 'Question#', 'Question_English', 'Question_UR', 'Question_RU', 'Answer_English', 'Answer_UR', 'Answer_RU']
    for c in col_list:
        worksheet.write(0, i, c)
        i += 1
    row = 1
    for ind in df.index:
        # print(df['Question#'][ind])
        x = df['Question#'][ind]
        x = str(x)
        y = x.split('.',3)
        y = str(y[0])
        # print(y)
        column = 0
        for d in df.iloc[ind]:
            try:
                worksheet.write(row, column, d)
                column += 1
            except:
                pass
        row += 1
        if str(counter) == y:
            a=1
            # print("yas")
        else:
            print(counter)
            workbook.close()
            counter = str(y)
            file_string = '/home/mshamyl/faq'+counter+'.xlsx'
            # print(file_string)
            workbook = xlsxwriter.Workbook(file_string)
            worksheet = workbook.add_worksheet(str("faq") + str(counter))
            print(workbook)
            i=0
            for c in col_list:
                worksheet.write(0, i, c)
                i += 1
            row=1
            # print("counter value changed")



# /home/mshamyl/python practise/python basic/
if __name__=="__main__":
    csv()