#string,tuple,dictonary,list,set,unfrozen#

str='ranjni pandian'

print("Value of str",'pan' in str)
print("Value of str",'PAN' not in str)

lt=[2,3,4,5]
print("Value of 5",5 in lt)
print("Value of string 5",'5' in lt)
lt1=[5,6]
lt2=[5,6,[5,6]]
print("Value of lt",lt1 in lt2)

dt={1:'Ranjini',2:'Pandian',3:'P'}
print("Value of dt for key1",1 in dt)
print("Value of dt values for Ranjini",'Ranjini' in dt.values())
print("Value of Pandian",'Pandian' in dt.keys())
print("Value of Pandian",2 in dt.keys())


