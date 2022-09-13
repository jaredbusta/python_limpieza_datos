from lib2to3.pgen2 import driver
from operator import index
import pandas as pd
import numpy as np
# Limpieza de datos excel

def readExcel():
    FILE_NAME="resumen agosto.xlsx"
    DESTINO="agosto"
    
    # excel = pd.ExcelFile("data_demo.xlsx")
    # excel = pd.ExcelFile("inventario.xlsx")
    
    dframe = pd.read_excel(FILE_NAME)
    print(dframe.columns)
    # dFrame_clear = dframe[4:9]
    # columns_name_to_search = ['Siniiga','Peso ',  'Peso Bascula','Sexo']
    # columns_name_to_search = 'Siniiga'
    # dFrame_clear = dframe[columns_name_to_search] 
    # print(dFrame_clear )
    
    # selecciona indice de columnas 
    #dframe = dframe.iloc[:,3:9] # todos los renglones de la columna 3 a la 9
    #dframe.drop('Fecha',axis=1, inplace=True) # borra la columna Fecha
    # print(cols)
    # borrar los rows que no se usan
    
    # dframe = cols.drop(range(94,113),axis=0)
    # dframe = dframe.drop(range(94,99),axis=0)
    # dframe = cols.drop(range(243,247),axis=0)
    # print(dframe.tail(30))
    
    # AGREGAR UNA COLUMNA CON EL NUMERO DE FILA
    # nueva columna
    # num_registros = dframe.shape[0]
    # col_data_nueva = np.arange(0,num_registros)
    
    # print(col_data_nueva)
    # dframe['contador']= col_data_nueva
    
    # print(dframe)
    
    # manejo de nulls
    
    # print(dframe.isnull()*1) #identificar con 1 las celdas con valores null o nan
    
    
    # dframe = dframe.fillna("Missing")#reemplaza valores null o nan con missing
    # dframe = dframe.fillna(dframe.mean())#reemplaza valores null o nan con media
    # dframe = dframe.fillna(dframe.median())#reemplaza valores null o nan con mediana
    dframe= dframe.dropna() # borra todos los rows con datos nulos
    
    # print(dframe[80:110])
    
    
    
    
    # filtrando datos 
    col_siniiga = dframe["Siniiga"] =="Siniiga"
    dframe= dframe.drop(dframe[col_siniiga].index, axis=0) # borra encabezados entre bloques
    
    # cambiando el tipo de dato de las columnas
    dframe['Siniiga'] = dframe["Siniiga"].astype('int64')
    
    dframe['Peso'] = dframe["Peso"].astype('float64')
    dframe['Peso Bascula'] = dframe["Peso Bascula"].astype('float64')
    dframe['Peso Origen'] = dframe["Peso Origen"].astype('float64')
    
    
    print(dframe.info()) # info general del data frame
    print(dframe.describe()) # estadisticas de las columnas numericas ( cont, media, desv.std, min, max, etc)
    print(dframe.memory_usage(deep=True)) # cuanta memoria se está usando en el dataframe y a nivel de columnas
    print(dframe['Sexo'].value_counts()) # cuenta las repeticiones de la columna 
    print(dframe.sort_values('Siniiga',ascending=True)) # ordena los valores de una columna
    
    print("=======================================")
    
    # groupBy
    # print(dframe.groupby("Sexo").mean())
    # funciones de agregacion
    res = dframe.groupby("Sexo").agg({'Peso':['min','max','count'],'Peso Bascula':['mean','sum']})
    
    # print(dframe.pivot_table(index='Siniiga', columns='Sexo', values='Peso Bascula', aggfunc=['sum','mean']))
    
    dframe.to_excel("./limpiados/"+DESTINO+"/"+  FILE_NAME);

if __name__ =="__main__": 
    readExcel()