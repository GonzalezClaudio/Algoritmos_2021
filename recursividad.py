# ejemplo factorial con solucion interactiva
#5!= 5*4*3*2*1=120

#def factorial_i(numero):
 #   factorial=1
  #  for i in range (2,6):
  #      factorial= factorial * i
        
  #  return factorial

# ejemplo factorial con solucion recursiva
#def factorial_R(numero):
 #   if (numero == 1 or numero == 0):
 #       return 1
 #   else:
 #    return numero * factorial_R(numero-1)       

#print(factorial_i(5))
#print (factorial_R(5))

# Ejemplo numeros fibonacci interactiva
def fibonacci_I(numero):
    fib_1=0
    fib_2=1
    for i in range(2,numero+1):
        fib_1,fib_2=fib_2,fib_1+fib_2
    return fib_2

# ejer 1: implementar una funcion que permita obtener el valor en la sucesion
#         de fibonacci para un numero dado.
# Ejemplo numeros fibonacci recursiva
# fib(n)=fib(n-1)+fib(n-2)

def fibonacci_R(numero):
    if (numero==0 or numero==1):
        return numero
    else:
        return fibonacci_R (numero-1) + fibonacci_R(numero-2)

#print (fibonacci_I(8))
#print (fibonacci_R(9))

# EJER 2: 
#IMPLEMENTAR UNA FUNCION QUE CALCULE LA SUMA DE TODOS LOS NUMEROS ENTEROS COMPRENDIDOS
# ENTRE 0 Y UN NUMERO ENTERO POSITIVO DADO.

def suma(numero):
    if (numero==0):
        return numero
    else:
        return numero + suma(numero-1)

#print (suma(8))

# EJER 3:
## IMPLEMENTAR UNA FUNCION PARA CALCULAR EL PRODUCTO DE DOS NUMEROS ENTEROS DADOS.

def producto(num1, num2):
    if (num2==0):
        return num2
    else:
        return num1 + producto(num1,num2-1)

#print (producto(8,8))

## EJER 4:
# IMPLEMENTAR UNA FUNCION PARA CALCULAR LA POTENCIA DADO DOS NUMEROS ENTEROS, EL PRIMERO
# REPRESENTA LA BASE Y EL SEGUNDO EL EXPONENTE.

def potencia(base,exponente):
    if (exponente==1):
        return base
    else:
        return base * potencia(base,exponente-1)

#print (potencia(3,5))