import time
contraseña = "contraseña"

var_contra = input("Pon una contraseña: ")
incorrecta = 1

while var_contra != contraseña:
    print("Contraseña Incorrecta")
    var_contra = input("Prueba de Nuevo: ")
    incorrecta += 1
    if incorrecta % 3 == 0:
        print("El sistema esta bloqueado 30 segundos")
        for i in range(1,31):
            print(i)
            time.sleep(1)
print("Contraseña Correcta")