import pandas as pd
import pandasql as ps

# arr = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
#
# print(arr)
#
# print("Series",arr['e'])

# pdlist = [
#     ['Ranj','34','IT'],
#     ['KAYA','35','Manufacture']
#   ]
#
# frame = pd.DataFrame(pdlist,columns=['Name','ID','Dept'])
#
# print(frame)

df= pd.read_csv(r"C:\Users\Home\PycharmProjects\pythonProject\Files\Sample.csv")

# print(df.head(2))
# print(df.shape[0],df.shape[1])  #no of rows and columns in file#
# print(df.describe()) # it will describe about the Int columns only
# print(df.columns) # display only the column names
# print(df.dtypes)
# print(df['ID'])
# print(ps.sqldf("Select * from df where id>2"))

df1 = pd.read_excel(r"C:\Users\Home\PycharmProjects\pythonProject\Files\Master_Test_Template.xlsx")

print(df1.head(3))

# print(df.iloc[0:2 , 1:2])
# print(df.loc[0:2, 'ID':'Subject'])
# print(df[(df.ID > 2) & (df.Subject == 'Maths')])



