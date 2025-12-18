class tipoEmpresa:
    TIPOS = {
        'I': 'Indústria',
        'C': 'Comércio',
        'S': 'Serviços',
        'M': 'Mista',
    }

    def __init__(self, codigo):
        if codigo not in self.TIPOS:
            raise ValueError("Tipo de empresa invalido")

        self.codigo = codigo

        self.descricao = self.TIPOS[codigo]