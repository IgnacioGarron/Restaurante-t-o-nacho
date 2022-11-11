##############################################################
from random import seed, randint, choice
from personas import Cliente, Cocinero, Repartidor
from restaurante import Restaurante
## Si necesita agregar imports, debe agregarlos aquí arriba ##

# IGNACIO GARRON VEDIA
# python 3.10.3

### INICIO PARTE 4 ###

def crear_cocineros():
    c1=Cocinero(choice(NOMBRES),randint(1,10))
    c2=Cocinero(choice(NOMBRES),randint(1,10))
    c3=Cocinero(choice(NOMBRES),randint(1,10))
    c4=Cocinero(choice(NOMBRES),randint(1,10))
    c5=Cocinero(choice(NOMBRES),randint(1,10))
    cocineros=[c1,c2,c3,c4,c5]
    for i in cocineros:
        print(i.nombre)
    return(cocineros)


def crear_repartidores():
    r1=Repartidor(choice(NOMBRES),randint(20,30))
    r2=Repartidor(choice(NOMBRES),randint(20,30))
    repartidores=[r1,r2]
    for i in repartidores:
        print(i.nombre)
    return(repartidores)


def crear_clientes():
    c1=Cliente(choice(NOMBRES),["Empanadas"])
    c2=Cliente(choice(NOMBRES),["Mariscos"])
    c3=Cliente(choice(NOMBRES),["Papas Duqueza"])
    c4=Cliente(choice(NOMBRES),["Jugo Natural"])
    c5=Cliente(choice(NOMBRES),["Lomo a lo Pobre"])
    clientes=[c1,c2,c3,c4,c5]
    return(clientes)

def crear_restaurante():
    c=crear_cocineros()
    r=crear_repartidores()
    crear_restaurante=Restaurante("Taquería Tío Nacho",INFO_PLATOS,c,r)
    return(crear_restaurante)
### FIN PARTE 4 ###

################################################################
## No debe modificar nada de abajo en este archivo.
## Este archivo debe ser ejecutado para probar el funcionamiento
## de su programa orientado a objetos.
################################################################

INFO_PLATOS = {
    "Pepsi": ["Pepsi", "Bebestible"],
    "Coca-Cola": ["Coca-Cola", "Bebestible"],
    "Jugo Natural": ["Jugo Natural", "Bebestible"],
    "Agua": ["Agua", "Bebestible"],
    "Papas Duqueza": ["Papas Duqueza", "Comestible"],
    "Lomo a lo Pobre": ["Lomo a lo Pobre", "Comestible"],
    "Empanadas": ["Empanadas", "Comestible"],
    "Mariscos": ["Mariscos", "Comestible"],
}

NOMBRES = ["Amaia", "Cristian", "Maggie", "Pablo", "Catalina", "Juan", "Sergio"]

if __name__ == "__main__":

    ### Código para probar que tu miniproyecto esté funcionando correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    seed("With Love")
    restaurante = crear_restaurante() # Crea el restaurante a partir de la función crear_restaurante()
    clientes = crear_clientes() # Crea los clientes a partir de la función crear_clientes()
    if restaurante != None and clientes != None:
        restaurante.recibir_pedidos(clientes) # Corre el método recibir_pedidos(clientes) para actualizar la calificación del restaurante
        print(
            f"La calificación final del restaurante {restaurante.nombre} "
            f"es {restaurante.calificacion}"
        )
    elif restaurante == None:
        print("la funcion crear_restaurante() no esta retornando la instancia del restaurante")
    elif clientes == None:
        print("la funcion crear_clientes() no esta retornando la instancia de los clientes")
