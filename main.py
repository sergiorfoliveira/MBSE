import pandas

from Dados import *
from ahpGaussiano import *
import pandas as pd


def calcula(pl: int, pt: str, fl: int, df: pd.DataFrame, d: Dados):
    dici: dict

    # a sequencia abaixo precisa ser obedecida:
    dici = {"Payload": d.setPayload(pl),
            "Propulsion_Type": d.setPropulsion_Type(pt),
            "Fuel_Level": d.setFuel_Level(fl),
            "Base_Mass": d.setBase_Mass(),
            "Mass_Frac": d.setMass_Frac(),
            "Bus_Mass": d.setBus_Mass(),
            "Dry_Mass": d.setDry_Mass(),
            "Total_Mass": d.setTotal_Mass(),
            "Isp": d.setIsp(),
            "Delta_V": d.setDelta_V(),
            "Capability": d.setCapability(),
            "Response_Time": d.setResponse_Time(),
            "Total_Cost": d.setTotal_Cost(),
            "SAU_Delta_V": d.setSAU_Delta_V(),
            "SAU_Capability": d.setSAU_Capability(),
            "SAU_Response_Time": d.setSAU_Response_Time(),
            "MAU": d.setMAU()
            }
    novoRegistro = pd.DataFrame([dici])
    df = pd.concat([df, novoRegistro], ignore_index=True)
    return df


def produtoCartesiano(*args):
    # args deve ser uma tupla de listas. Se args tiver apenas 1 componente, este componente
    # deve ser uma lista de listas

    if (len(args) == 1) and (type(args[0]) == list):
        pools = [tuple(pool) for pool in args[0]]
    else:
        pools = [tuple(pool) for pool in args]
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    return result


def fullFactorial(db: Parametros):
    variaveis: list = []
    niveis: list = []

    for a in db.variaveis_de_projeto:
        variaveis.append(a)
        niveis.append(db.variaveis_de_projeto[a])
    return produtoCartesiano(niveis)


# def pareto(campos: list, df: pandas.DataFrame):
#     df1: pandas.DataFrame
#
#     df2 = pandas.DataFrame(columns=campos)
#     df1 = df.sort_values(by=campos)
#     for row1 in df1:
#
#     return df2


def main():
    df1: pandas.DataFrame
    df2: pandas.DataFrame
    df4: pandas.DataFrame
    ahp: pandas.DataFrame

    df1 = pd.DataFrame(columns=[])
    parametros = Parametros()
    dados = Dados(parametros)
    A = fullFactorial(parametros)
    for a in A:
        df1 = calcula(a[0], a[1], a[2], df1, dados)
    df1.to_csv('C:\\Users\\F9910101\\Downloads\\df1.csv')
    ahp = df1[["MAU", "Total_Cost"]].copy()
    df2 = ahpGaussiano(ahp, [True, False], [1, 1])
    df2.to_csv('C:\\Users\\F9910101\\Downloads\\df2.csv')
    # df4 = pareto(["Total_Cost", "MAU"], df1)
    pass


if __name__ == '__main__':
    main()
