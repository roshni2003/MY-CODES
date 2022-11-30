# rangea='15-30'
# list=[]
# a=rangea.split("-")
# for i in range(int(a[0]),int(a[1])+1):
#     list.append(i)
# print(a)

# a="shahnaz"
# c=0
# for i in a:
#     if i=="h":
#         c=c+1
# print(c)


# list=[2, 6, 18, 10, 3, 75] 
# list1=[6, 19, 24, 12, 3, 87] 
# i=0
# while i<len(list):
#     j=0
#     while j<len(list1):
#         if list[i]%2==0 and list1[j]%2==0:
#             print("dono even hai")
#         else:
#             print("dono even nhi hai")
#         j=j+1
#     i=i+1


# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# for i in d2:
#     if i in d1:
#         d1[i]=d1[i]+d2[i]
#     else:
#         d1[i]=d2[i]
# print(d1)

N = int(input("Enter:"))
if N%5==0 and N%11==0:
    print("BOTH")
elif N%5==0 or N%11==0:
    print("ONE")
elif N%5!=0 and N%11!=0:
    print("NONE")