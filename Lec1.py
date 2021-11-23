import pandas as pd
import re
import numpy as np
import csv
import matplotlib.pyplot as plt

class Error(Exception):
    pass

class ErrorColumnas(Error):
    pass

class ErrorFaltaDatos(Error):
    pass

class ErrorDivision(Error):
    pass

def numCols():
    col = df.columns
    numCol = len(col)
    if(numCol == 12):
        print("El número de columnas es correcto.Son 12, es decir, una por cada mes")
    else:
        raise ErrorColumnas

def datosCols():
    meses = list(df.columns.values)
    for meses in df:
        if(df[meses].empty):
            print(f'{meses} no tiene datos')
            raise ErrorFaltaDatos
    print('Totas las columnas tienen datos')

def entero(valor):
    reg_exp = "[-+]?\d+$"
    return re.match(reg_exp, valor) is not None

'''def converDatos():
    for meses in df:
        if(df[f'{meses}'].dtype == 'object'):
            print(meses)
            for i in df[meses]:
                if(entero(i)== False):
                    print(i)
                    df[meses].replace([i], int(0))
            print(df.loc[:,[meses]])'''

def sumMes():
    suma = df.apply(np.sum)
    return (suma)

def mediaAnyo():
    col = df.columns
    numCol = len(col)
    total = sumM.sum()
    if(numCol > 0):
        media = total/numCol
        return media
    else:
        raise ErrorDivision

def gastosIngresos():
    totalGastos = 0
    totalIngresos = 0

    for num in sumM:
        if(num > 0):
            totalIngresos = totalIngresos + num
        else:
            totalGastos = totalGastos + num

    return totalGastos, totalIngresos

try:
    with open('M:\Master Python\ASIGNATURAS\Buenas practicas de programacion en Python\Leccion1\\finanzas2020.csv', newline='') as csvfile:
        read_csv = csv.reader(csvfile, delimiter='\t')
        dataset = []
        for row in read_csv:
            dataset.append(row)

        processed_data = []
        for i in range(1, len(dataset)):
            aux_dataset = []
            for j in dataset[i]:
                try:
                    aux = int(j)
                    aux_dataset.append(aux)
                except:
                    aux_dataset.append(0)
            processed_data.append(aux_dataset)
        df = pd.DataFrame(processed_data, columns=dataset[0])
        
except IOError:
    print("Error al leer el archivo csv")
else:
    print("Se ha leido y tratado correctamente el fichero")
    try:
        numCols()
        datosCols()
        sumM = sumMes()
        max_gasto = min(sumM)
        print(f'El mes que más ha gastado con {max_gasto} es', sumM.idxmax())
        min_gasto = max(sumM)
        print(f'El mes que más ha ahorrado con {min_gasto} es', sumM.idxmin())
        mediaTotal = mediaAnyo()
        print(f'La media de gastos al año es {mediaTotal}')
        totalG, totalI = gastosIngresos()
        print(f'El total de ingresos al año es de {totalI}')
        print(f'El total de gastos al año es de {totalG}')

        plt.plot(sumM,marker='o')
        plt.show()

    except ErrorColumnas:
        print("El número de columnas no es 12, por favor revise el fichero")
    except ErrorFaltaDatos:
        print("Hay un mes que no tiene datos")
    except ErrorDivision:
        print("No se puede dividir entre 0")
