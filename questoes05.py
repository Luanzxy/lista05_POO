from datetime import datetime

class Paciente():
    def __init__(self, n, c, f, datetime):
        self.__nome = n
        self.__cpf = c
        self.__fone = f
        self.__nasc = datetime
    def set_nome(self,v):
        if v == "": raise ValueError("Informe o nome do paciente")
        v = self.__nome
    def set_cpf(self,v):
        if len(v) < 0: raise ValueError("Informe o CPF do paciente")
        v = self.__cpf
    def set_fone(self,v):
        if len(v) < 0: raise ValueError("Informe o fone do paciente")
        v = self.__fone
    def get_nome(self):
        return self.__nome
    def get_cpf(self):
        return self.__cpf
    def get_fone(self):
        return self.__fone  
    def get_nasc(self):
        return self.__nasc
    def idade():
        return 
    x = datetime.today()

