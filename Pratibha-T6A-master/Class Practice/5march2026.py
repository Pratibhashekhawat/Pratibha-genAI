# pattern printing

# for i in range(1,4):
#     for j in range(1,4):
#         if(i==j):
#             print('*',end='')
#         elif(i>j):
#             print('#',end='')    
    
#         else:
#             print('$',end='')
#     print()          


# #primary diagonal left to right
# for i in range(1,4):
#     for j in range(1,4):
#         if(i==j):
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print()        

# sec diagonal right+1
# n= int(input('row: '))
# m= int(input('column: '))
# for i in range(1,n+1):
#     for j in range(1,m+1):
#         if(i+j== n+1):
#             print('#',end='')
#         else:
#             print(' ', end='')
#     print()            

#for i in range(1,4):
#     for j in range(1,4):
#         if(i+j== 4):
#             print('#',end='')
#         elif (i==1 and j==1):
#             print('*',end='')
#         elif(i==3 and j==3):
#             print('@', end='')    
#         else:
#             print(' ',end='')    
#     print()   
# 

# row = int(input('enter row:'))
# column=  int(input('enter column: '))
# for i in range(1,row+1):
#     for j in range(1,column+1):
#         print('#' ,end ='')
#     print()    

# a=10
# for i in range(0,10):
#     a=2
# print(a)

# a=10
# def show():
#     global  a
#     a=5
#     print(id(a))
# show()
# print(a)
# print(id(a))

# a=20
# def f1():
#     global a
#     a=10
#     b=2000
#     def f2():
#         nonlocal b
#         b=2
#         print(b)
# print(a)
      
