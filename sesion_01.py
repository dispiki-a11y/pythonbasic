#numeros

print(int(7))
print(float(7.7))
print(type(7))
print(type(7.7))
print(int(1+2))
print(int(10*2))
print(int(1 + 4 - 2))
print(float(1 + 2.0))

# operadores matematicos
# +
# -
# *
# /
# **
# % Modulo

print(int(2**3))
print(int(4**8))
print(float(10%3))
print(float(25%4))
print(float(16%2))
print(float(10 / 3))

#variables
print("====variables====")
x=100
y=1
print(x+y)

ventas = 1999991
print("nuestras ventas fueron:",ventas)
      
is_active=True
print(is_active)

game_over=False
print(game_over)

some_string="hola soy un string"
print(some_string)

print("====condiciones====")
edad=18
if (edad >=18):
    print("si puedes entrar al bar!!!")
else:
    print("no puedes entar al bar!!!!")

mi_numero = int(input("¿cual es el numero que deseas verificar?:"))
print(f"el numero que deseas verificar es{mi_numero}")
if mi_numero % 2 == 0:
    print(f"el numero {mi_numero} es par!")
else:
    print(f"el numero {mi_numero} es inpar!")

    def par_inpar(numero):
        if numero % 2 == 0:
            print(f"el numero {mi_numero} es par!")
        else:
            print(f"el numero {mi_numero} es inpar!")

print("====funcion par o inpar()=====")
mi_numero = int(input("¿cual numero desea verificar?:"))
print(f"el nuemero quedesea verificar es {mi_numero}")
print(par_inpar (mi_numero))