def takinginput():
    print("Write /done to terminate\n3")
    lines = []
    while True:
        line = input()
        if line == '/done':
            break
        lines.append(line)
    text = '\n'.join(lines)
    return text

def create_file(user_file, ext):
    file_name = user_file + "." + ext
    with open(file_name, 'w') as file:
        print(f"{file_name} has been created")
        wrt = takinginput()
        file.write(wrt)

def emptyfile(user_file, ext):
    file_name = user_file + "." + ext
    with open(file_name, 'w') as file:
        print(f"{file_name} empty has been created")

def readfile(user_file, ext):
    file_name = user_file + "." + ext
    with open(file_name, 'r') as file:
        print(file.read())

print("1= to open a file\n2= to create an empty file\n3= read a file")    
opt = int(input("Please Enter what you want to do: "))

user_file = input("Enter file name: ")
ext = input("Enter file extension [without '.']: " )
11
if opt == 1:
    create_file(user_file, ext)
elif opt == 2:
    emptyfile(user_file, ext)
elif opt == 3:
    readfile(user_file, ext)
else:
    print("Enter a valid option >.< ")
