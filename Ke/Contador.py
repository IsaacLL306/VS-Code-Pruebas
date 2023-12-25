# Primera prueba

#c = Contador de numeros
#n = Numero a solicitar

print("Prueba de contador")

c=0
n=int(input("Dime un numero de contador -  \n"))

while c<n:
    c+=1
    print(c, end=", ")

    if c == n:
        print("Finalizado")
        break


##Finalizado  