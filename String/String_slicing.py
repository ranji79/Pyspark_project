# str='Ranjini ETL Automation'
#
# print("Value of str",str[0:7:3])
#
# gmail='ranjinip7@gmail.com'
#
# print("value of User",gmail[0:9])
# print("value of provider",gmail[10:15])
# print("value of domain",gmail[16:20])
# print("value of User",len(gmail))
# print("value of User",gmail.split('@'))

v1=(1,'ETLL',1.2,True) #()->consider as tuple#
print("Value of v1",type(v1))

v1=[1,'ETLL',1.2,True] #[]->consider as list#
print("Value of v1",type(v1))

##append###
v3=[]
print ("before Append",v3)
v3.append(3)
print ("After Append",v3)
v3.append ('ETL')
print ("After Append STR",v3)
v3.append (8)
print ("After Append STR",v3)
v3.append ([1,2,8])
print ("After Append STR",v3)

#**extend**#
v4=list()
v4.extend(['ET'])
print ("After extn print STR",v4)
v4.extend('24.6')
print("After 2 nd value",v4)
v4.insert(3,'Ranjini')
print("After Insertion",v4)
v4.insert(0,1)
print("After oth position",v4)
#**update**#
v4[3]='RAN'
print("After update",v4)#it is added 3 position data as RAN#

#pop remove clear***#
# print("Before pop",v4)
# v4.pop(3)
# print("After pop",v4)
# v4.remove('.')
# print("After remove",v4)
# v5=['RAN',1,3]
# print("Before clear",v5)
# v5.clear()
# print("After clear",v5)

#pop  removes specific position data,pop() - without mention postion default remove last position#
#remve -exact letter will remove#
#clear-It will remove entire list#
srt=[1,2,3,9,8,6,7]
print("Before sort",srt)
srt.sort()
print("After sorting",srt)
srt.reverse()
print("After reverse",srt)






