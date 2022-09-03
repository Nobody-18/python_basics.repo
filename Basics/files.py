employee_file = open("employees1.txt", "a+")

if employee_file.readable():
    print(employee_file.read())  # reads the whole file
    # print(employee_file.Breadline())#reads the first line
    # print(employee_file.Breadlines())#reads every line as an array
    # print(employee_file.Breadlines()[0])#reads the line with index0
else:
    print("Cannot open file")
employee_file.write("\nKaren -  HR manager")

employee_file.close()
