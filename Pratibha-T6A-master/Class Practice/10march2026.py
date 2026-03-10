# class bank:
#     name = 'SBI'

#     def __init__(self, name, accno, age, balance):
#         self.name = name
#         self.accno = accno
#         self.age = age
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print("Total:", self.balance)

#     def withdraw(self, amount):
#         self.balance -= amount
#         print("Remaining:", self.balance)

#     def show_balance(self):
#         print("Balance:", self.balance)


# user = bank("rahul", 567, 21, 2000)

# user.withdraw(300)
# user.deposit(400)
# user.show_balance()


#inheritance
# class employee:
#     def __init__(self,name,salary):
#         self.name=name 
#         self.salary=salary
# class manager(employee):
#     def __init__(self,name,salary,dep):
#         super().__init__(name,salary)
        
#         self.dep=dep  
# m= manager('pratibha',2000,'se')
# print(m.name)
# print(m.salary) 
# print(m.dep)     
# 

#property(no brackets requiredat the time of function calling)
# class student:
#     @property
#     def show(self,name):
#         self.name=name
#         print(name)
# s=student()
# s.show('Pratibha')  



#polymorphism
# class credit:
#  def pay(self,amount):
#   print ('amount paid by credit',amount)
# class upi:
#  def pay(self,amount):
#   print('amount paid by upi',amount) 
# class cash:
#  def pay(self,amount):
#   print('amount paid in cash',amount) 
# var=[credit(),upi(),cash()]  
# amount= int(input('enter amount:'))
# for i in var:
#  i.pay(amount) 
# 

# class circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         area= self.radius*self.radius*3.14
#         print('area is:',area)
#     def circumference(self):
#         circumference= 2*3.14*self.radius
#         print('circumference is: ',circumference)
# c= circle(int(input('enter radius: '))) 
# c.area()
# c.circumference()  


#file handling
# file = open('temp.txt','w')

# file.writelines('i am the first line \n'
#                 'second line \n'
#                 'third line \n')
# file.close()

# file = open('temp1.txt','w+')
# file.writelines('first line/n' 
#                 'second line/n')
# #to make sython interpreter to point at a specific index
# file.seek(0)


# print(file.readlines())
# file.close()
 
# file = open('jecrc.txt','a+')
# file.writelines(['jecrc is a university/n',
#                 'jecrc/n',
#                 'university'])

# file.close()

# import csv
# from datetime import date

# file = open('expense.csv','a+', newline='')

# w = csv.writer(file)
# r= csv.reader(file)

# w.writerow(['date','category','amount'])  # column names

# w.writerows([
#     [date.today(),'travel',400],
#     [date.today(),'travel',400],
#     [date.today(),'travel',400]
# ])

# file.close()


#dump
#loads
#json and pickle
# import json
# file=open('temp.txt','a+')
# data= {
#     'name:':'a',
#     'id:':56,
#     'pass:':123

# }
# print(type(data))
# enc_data= json.dumps(data)
# print(type(enc_data))
# file.write(enc_data)
# file.seek(0)
# print(file.read())

import pickle
file=open('temp.txt','ab+')
data= {
    'name:':'a',
    'id:':56,
    'pass:':123

}
print(type(data))
enc_data= pickle.dumps(data)
print(type(enc_data))
file.write(enc_data)
file.seek(0)
print(file.read())




