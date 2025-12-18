from estoque import Estoque
class Empresa:
    def __init__(self, razao_social, cnpj, nome_fantasia, endereco, tipo_empresa):
        self.razao_social = razao_social
        self.cnpj = cnpj
        self.nome_fantasia = nome_fantasia
        self.endereco = endereco

        self.tipo_empresa = tipo_empresa

        self.funcionarios = []

        self.estoque = Estoque()

        self.patrimonios = []