# def calc (*args):
#     sum =0
#     for i in args:
#         sum =sum+i
#     ##print(f"Sum {args} is :", sum)
#     return sum
#
# print("Sum",calc (1,2,3,4,5))

def calc(**kwargs):
    print(kwargs)
    print_message=''
    for i in kwargs.values():
        print_message = print_message + " " + i
    print(print_message)


calc(name= "Ranjini",message="Good")
