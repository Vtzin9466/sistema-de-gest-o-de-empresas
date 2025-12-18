class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        for p in self.produtos:
            if p.codigo == produto.codigo:
                p.quantidade += produto.quantidade
                return

        self.produtos.append(produto)

    def remover_produto(self, codigo):
        self.produtos = [ p for p in self.produtos if p.codigo != codigo]

    def buscar_produto(self, codigo):
        for produto in self.produtos:
            if produto.codigo == codigo:
                return produto
        return None

    def buscar_produto(self, codigointerno):
        for produto in self.produtos:
            if produto.codigointerno == codigointerno:
                return produto
        return None

    def atualizar_quantidade(self, codigo, nome_quantidade):
        produto = self.buscar_produto(codigo)
        if produto:
            produto.quantidade = nova_quantidade
        else:
            print(f'Produto com código {codigo} não encontrado.')

    def listar_estoques(self):
        if not self.produtos:
            print('Estoque vazio.')
        else:
            print('Produtos no estoque')


            for p in self.produtos:
                print(f'Código: {p.codigo}, Codigo Interno: {p.codigointerno}, Descrição: {p.descricao}, Quantidade: {p.quantidade}, Valor Unitario: R${p.valor_unitario:.2f}')
