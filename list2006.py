# with slicing

k = [1,0,1,1,0,1,0,1,1,0,1,1,0]
k.sort()
print(k[len(k)-8:]+k[:len(k)-8])

#Output ======> [1,1,1,1,1,1,1,1,0,0,0,0,0]

#without slicing

k = [1,0,1,1,0,1,0,1,1,0,1,1,0]
zeros=[]
non_zeros=[]
for i in k:
     if i==0:
         zeros.append(i)
     else:
        non_zeros.append(i)
print(non_zeros+zeros)
 
#Output ======> [1,1,1,1,1,1,1,1,0,0,0,0,0]

#common elements

list1 = [1,2,3,4,5,6,7]
list2 = [2,3,4,67,11,12,8]
list3=[]
for i in list1:
     if i in list2:
         list3.append(i)
print(list3)

#Output ======> [2,3,4]

#remove duplicates

list = [1,2,3,4,5,6,3,4,10,1]
list2=[]
for i in list:
     if i not in list2:
         list2.append(i)
print(list2)

#Output ======> [1,2,3,4,5,10]

#maximum len

list = ["python","java","c++","Developer"]
le = ""
for i in list:
    if len(i)>len(le):
        le=i
print(le)

#Output ======> Developer

#Given a list and a target number, return all pairs that sum to the target.


list = [1,2,3,4,5,6,7,8,9,1,2,3,2,1]
t= 9
for i in range(len(list)-1):
    if list[i]+list[i+1]==t:
        print(list[i],list[i+1])

# Output ======> 4 5 
       
