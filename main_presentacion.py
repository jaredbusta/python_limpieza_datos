import matplotlib.pyplot  as plt
import pandas as pd
import numpy as np
import seaborn as sns

def readExcel():
    # excel = pd.ExcelFile("data_demo.xlsx")
    # excel = pd.ExcelFile("inventario.xlsx")
    
    dframe = pd.read_excel("data_demo_clean.xlsx")      
    # dframe= (dframe.sort_values('Siniiga',ascending=True)) # ordena los valores de una columna
    
    print(dframe.info())
    print("=========================================================================")
    
    # groupBy
    # print(dframe.groupby("Sexo").mean())
    # funciones de agregacion
    # res = dframe.groupby("Sexo").agg({'Peso ':['min','max','count'],'Peso Bascula':['mean','sum']})
    
    # print(dframe.pivot_table(index='Siniiga', columns='Sexo', values='Peso Bascula', aggfunc=['sum','mean']))
    # print(dframe)
    
    # ejemplo
    # x = np.linspace(0,5,11)
    # y = x**2
    # # subplot( fila, col, indice)
    # plt.subplot(2,1,1)
    # # primera fila muestra un plot y un histograma
    # plt.plot(x,y, 'rs-') # grafica de lineas
    # plt.hist(x ) # histograma
    # # subplot( fila, col, indice)
    # plt.subplot(2,1,2)
    # # segunda fila muestra un pie
    # plt.pie(x) # pie
    # plt.title("grafica de pie")
    # plt.xlabel("aver donde pone esto")
    # # plt.legend(loc="lower left")
    # # plt.legend()
    # plt.show()
    
    
    # personalizacion con POO
    # x = np.linspace(0,5,11)
    # y = x**2
    
    # fig = plt.figure()
    # un axes es una grafica
    # 0.1=> 
    # 0.1=>
    # 0.5=>
    # 0.9=>
    
    # axes = fig.add_axes([0.1,0.1,0.5,0.9])
    # axes.plot(x,y)
    # fig.show()
    
    # subplots
    # fig,axes = plt.subplots(nrows=1, ncols=2)
    # axes.plot(x,y)
    # fig.show()
    
    
    
    # bar chart categorical
    # country=['INDIA','JAPAN','MEXICO','COLOMBIA','GERMANY']
    # population = [1000,800,900,1000,300]
    # plt.bar(country, population, width=0.5,color=['red', 'blue','#cccccc'] )
    # plt.show()
    
    # sns.set(style='dark',palette='dark',font='Verdana', font_scale=1)
    # sns.barplot(x=['A','B','C'],y=[2,9,3])
    # plt.show()
    # sns.set();
    # tips = sns.load_dataset('tips') # dataset de prueba
    # # grafica de total_bils en x, propinas en y, agrupado por sex
    # sns.displot(tips, x="total_bill", y='tip',hue='sex')
    # plt.show()
    
    # sns.displot(dframe,x='Peso Bascula',kind='kde', legend=True)
    # plt.show()
    
    # graficos de distribucion
    print(dframe.head())
    # sns.histplot(data=dframe,x='Peso Bascula',cumulative=False,hue='Sexo',multiple='dodge')
    # plt.show()
    
    #Diagrama de densidad
    # sns.kdeplot(data=dframe,x='Peso Bascula', hue='Sexo',shade=True, bw_adjust=1)
    # plt.show()
    
    #Digrama escalonado
    # sns.ecdfplot(data=dframe,x='Peso Bascula', hue='Sexo')
    # plt.show()
    
    
    
    
    

if __name__ =="__main__": 
    readExcel()