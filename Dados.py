import math


class Parametros:
    atributos: dict
    variaveis_de_projeto: dict
    variaveis_auxiliares: dict
    constantes: dict
    casos_de_teste: dict

    def __init__(self):
        # Todas os campos chamados "niveis" devem ser monotomicamente crescentes
        # Todos os campos chamados "SAU" devem ter o mesmo tamanho dos repectivos "niveis".
        # Os pesos dos atributos que não são "de_custo" devem somar 1
        # Os pesos dos atributos que são "de_custo" devem somar 1
        self.atributos = {
            "Delta_V": {
                "de_custo": False,
                "peso": 0.6,
                "niveis": [0.0, 4.3, 8.3, 12.0],
                "SAU": [0.0, 0.7, 0.9, 1.0]
            },
            "Capability": {
                "de_custo": False,
                "peso": 0.3,
                "niveis": [0, 1, 2, 3, 4],
                "SAU": [0.0, 0.3, 0.6, 0.9, 1.0]
            },
            "Response_Time": {
                "de_custo": False,
                "peso": 0.1,
                "niveis": [0, 1],
                "SAU": [1, 0]
            },
            "Total_Cost": {
                "de_custo": True,
                "peso": 1,
                "niveis": [0, 4500],
                "SAU": [1, 0]
            }
        }
        self.variaveis_de_projeto = {
            "Payload": [300, 1000, 3000, 5000],
            "Propulsion_Type": ["Biprop", "Cryo", "Electric", "Nuclear"],
            "Fuel_Level": [100, 300, 1000, 3000, 10000, 30000]
        }
        self.variaveis_auxiliares = {
            "Isp": {"Biprop": 300, "Cryo": 450, "Electric": 2200, "Nuclear": 1500},
            "Base_Mass": {"Biprop": 0, "Cryo": 0, "Electric": 25, "Nuclear": 1000},
            "Mass_Frac": {"Biprop": 0.12, "Cryo": 0.13, "Electric": 0.3, "Nuclear": 0.2},
            "Capable": {0: 0, 300: 1, 1000: 2, 3000: 3, 5000: 4},  # índices vêm do Payload
            "Fast": {"Biprop": 0, "Cryo": 0, "Electric": 1, "Nuclear": 0}
        }
        self.constantes = {
            "BMF": 1,
            "Costwet": 20,
            "Costdry": 150,
            "Gee": 9.8
        }
        self.casos_de_teste = {  # usar os casos abaixo para testar as fórmulas e código
            "caso 1": {
                "Payload": 300,
                "Propulsion_Type": "Biprop",
                "Fuel_Level": 100,
                "Resultados": {
                    "Bus_Mass": 312,
                    "Dry_Mass": 612,
                    "Total_Mass": 712,
                    "Isp": 300,
                    "Delta V": 0.4,
                    "Capability": 1,
                    "Response_Time": 0,
                    "Total_Cost": 106
                }
            },
            "caso 2": {
                "Payload": 1000,
                "Propulsion_Type": "Cryo",
                "Fuel_Level": 300,
                "Resultados": {
                    "Bus_Mass": 1039,
                    "Dry_Mass": 2039,
                    "Total_Mass": 2339,
                    "Isp": 450,
                    "Delta V": 0.605,
                    "Capability": 2,
                    "Response_Time": 0,
                    "Total_Cost": 353
                }
            },
            "caso 3": {
                "Payload": 1000,
                "Propulsion_Type": "Electric",
                "Fuel_Level": 1000,
                "Resultados": {
                    "Bus_Mass": 1325,
                    "Dry_Mass": 2325,
                    "Total_Mass": 3325,
                    "Isp": 2200,
                    "Delta V": 7.713,
                    "Capability": 2,
                    "Response_Time": 1,
                    "Total_Cost": 415.25
                }
            },
            "caso 4": {
                "Payload": 3000,
                "Propulsion_Type": "Electric",
                "Fuel_Level": 1000,
                "Resultados": {
                    "Bus_Mass": 3325,
                    "Dry_Mass": 6325,
                    "Total_Mass": 7325,
                    "Isp": 2200,
                    "Delta V": 3.165,
                    "Capability": 3,
                    "Response_Time": 1,
                    "Total_Cost": 1095.25
                }
            },
            "caso 5": {
                "Payload": 300,
                "Propulsion_Type": "Nuclear",
                "Fuel_Level": 1000,
                "Resultados": {
                    "Bus_Mass": 1500,
                    "Dry_Mass": 1800,
                    "Total_Mass": 2800,
                    "Isp": 1500,
                    "Delta V": 6.495,
                    "Capability": 1,
                    "Response_Time": 0,
                    "Total_Cost": 326
                }
            }
        }


