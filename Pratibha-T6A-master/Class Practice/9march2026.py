#class and object

# in class attributes are same for every object
# class college:
#     c_name='jecrc'
#     loc = 'jaipur'
# s1=college() 
# print (college) 
# print(s1)  

# class college:
#     c_name='jecrc'
#     loc = 'jaipur'
# s1=college() 
# print (college) 
# print(s1) 
# s1.name='pratibha'
# s2= college()
# print(s1.name)

# class college:
#     c_name='jecrc'
#     loc = 'jaipur'
#     type='uni'
# s1=college() 
# s1.name='pratibha'
# s1.branch = 'btech'
# s1.age=21
# print(s1.name,s1.branch,s1.age)
# s2= college()
# s2.name='b'
# s2.branch='btech'
# s2.age=20
# print(s2.name,s2.branch,s2.age)
# s3=college()
# s3.name='c'
# s3.branch='bca'
# s3.age=22
# print(s3.name,s3.branch,s3.age)




#constuctor
# class college:
#     c_name='jecrc'
#     loc = 'jaipur'
#     def __init__(self,name,id,age):
#         self.name=name
#         self.id=id 
#         self.age=age
# s1=college('a','1',21) 
# print(s1.name,s1.id,s1.age)
# s2=college('b','2',21) 
# print(s2.name,s2.id,s2.age)
# s3=college('c','3',21) 
# print(s3.name,s3.id,s3.age)

# class college:
#     c_name='jecrc'
#     loc = 'jaipur'
#     def __init__(self,name,id,age):
#         self.name=name
#         self.id=id 
#         self.age=age
#     def show(self):
#         print(self.name)
#         print(self.id)
#         print(self.age)    
# s1=college('a','1',21)
# s1.show()


#types of method
#object method
# class college:
#     c_name='jecrc'
#     loc = 'jaipur'
#     def __init__(self,name,id,age):
#         self.name=name
#         self.id=id 
#         self.age=age
#     def show(self):
#         print(self.name)
#         print(self.id)
#         print(self.age) 
#         print(self.loc)   
# s1=college('a','1',21)
# s1.show()

#class method- accessible only using class @classname decorator is  used
# class college:
#     c_name='jecrc'
#     loc = 'jaipur'
#     def __init__(self,name,id,age):
#         self.name=name
#         self.id=id 
#         self.age=age
        
#     def show(self):
#         print(self.name)
#         print(self.id)
#         print(self.age)
        
#         print(self.loc)
#     @classmethod 
#     def display(cls):
#         print(cls.loc)       
# s1=college('a','1',21)

# s1.show()
# college.display()

#static method
# class Math:

#     @staticmethod
#     def add(a, b):
#         return a + b
# print(Math.add(5, 3))

#abstract method
class car:
    def __init__(self):
        self.acc=False 
        self.clutch=False
        self.brk=False
    def start(self):
        self.acc=True
        self.clutch=True
    c1.car()
    c1.start()        

