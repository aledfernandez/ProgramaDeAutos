def calcular_precio (marca,puertas, color):
    marcas ={'ford':100000,'chevrolet':50000,'fiat':30000}
    colores = {'azul':5000,'rojo':4000,'verde':3000}
    puertas ={2:10000,3:20000,4:30000}
    precio = marcas[marca]+colores[color]+puertas[puerta]
    return precio

hay_clientes ='si'
marcas = ['ford','chevrolet','fiat']
puertas = [2,3,4]
colores = ['azul','rojo','verde']
ventas = []

while hay_clientes =='si':
    nombre=input("ingrese nombre del comprador: ")
    apellido=input("Ingrese apellido del comprador: ")
    marca = ''
    while marca not in marcas:
         marca=input("Ingrese marca: ")
    puerta = 0
    while puerta not in puertas:
        puerta = int(input("Ingrese cantidad de puertas: "))
    color = ''    
    while color not in colores:
        color = input("Ingrese color: ")
    precio = calcular_precio (marca,puerta,color)
    ventas.append({'Nombre':nombre,'Apellido':apellido,'Marca':marca,'Puertas':puerta,'Color':color,'precio':precio})   
    hay_clientes=input ("hay mas clientes?")

print(ventas)    

    

     
