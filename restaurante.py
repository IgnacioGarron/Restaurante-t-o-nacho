##############################################################
## Si necesita agregar imports, debe agregarlos aquí arriba ##
from personas import Cliente, Cocinero, Repartidor
### INICIO PARTE 3 ###
class Restaurante:
    def __init__(self,n,p,c,r):
        self.nombre=str(n)
        self.platos=p
        self.cocineros=c
        self.repartidores=r
        self.calificacion=0
    
    def recibir_pedidos(self,clientes):
        for cliente in clientes:
            pedidos=[]
            for plato in cliente.platos_preferidos:
                info_plato=self.platos[plato]
                self.cocineros.sort(reverse=True, key=lambda x:x.habilidad)
                for cocinero in self.cocineros:
                    if cocinero.energia>0:
                        plato_cocinado=cocinero.cocinar(info_plato)
                        pedidos.append(plato_cocinado)
                        break
            self.repartidores.sort(reverse=True, key=lambda x:x.tiempo_entrega)
            for repartidor in self.repartidores:
                if repartidor.energia>0:
                    tiempo=repartidor.repartir(pedidos)
                    self.calificacion+=cliente.recibir_pedido(pedidos,tiempo)
                    break
                else:
                    self.calificacion+=cliente.recibir_pedido([],0)
        self.calificacion=round(self.calificacion/len(clientes),2)


### FIN PARTE 3 #

if __name__ == "__main__":

    ### Código para probar que tu clase haya sido creada correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    try:
        PLATOS_PRUEBA = {
        "Pepsi": ["Pepsi", "Bebestible"],
        "Mariscos": ["Mariscos", "Comestible"],
        }
        un_restaurante = Restaurante("Bon Appetit", PLATOS_PRUEBA, [], [])
        print(f"El restaurante {un_restaurante.nombre}, tiene los siguientes platos:")
        for plato in un_restaurante.platos.values():
            print(f" - {plato[1]}: {plato[0]}")
    except TypeError:
        print("Hay una cantidad incorrecta de argumentos en algún inicializador y/o todavía no defines una clase")
    except AttributeError:
        print("Algún atributo esta mal definido y/o todavia no defines una clase")
