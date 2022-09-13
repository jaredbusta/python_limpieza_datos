import os
import numpy as np

def run():
    # data = pd.read_excel("inventario.xlsx")
    # data = pd.ExcelFile("inventario.xlsx")
    # print(data.sheet_names)
    arr= np.array([1,2,3,4,5])
    print(arr.dtype)
    
def dimenciones():
    scalar=np.array([1,2,3], ndmin=10) # setea las dimensioes
    print(scalar)
    print(scalar.ndim)
    # expander dimensiones
    exp = np.expand_dims(np.array([0,1,2]), axis=1 ) 
    print(exp)
    print(exp.ndim)
    # elimina las dimensiones que no se están usando
    exp_2 = np.squeeze(scalar)
    print(exp_2)
    print(exp_2.ndim)
    
def crearArrays():
    # lista en python nativo
    lista =list(range(0,10))
    print(lista)
    
    # lista con numpy
    # inicial, final, pasos
    lista = np.arange(0,20,2)
    print(lista)
    
    # crear arrays en rellenos de ceros
    # se usa para definir esquemas o esqueletos vacíos
    # que sirven como base
    lista = np.zeros(10) #lista o tupla de una dimension
    print(lista)
    lista= np.zeros((10,10)) # matriz de 10 x 10 
    print(lista)
    
    #  crea estructuras igual que zeros pero rellenos con numeros 1
    lista = np.ones(10) #lista o tupla de una dimension
    print(lista)
    lista= np.ones((10,10)) # matriz de 10 x 10 
    print(lista)
    
    lista= np.linspace(0,1,100)
    print(lista)
    
    # valores aleatorios
    lista = np.random.rand(4)
    # lista = np.random.rand(4,2) matriz
    # lista = np.random.rand(4,3,3) tensor 
    print(lista)
    
 
    
    

if __name__ == '__main__':
    # run()
    # dimenciones()
    # crearArrays()
    pass
