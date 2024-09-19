"""The file is to create a pratcie of set
Created by Ranjini on 08/07/2024"""

dic={}
dic1={1:'Ranjini',2:'Gopi'}
print("Dictnary value",dic,type(dic),id(dic))

 ##Adding and updating the vaue ##
dic1 [3] = 'Saran'
print("Adding 3 key value",dic1)
dic1[4]='kayal'
print("Adding 4 key value",dic1)

dic1[3]='SriSaran'
print("After update the 3rd value",)

##update Will update the exsisting key and value and add the new key and value##
dic1.update({5:'Family',6:'Members',3:'Saran'})
print("Adding values",dic1)

print("Adding 3 key value",dic1.items(),type(dic1.items()))
print("Adding 3 key value",dic1.keys(),type(dic1.keys()))
print("Adding 3 key value",dic1.values()),type(dic1.values())





