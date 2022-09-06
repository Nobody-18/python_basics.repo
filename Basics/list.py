friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends1 = ["Kevin", "Karen", "JIm", "Oscar", "Toby"]
print(friends[0])  # 1 element ffrom front
print(friends[-1])  # 1 element from back
print(friends[1:])  # every elemt from 2 nd
friends[1] = "Mike"
print(friends[1:4])  # elements frm 1 to 3
friends.extend(friends1)  # add friends1 to friends
friends.append("Creed")  # add creed to the end of the list
friends.insert(1, "Steve")  # insert steve at index 1 to the list
friends.remove("Jim")  # remove jim frm the list
friends.pop()  # pop out the last element from the list
friends.index("Kevin")  # give the index of Kevin
friends .count("Kevin")  # give the count of Kevins
friends.sort()  # sort list in alpha order
friends.reverse()  # reverse the order of the list
friends2 = friends.copy  # copy friends to friends2
print(friends)
