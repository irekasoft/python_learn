employee_file = open("employees.txt", "r")

print(employee_file.readable())

print(employee_file.read())

print(employee_file.readline())

print(employee_file.readlines())

employee_file.close();


html_file = open("index.html", "w")

html_file.write("<p>this is html</p>")

html_file.close()