class Dados:
    parametros: Parametros
    Delta_V: float
    Capability: int
    Response_Time: int
    Total_Cost: float
    Payload: int
    Propulsion_Type: str
    Fuel_Level: int
    Isp: int
    Bus_Mass: float
    Base_Mass: int
    Dry_Mass: float
    Mass_Frac: float
    Total_Mass: float
    Capable: int
    Fast: int
    SAU_Delta_V: float
    SAU_Capability: float
    SAU_Response_Time: float
    MAU: float
    BMF: int
    Costwet: int
    Costdry: int
    Gee: float

    def __init__(self, parametros: Parametros):
        self.Parametros = parametros
        self.Delta_V = 0.0
        self.Capability = 0
        self.Response_Time = 0
        self.Total_Cost = 0.0
        self.Payload = 0
        self.Propulsion_Type = ""
        self.Fuel_Level = 0
        self.Isp = 0
        self.Bus_Mass = 0.0
        self.Base_Mass = 0
        self.Dry_Mass = 0.0
        self.Mass_Frac = 0.0
        self.Total_Mass = 0.0
        self.Capable = 0
        self.Fast = 0
        self.BMF = parametros.constantes["BMF"]
        self.Costwet = parametros.constantes["Costwet"]
        self.Costdry = parametros.constantes["Costdry"]
        self.Gee = parametros.constantes["Gee"]

    def setPayload(self, valor: int):
        self.Payload = valor
        return self.Payload

    def setPropulsion_Type(self, valor: str):
        self.Propulsion_Type = valor
        return self.Propulsion_Type

    def setFuel_Level(self, valor: int):
        self.Fuel_Level = valor
        return self.Fuel_Level

    def setBase_Mass(self):
        self.Base_Mass = self.Parametros.variaveis_auxiliares["Base_Mass"][self.Propulsion_Type]
        return self.Base_Mass

    def setMass_Frac(self):
        self.Mass_Frac = self.Parametros.variaveis_auxiliares["Mass_Frac"][self.Propulsion_Type]
        return self.Mass_Frac

    def setBus_Mass(self):
        self.Bus_Mass = self.Payload * self.BMF + self.Base_Mass + self.Fuel_Level * self.Mass_Frac
        return self.Bus_Mass

    def setDry_Mass(self):
        self.Dry_Mass = self.Payload + self.Bus_Mass
        return self.Dry_Mass

    def setTotal_Mass(self):
        self.Total_Mass = self.Dry_Mass + self.Fuel_Level
        return self.Total_Mass

    def setIsp(self):
        self.Isp = self.Parametros.variaveis_auxiliares["Isp"][self.Propulsion_Type]
        return self.Isp

    def setDelta_V(self):
        self.Delta_V = self.Gee * self.Isp * math.log(self.Total_Mass / self.Dry_Mass, math.e) / 1000
        return self.Delta_V

    def setCapability(self):
        self.Capability = self.Parametros.variaveis_auxiliares["Capable"][self.Payload]
        return self.Capability

    def setResponse_Time(self):
        self.Response_Time = self.Parametros.variaveis_auxiliares["Fast"][self.Propulsion_Type]
        return self.Response_Time

    def setTotal_Cost(self):
        self.Total_Cost = (self.Costwet * self.Total_Mass + self.Costdry * self.Dry_Mass) / 1000
        return self.Total_Cost

    def interpolaSAU(self, atr: str, v: float):
        # Executa interpolação piecewise, ou seja, considera os extremos do
        # intervalo piecewise que contém o ponto v.
        # Retorna o SAU interpolado correspontente ao valor v.
        de_custo: bool
        peso: float
        sau: list = []
        niveis: list = []
        v0 = v1 = s0 = s1 = 0.0
        for a in self.Parametros.atributos:
            if a == atr:
                for item in self.Parametros.atributos[a]:
                    if item == "de_custo":
                        de_custo = self.Parametros.atributos[a][item]
                    elif item == "peso":
                        peso = self.Parametros.atributos[a][item]
                    elif item == "niveis":
                        niveis = self.Parametros.atributos[a][item]
                    elif item == "SAU":
                        sau = self.Parametros.atributos[a][item]
                tam = len(niveis)
                if v < niveis[0]:
                    return sau[0]
                if v > niveis[tam - 1]:
                    return sau[tam - 1]
                try:
                    t = niveis.index(v)
                except:
                    t = -1
                if t != -1:
                    return sau[t]
                else:
                    t = 0
                    while (t < tam) & ((niveis[t]) < v):
                        t += 1
                    v1 = niveis[t]
                    s1 = sau[t]
                    if t > 0:
                        v0 = niveis[t - 1]
                        s0 = sau[t - 1]
                    else:
                        v0 = niveis[0]
                        s0 = sau[0]
                return ((s1 - s0) * (v - v0) + s0 * (v1 - v0)) / (v1 - v0)

    def setSAU_Delta_V(self):
        self.SAU_Delta_V = self.interpolaSAU("Delta_V", self.Delta_V)
        return self.SAU_Delta_V

    def setSAU_Capability(self):
        self.SAU_Capability = self.interpolaSAU("Capability", self.Capability)
        return self.SAU_Capability

    def setSAU_Response_Time(self):
        self.SAU_Response_Time = self.interpolaSAU("Response_Time", self.Response_Time)
        return self.SAU_Response_Time

    def setMAU(self):
        self.MAU = self.SAU_Delta_V * self.Parametros.atributos["Delta_V"]["peso"] + \
                   self.SAU_Capability * self.Parametros.atributos["Capability"]["peso"] + \
                   self.SAU_Response_Time * self.Parametros.atributos["Response_Time"]["peso"]
        return self.MAU
