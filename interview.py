# list=[3,5,2,8]
# list.reverse()
# print(list)

# #reverse    
    
    
# list1=["Roshni","khushi","vanshika"]
# list2=["sakshi","neha"]
# list1.extend(list2)
# print(list1)  

# # adding two list 


# a=[2,3,1,1,3,4,6,4]
# i=0
# b=[]
# while i<len(a):
#     if a[i] in b:
#         b.append(a[i])
#     i+=1
# print(a)


# a=[2,3,5,7,9,11]
# i=0
# while i<len(a):
#     if a[i]%2==0:
#         print("even",a[i])
#     else:
#         pass
#     i=i+1



# a=[2,3,5,7,9,11]
# num=int(input("enter"))
# i=0
# while i<len(num):
#     if num%2==0:
#         print(a[0])
    
#     i=i+1
#     break
# a=int(input("enter year"))
# if a%4==0:
#     print("leap")
# else:
#     print("not leap")

# N, M = map(int, input().split())
# for i in range(1, N, 2):
#     print(str('.|.' * i).center(M, '-'))
# print('WELCOME'.center(M, '-'))
# for i in range(N-2, -1, -2):
#     print(str('.|.' * i).center(M, '-'))


# num1=int(input("enter"))
# num2=int(input("enter"))
# num3=int(input("enter"))
# if num1<num2<num3:
#     print(num1)
#     print(num1)
# if num2>num1 and num2>num3:
#     print(num2)
# if num3>num1 and num3>num2:
#     print(num3)

# input_string = input('Enter elements of a list separated by space ')
# print("\n")
# user_list = input_string.split()
# # print list
# print('list: ', user_list)

# # convert each item to int type
# for i in range(len(user_list)):
#     # convert each item to int type
#     user_list[i] = int(user_list[i])

# # Calculating the sum of list elements
# print("Sum = ", sum(user_list))




# def Max(A, B, C): 
#    list = [A,B,C] 
#    return max(list) 
# A = int(input("Enter"))
# B = int(input("Enter"))
# C = int(input("Enter"))
# maximum=Max(A,B,C)
# def Min(A,B,C): 
#    list = [A,B,C] 
#    return min(list) 
# minimum=Min(A,B,C)
# res=maximum-minimum
# print(res)

# # integer palindrom
# num=int(input("enter"))
# x=num
# rev=0
# while num>0:
#     rev=(rev*10)+num%10
#     num=num//10
# if x==rev:
#     print("palindrom")
# else:
#     print("not palindrom")


# # string palindrom

# word=input("enter ")
# str=word.lower()
# pal=str[::-1]
# if pal==str:
#     print("palindrom")
# else:
#     print("not palindrom")


# # fibonacci series

# a=0
# b=1
# sum=0
# i=1
# while i<=10:
#     a=b
#     b=sum
#     sum=a+b
#     i=i+1
#     print(sum)


# reverse
# num=int(input("enter"))
# i=0
# while (num>0):
#     b=num%10
#     i=i*10+b
#     num=num//10
#     print(b,end="")



# # factor
# num=int(input("enter"))
# i = 1
# while i<=num:
#     if num%i==0:
#         print(i, end=" ")
#     i+=1


# # prime
# num=int(input("enter"))
# i=1
# a=0
# while i<=num:
#     if num%i==0:
#         a=a+1
#     i=i+1
# if a==2:
#     print(num,"prime")
# else:
#     print(num,"not prime")



# a={'a':2,'b':13,'c':5,'f':{'d':6,'e':9}}
# for i in a:
#     sum=0
#     for j in a[f]:
#         sum=sum+a[f][j]
#         print(sum)


# x={'a':56,'b':101,'c':52.5,'d':22,'e':2.5}
# list=[]
# for i in x:
#     if type(x[i])=="float" :
#         list.append(x[i])
# print(list)  

# a='Roshni'
# dic={}
# for i in a:
#     dict[i]=a
# print(dict)



# a="I am roshini jha"
# b=a.split()
# d={}
# for i in b:
#     j=0
#     c=0
#     while j<len(i):
#         c=c+1
#         j=j+1
#         d[i]=c
# print(d)

# def num(n):
#     if n>1:
#         num(n-1)
#         print(n)
#     else: 
#         print(n)
# num(5)  


# list1=[2,4,3,6]
# list2=[3,6,2,6]
# i=0
# a=[]
# while i<len(list1):
#     a.append(list1[i]+list2[i])
#     i+=1
# print(a)

# x= lambda a:a+10
# print(x(4))

def topten():
    yield 1
    yield 2
    yield 3
    yield 4
    
num=topten()

print(num.__next__())
# print(num.__next__())
# print(num.__next__())
# print(num.__next__())
 