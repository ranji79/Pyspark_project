"""
THis is for Testing File
Single line comment #
Multiple line comment ctrl + /
print() - empty line is created
end=/t - merging two print statement with tab space
end=/n - merging two print statement with new line
"""

a=10
b=20
c=a+b
#print("Value c:",c,"vaue b:",b,sep='-',end='\t')
print(f"value a is {a},value of b is {b},value of c is {c}",sep='|',end='\n')
print
print ("Input values",a,sep='|',end='\t')
print ("Output values",c)