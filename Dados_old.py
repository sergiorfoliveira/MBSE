import pandas as pd
import json


class DadosBrutos:
    atributos_de_performance = pd.DataFrame
    atributos_de_custo = pd.DataFrame
    variaveis_de_projeto = pd.DataFrame
    dvm = pd.DataFrame
    variaveis_auxiliares = pd.DataFrame
    constantes = pd.DataFrame
    formulas = pd.DataFrame
    casos_de_teste = pd.DataFrame

    def __init__(self, Arquivo: str):
        self.atributos_de_performance = pd.read_excel(Arquivo, sheet_name="atributos_de_performance")
        self.atributos_de_custo = pd.read_excel(Arquivo, sheet_name="atributos_de_custo")
        self.variaveis_de_projeto = pd.read_excel(Arquivo, sheet_name="variaveis_de_projeto")
        self.dvm = pd.read_excel(Arquivo, sheet_name="dvm")
        self.variaveis_auxiliares = pd.read_excel(Arquivo, sheet_name="variaveis_auxiliares")
        self.constantes = pd.read_excel(Arquivo, sheet_name="constantes")
        self.formulas = pd.read_excel(Arquivo, sheet_name="formulas")
        self.casos_de_teste = pd.read_excel(Arquivo, sheet_name="casos_de_teste")
        pass


class Dados:
    Delta_V: float
    Capability: int
    Response_Time: int
    Total_Cost: float
    Payload: int
    Propulsion_Type: str
    Fuel_Level: int
    Isp: int
    Base_Mass: int
    Mass_Frac: float
    Capable: int
    Fast: int
    BMF = 1
    Costwet = 20
    Costdry = 150
    Gee = 9.8

    def __init__(self, dadosBrutos: DadosBrutos):
        self.Delta_V = 0
        self.Delta_V_Niveis = dadosBrutos.atributos_de_performance["niveis_atributo"][0]
        self.Capability = 0
        self.Response_Time = 0
        self.Total_Cost = 0.0
        self.Payload = 0
        self.Propulsion_Type: ""
        self.Fuel_Level = 0
        self.Isp = 0
        self.Base_Mass = 0
        self.Mass_Frac = 0.0
        self.Capable = 0
        self.Fast = 0
        self.BMF = dadosBrutos.constantes["valor_constante"][0]
        self.Costwet = dadosBrutos.constantes["valor_constante"][1]
        self.Costdry = dadosBrutos.constantes["valor_constante"][2]
        self.Gee = dadosBrutos.constantes["valor_constante"][3]

def main():
    dadosBrutos = DadosBrutos("C:\\Users\\F9910101\\Documents\\BSBr\\Dados.xlsx")
    pass


if __name__ == '__main__':
    main()
