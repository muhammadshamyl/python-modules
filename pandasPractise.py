import pandas as pd






if __name__=="__main__":
    # dataset = pd.read_csv('/home/mshamyl/Downloads/kaggle.csv')
    # dataset1 = dataset[dataset.vote_count >= 7078]
    # # print(dataset1)
    # dataset3 = dataset1[dataset1['vote_count'].isin([7078,17537,701,10957])]
    # # print(dataset3)
    # url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv"
    # datesetOnline = pd.read_csv(url, sep= '\t')
    # print(datesetOnline)
    # print(datesetOnline.shape)
    df = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv', sep='\t')
    print(df.head(10))
    print("df.info: ",df.info())
    print("df.describe: ",df.describe())
    print("df.columns: ", df.columns)
    df2 = df.groupby('item_name').sum()    
    print("sum: ", df2)
    # df2 = df2.sort_values(['quantity'],ascending=False)
    # print(df2.head(5))














# def lst_print(lst):
#     # to simply print pandas dataframe
#     df = pd.DataFrame(lst)
#     print(df)
#     print("-----------------------")
#     # to assign names to columns
#     df = pd.DataFrame(lst,columns=['word','number'])
#     print(df)
#     print("------------------------")
#     print(df['word']) 
#     length = len(df)
#     print(length)
#     x = 0
#     while x < length:
#         print(df.loc[x,'word'])
#         x+=1
# def csv_print():
#     df = pd.read_csv('/home/mshamyl/Downloads/sample.csv',delimiter=',', encoding='latin1',header=None)
#     df.columns = ["sr.no","Description","Name","count1","count2","count3","count4","Col1","Dpt","count5"]
#     # print(df[25:70])
#     print(df.columns)
#     print(df[['sr.no','Description']])
#     print(df.nlargest(3,'count2'))
#     print("-----------------------")
#     print(df['count5'].max())
#     # if you want to store this in a different dataset
#     df2 = df[df['count2'] == df['count2'].max()]
#     # if you want to get a specific col for the maximum value
#     df2 = df['Description'][df['count2']==df['count2'].max()]
#     #multiple cols for top three values
#     df3 = df.nlargest(3,'count2')[['sr.no','Description','Name']]
#     print(df3)



# if __name__=="__main__":
#     # lst = [['Geek', 25], ['is', 30], 
#     #    ['for', 26], ['Geeksforgeeks', 22]]
#     # lst_print(lst)
#     csv_print()
