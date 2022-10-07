# tuples are 
mytuple = ("max",18,"paris")
print(mytuple)
mytuple1 = ("name",)  # without comma at end if tuple contain only one element is considered a string
print(type(mytuple1))
tuple = tuple([1,2,3,4,5,6])
print(type(tuple))
mylist = list[mytuple]
print(mylist)
name, age, city = mytuple
print(name)
print(age)
print(city)
i1,*i2,i3 = tuple  # convert tuple into ist elemnet last elemnent and list of middle elements
print(i1)
print(i2)
print(i3)
 