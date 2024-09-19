"""The file is to create a pratcie of set
Created by Ranjini on 08/07/2024"""

tp={1,'ETL',2,3+4j,True}
print ("Value of Tuple is",tp,type(tp),id(tp))

tp1={2,1,4}
tp3=tp1.intersection(tp)
print("Intersection",tp3)
tp4=tp.difference(tp1)
print("Difference",tp4)

#Set will be used to displaye only unique values,Ordering the data is not in ststic wi change anytime#
#Unfrozen set we can't able to edit or update#
# tp.count('False')
#
# print("Adding False value",tp)

# print ("Tuple slicing is",tp[2:4],type(tp[2:4]),id(tp[2:4]))
#
# #whenever we are slicing the value [] is mandatory#
# tp=[1,2,2,2,3,3,4,5]
# print ("Count of Tuple is",tp.count(2),"index of tp",tp.index(3),id(tp))