#global can only be accesible  inside a function but cannot be changed and can only be changed by accessing it using global keyword inside a function
#a=500

#local variable
# def show():
#     global a
#     a=100
#     b=50
#     print(a+b)
# show()
# print(a)

# def f1():
#     b=50
#     print(a+b)
# def f2():
#     nonlocal b
#     b=30
#     print (b)
# f1()
# f2()    

    

#create a function to find product of list
# def product(list):
#     product=1
#     for i in list:
#         product= product*i
#     return product
# print(product([10,20,30]))

# write a program to print the intial index of a character present in a string
# def initial(a,b):
#     for i in range(len(a)):
#         if a[i]==b:
#             return i
# print(initial('pratibha','a')) 

#packing and unpacking
# packing is the phenomenon of grouping elements together ~ two types tuple packing and dictionary packing
# def initial(v,*t):
#     for i in range(len(t)):
#         if t[i]==v:
#             print(t)
#             return i
# print(initial(100,20,30,100))  

#dictionary packing

# def initial(**d):
#     for i in range(len(d)):
        
#         print(d)
            
# print(initial(a=100,b=20,c=50))  

def unpack(a,b,c,d):
    return a,b,c,d
print(unpack(*'KFGH'))



