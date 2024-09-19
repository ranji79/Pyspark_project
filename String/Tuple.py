"""The file is to create a pratcie of tuple
Created by Ranjini on 08/07/2024"""

tp=(1,'ETL',2.3,3+4j,True)
print ("Value of Tuple is",tp,type(tp),id(tp))

print ("Tuple slicing is",tp[2:4],type(tp[2:4]),id(tp[2:4]))

#whenever we are slicing the value [] is mandatory#
tp=[1,2,2,2,3,3,4,5]
print ("Count of Tuple is",tp.count(2),"index of tp",tp.index(3),id(tp))