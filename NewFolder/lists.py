# lists are 
mylist = ["banana", "apple", "orange"]  # created a list
mylist1 = [list()]  # created an empty list
mylist1 = ["apple", True, 52]
mylist1.append(True)
mylist.append("lemon") 
mylist.insert(1,"grape")
print(mylist+mylist1)
mylist1.remove(True)
mylist2 = sorted(mylist)
print(mylist1)
for element in mylist:
    if element in mylist1:
        print(element)
print(len(mylist)) 
print(mylist2)
mylist3 = [0, 1] * 10  
print(mylist3)   
a = mylist[1:5]  # a contains elements from index 1 to 4
b = mylist3[:1]  # b contain elements till index less than 1 
b1 = mylist3[8:]  # b1 contains elemnts from index 8
c = mylist3[::2]  # c contains every even elements 
d = mylist3[::-1]  # d contains elements in reverse order
print(a+b+c+d)
print(b1+b)
list = mylist  # changes made to list will be reflected in mylist as well 
list1 = mylist.copy()  # changes made  to list will not be reflected in my list
list3 = [1,2,3,4,5,6,7]
s = [i*i for i in list3]
print(list3)
print(s)
