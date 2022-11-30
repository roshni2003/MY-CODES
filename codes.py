# a=["p","u","j","a"]
# i=0
# b=[]
# while i<len(a):
#     c=[]
#     c.append(a[i])
#     b.append(c)
#     i=i+1
# print

# list=[1,2,3,1,2,2]
# i=0
# a=[]
# while i<len(list):
#     if list[i] in a:
#         a.append(list[i])
#     i=i+1
# print(a)

# n=int(input("enter"))
# i=0
# j=1
# while i<n:
#     i=i+1
#     print(i,end="")
# print()
#     j=j+i
#     print(j,end="")

# n=int(input("enter"))
# for i in range(1,11):
#     print(n,"*",i,"=",n*i)


# reverse
# num=int(input("enter"))
# i=0
# while(num>0):
#     b=num%10
#     i=i*10+b
#     num=num//10
#     print(b,end="")


# binary to decimal
# num=int(input("enter a number"))
# a=0
# sum=0
# while num!=0:
#     b=num%10
#     sum=sum+b*2**a
#     num=num//10 
#     a=a+1
#     print(sum)

# a=2
# b=3
# if a>b:
#     print("yes")
# else:
#     print("no")

# a=2
# b=3
# c=4
# if a>b:
#     print("nav")
# elif c<a:
#     print("gurukul")
# else:
#     print("navgurukul")

# L=int(input("enter"))
# R=int(input("enter"))
# i=1
# while i<=R:
#     if i%2!=0:
#         print(L,end=" ")
#     i+=1
    
    
# a=int(input("enter:"))
# b=int(input("enter:"))
# c=int(input("enter:"))
# if a==b!=c and a!=b==c:
#     print("2")
# elif a==b==c:
#     print("1")
# elif a!=b!=c:
#     print("3")
# else:
#     print("-1")



# N=int(input("enter"))
# sum=0
# for i in range(N+1):
#     sum=sum+i
#     i+=1
# print(sum)



# X=int(input())
# if X>=2000:
#     print("YES")
# else:
#     print("NO")



# n=int(input("Enter an integer:"))

# i=1
# while(i<=n):
#     k=0
#     if(n%i==0):
#         j=1
#         while(j<=i):
#             if(i%j==0):
#                 k=k+1
#             j=j+1
#         if(k==2):
#             print(i,"YES")
#         else:
#             print(i,"NO")
#     i=i+1



# a=int(input("enter"))
# if N%5==0 and N%11==0:
#     print("BOTH")
# elif N%5==0 or N%11==0:
#     print("ONE")
# elif N%5!=0 and N%11!=0:
#     print("NONE")


# a=int(input("enter"))
# b=int(input("enter"))
# for i in range (a,b+1):
#     if i%2!=0:
#         print(i,end=" ")


# A=int(input("enter"))
# B=int(input("enter"))
# C=int(input("enter"))
# if A>B and A>B:
#     if B>C:
#         print(B)
#     else:
#         print(C)
# if B>A and B>C:
#     if C>A:
#         print(C)
#     else:
#         print(A)
# if C>A and C>B:
#     if A>B:
#         print(A)
#     else:
#         print(B)

# n=int(input("enter"))
# i=0
# sum=0
# while i<=n:
#     sum=sum+i
#     i=i+1
# print(sum)


# N=int(input("enter"))
# print(N*(N+1)//2)



# n=int(input("enter"))
# i=0
# j=1
# while i<n:
#     i+=1
#     print(i,end=" ")
# print()
#     j+=1


# N=int(input("enter"))
# i=0
# while (N>i):
#     b=N%10
#     i=i*10+b
#     N=N//10
#     print(b,end="")

# N=int(input("enter"))
# M=[1,2,3,4]
# i=0
# while i<len(M):
#     if N in M:
#         print(1)
#     else:
#         print(-1) 
#     i+=1
#     break



# N=int(input("enter"))
# A=int(input("enter"))
# B=int(input("enter"))


# t=int(input())
# for i in range(t):
#     n,m,k,x=map(int,input().split())
#     if n%4==0:
#         print("YES")
#     else:
#         print("NO")

# a=2**5
# print(a)


# X=int(input("enter"))
# Y=int(input("enter"))
# sum=X+200
# for i in range (X,sum+1):
#     if i==Y:
#         print("YES")
#     else:
#         print("no")

# W=100
# X=11
# Y=1
# Z=10
# p=X-Y
# print(W+p*Z)


N=int(input("Enter"))
N1=int(input("enter"))
i=0
while i<=N:
    