print("Bienvenido al generador de arbolitos navideños :D")
size = int(input("Introduce el tamaño de tu arbolito: "))
row = "*"
space= " "*(int((size+size-1)/2))
last_row = " "

for i in range(size, 1, -1):
    if row == "*":
        last_row += space+row
        print(space, row)
        row +="**"
        space = space.replace(" ","",1)
        continue
    else:
        print(space,row)
        row +="**"
        space = space.replace(" ","",1)

print(last_row)