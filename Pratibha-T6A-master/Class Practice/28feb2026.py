# for i in range(1,11,2):
#     print(i, end ='')

# a=input('enter name: ')
# result =''
# for i in a:
#     if(i==" "):
#         result+='_'
#     else:
#         result+=i    
        
# print(result)        

# age = int(input('age :'))
# income = int(input('income is :'))
# cs = int(input('credit score is :'))
# if(age>=21):
#     if(income>25000):
#         if(cs>=700):
#             print('approved')
#         else:
#             print('not approved')
#     else:
#         print('not approved')
# else:
#     print('not approved')                

# l = [(2+3j), 12, 'program', 'Python', False]
# dict = {}
# for i in l:
#     if type(i) == str:
#         vowels = ''
        
#         for j in i:
#             if j in 'AEIOUaeiou':
#                 vowels += j
#         dict[i] = vowels

# print(dict)

# l = ['p1.py','first.txt','13.py','tk.txt','tfk.com']

# dict = {}

# for i in l:
#     a = i.split('.')
    
#     if a[1] in dict:
#         dict[a[1]].append(a[0])
#     else:
#         dict[a[1]] = [a[0]]   

# print(dict)

# s= 'aaabbaabcc'
# result=''
# count=1
# for i in range(1,len(s)):
#     if(s[i]==s[i-1]):
#         count+=1
#     else:
#         result += s[i-1]+str(count)
#         count=1 
# result += s[-1]+str(count)           
# print(result)   

 