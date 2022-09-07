# strings are ordered , immutable, text representation
str = "hello world"  # can also use single quote
print(str)
mystr = "    hello world     "
mystr = mystr.strip()
print(mystr)
print(mystr.startswith("hel"))
print(mystr.endswith("rld"))
print(mystr.find('o'))
print(mystr.count('o'))
print(mystr.replace("world", "universe"))
list = mystr.split(" ")
print(list)
ss = "apple, mango, grape"
mlist = ss.split(',')
print(mlist)
s = ' '.join(list)
print(s)
var = 3.2665
va = "Tim"
mystr = "the variable is %.2f" %var
print(mystr)
str = "the variable is {:.2f} and {}".format(var,va)
print(str)
st = f"the variables are {var} and {va}"
print(st)
