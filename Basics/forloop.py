# friends = [ "jim","mike","kevin"]
# for friend in range(3):
#     print(friends[friend])
# def power(base,power):
#     result=1
#     for index in range(power):
#         result = result*base
#     return result
# print(power(2,4))
number_grid = [
    [1, 2, 3, ],
    [4, 4, 5],
    [6, 7, 8]
]

print(number_grid[1][2])
for row in number_grid:
    for column in row:
        print(column)
    print("")
