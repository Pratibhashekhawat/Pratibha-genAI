#arguments- 4types
# positional arguments - passing all the argument is manadatory
# def form(name ,age,phn,mail):
#     print('name : ',name)
#     print('age : ',age)
#     print('phn : ',phn)
#     print('mail : ',mail)
# form('pratibha','21','9928077712','pratibha@gmail.com') 
#

#default argument- should pe passed at the end only
# def form(name ,phn,mail,age=21):
#     print('name : ',name)
#     #print('age : ',age)
#     print('phn : ',phn)
#     print('mail : ',mail)
# form('pratibha','9928077712','pratibha@gmail.com')    

#keyword argument
# def form(name ,age,phn,mail,alt_ph):
#     print('name : ',name)
#     print('age : ',age)
#     print('phn : ',phn)
#     print('mail : ',mail)
#     print('alt_ph : ',alt_ph)
# form('pratibha','21','9928077712','pratibha@gmail.com',alt_ph=9928012185) 

#variable length args - same as packing
# def form(*a):
#     print('a:',a)
    # print('name : ',name)
    # print('age : ',age)
    # print('phn : ',phn)
    # print('mail : ',mail)
# form('pratibha','21','9928077712','pratibha@gmail.com') 

# def form(name ,phn,mail,alt_ph, age=21):
#     print('name : ',name)
  
#     print('phn : ',phn)
#     print('mail : ',mail)
#     print('alt_pn: ',alt_ph)
#     print('age : ',age)
    
# form(input('enter name:'),input('enter phone no:'),input('enter mail:'),alt_ph=9928012145) 

#recursion
#factorial using loop
# factorial=1
# n= int(input('enter no:'))
# for i in range(1,n+1):
#     factorial = factorial *i
# print(factorial) 

#factorial using recursion

# import sys
# sys.setrecursionlimit(2000)
# def fact(n):
#     if n==1 or n==0:
#         return 1
#     return n*fact(n-1)
# print(fact(int(input('enter no:'))))

#write a program to create a function which adds minimum two numberse and maximun 5 numbers

# def sum(a,b , c=0,d=0,e=0):
#     return(a+b+c+d)
# print(sum(2,3))


#wap to fing sum of individual digits 
# def sum(num):
#     sum=0
#     for i in str(num):
#         sum+= int(i)
#     return sum
# print(sum(521))