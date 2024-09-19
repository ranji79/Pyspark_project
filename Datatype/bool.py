d = True
print("vaue of d is",d)
print("type f d is",type(d))
print("ID of d is",id(d))

e = False
print("vaue of e is",e)
print("type f e is",type(e))
print("ID of e is",id(e))

print("Method available for a bool:",dir(d))


#True=1, False=0 (__add__=a.__add(b))#

print("__add__sum of d and e",d.__add__(e))

# int,bool,float
# int_false=True