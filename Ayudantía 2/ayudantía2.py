# ejercicio 1
archivo = open("datos_peliculas.csv","r")
lineas_arch = archivo.readlines()
archivo.close()

#ejercicio 2
arch1 = []
for i in lineas_arch:
    a = i.split(";")
    a[1] = a[1].replace(".","")
    arch1.append(";".join(a))
    

arch2 = []
for i in arch1:
    a = i.split(";")
    a[2]=a[2].replace(".","")
    a[2]=a[2].replace(",","")
    arch2.append(";".join(a))
    

arch3 = []
for i in arch2:
    a = i.split(";")
    a[3] = a[3].replace(",",".")
    arch3.append(";".join(a))
    


#ejercicio 3
final = open("arch_final.csv","w")
for i in arch3:
    final.write(i)
final.close()

