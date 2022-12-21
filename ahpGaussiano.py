import numpy as np
import pandas as pd


def ahpGaussiano(atributos: pd.DataFrame, crescimento: list, pesos: list):
    # "crescimento" deve ter o mesno número de elementos que as colunas de "atributos"
    # "crescimento" True : quanto maior o atributo, melhor
    # "crescimento" False : quanto maior o atributo, pior
    # df: pandas.DataFrame
    colunas: list = []
    totais: list = []
    media: float = 0
    desvpad: float = 0
    cv: list = []

    index = 0
    for k in atributos.keys():
        atributos[k] = atributos[k]*pesos[index]
        index += 1
    for k in atributos.keys():
        colunas.append(k)
        totais.append(atributos[k].sum())
    df = pd.DataFrame(columns=colunas)
    index = 0
    for k in df.keys():
        if crescimento[index]:
            df[k] = atributos[k]/(totais[index] + np.finfo(float).eps)
        else:
            df[k] = 1/(atributos[k] + np.finfo(float).eps)
            df[k] = df[k] / df[k].sum()
        index += 1
        media = df[k].mean()
        desvpad = df[k].std()
        cv.append(desvpad/media)
    index = 0
    soma = sum(cv)
    for k in cv:
        cv[index] = k/soma
        index += 1
    result = df.dot(cv)
    return result
