import pytest

def numCols():
    col = ['enero', 'febrero','narzo']
    numCol = len(col)
    assert numCol == 3

def datosCols():
    df = [[1,2,3],[45,6,8],[1,5,9]]
    for i in df:
        assert df[i].empty == False

def mediaAnyo():
    numCol = 12
    total = 1200
    media = 100
    assert total/numCol == media

def gastosIngresos():
    totalGastos = 0
    totalIngresos = 0

    for num in range(-5,5):
        if(num > 0):
            totalIngresos = totalIngresos + num
        else:
            totalGastos = totalGastos + num

    assert totalGastos  == -15 , totalIngresos == 15
