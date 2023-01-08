"""
expresion = input("Expresion: ")
x,y,z = expresion.split(" ")
x_new = float(x)
z_new = float(z)
if y == "+":
    result = x_new + z_new
if y == "-":
    result = x_new - z_new
if y == "*":
    result = x_new * z_new
if y == "/":
    result = x_new / z_new
print(round(result, 1))
 """

expression = input("Expression: ")
x,y,z = expression.split(" ")

new_x = float(x)
new_z = float(z)
if  y == "+":
    result = new_x + new_z
elif y == "-":
    result = new_x - new_z
elif y == "*":
    result = new_x * new_z
elif y == "/" and new_z != 0:
    result = new_x / new_z
print(round(result, 1))





