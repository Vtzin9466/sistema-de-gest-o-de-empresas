from tipoEmpresa import tipoEmpresa
from empresa import Empresa
from funcionario import Funcionario
from produto import Produto
from bemPatrimonial import bemPatrimonial

class SistemaEmpresa:
    def __init__(self):
        self.empresas = []

    def cadastrar_empresa(self):
        print('\n--- Cadastro de Empresa ---')

        razao_social = input('Razao Social: ')
        cnpj = input('CNPJ: ')
        nome_fantasia = input('Nome Fantasia: ')
        enderco = input('Enderço: ')

        print('\nTipos de Empresas Disponíveis:')
        for cod, desc in tipoEmpresa.TIPOS.items():
            print(f'{cod} - {desc}')

        tipo = input('Digite o tipo de empresa: ').upper()

        try:
            tipo_empresa = tipoEmpresa(tipo)

            nova_empresa = Empresa(razao_social, cnpj, nome_fantasia, enderco, tipo_empresa)

            self.empresas.append(nova_empresa)

            print('\nEmpresa cadastrada com sucesso!')

        except ValueError as e:
            print(f'Erro: {e}')

    def menu_principal(self):
        while True:
            print('\n-- SISTMA DE GESTÃO DE EMPRESAS --')
            print('1 - Cadastrar Empresa')
            print('2 - Listar Empresas')
            print('3 - Adicionar Funcionario')
            print('4 - Gerenciar Estoque')
            print('5 - Listar Funcionarios')
            print('6 - Gerenciar Patrimonio')
            print('7 - Sair')

            opcao = input('Escolha uma opção: ')

            if opcao == '1':
                self.cadastrar_empresa()
            elif opcao == '2':
                self.listar_empresas()
            elif opcao == '3':
                self.adicionar_funcionario()
            elif opcao == '4':
                self.gerenciar_estoque()
            elif opcao == '5':
                self.listar_funcionarios()
            elif opcao == '6':
                self.gerenciar_patrimonio()
            elif opcao == '7':
                print('Saindo...')
                break
            else:
                print('Opção invalida!')

    def listar_empresas(self):
        print("\n-- Empresa Cadastradas --")
        for empresa in self.empresas:
            print(f'\nRazão Social: {empresa.razao_social}')
            print(f'CNPJ: {empresa.cnpj}')
            print(f'Nome Fantasia: {empresa.nome_fantasia}')
            print(f'Tipo: {empresa.tipo_empresa.descricao}')
            print(f'Funcionários: {len(empresa.funcionarios)}')
            print(f'Patrimônios: {len(empresa.patrimonio)}')

    def adicionar_funcionario(self):
        if not self.empresas:
            print('Nenhuma empresa cadastrada ainda')
            return

        print('\nSelecione a empresa')
        for i, empresa in enumerate(self.empresas, 1):
            print(f'{i} - {empresa.nome_fantasia}')

        try:
            escolha = int(input('Escolha: ')) - 1

            empresa_selecionada = self.empresas[escolha]

            print (f'\nAdicionar funcionario á {empresa_selecionada.nome_fantasia}')
            nome= input('Nome do funcionario: ')
            cpf= input('CPF: ')
            cargo = input('Cargo: ')
            salario = float(input('Salario: '))

            novo_func = Funcionario(nome, cpf, cargo, salario)

            empresa_selecionada.funcionarios.append(novo_func)
            print('Funcionário adicionado com sucesso!')
        except (ValueError, IndexError):
            print('Seleção inválida!')

    def gerenciar_estoque(self):
        if not self.empresas:
            print('Nenhuma empresa cadastrada ainda')
            return

        print('\nSelecione a empresa para gerenciar o estoque')
        for i, empresa in enumerate(self.empresas, 1):
            print(f'{i} - {empresa.nome_fantasia}')

        try:
            escolha = int(input('Número da empresa: ')) - 1
            empresa = self.empresas[escolha]
        except (ValueError, IndexError):
            print('Seleção Inválida')
            return

        while True:
            print('\n-- Estoque de {empresa.nome_fantasia}')
            print('1 - Adicionar Produto')
            print('2 - Atualizar Quantidade')
            print('3 - Remover Produto')
            print('4 - Listar Produtos')
            print('5 - Voltar ao menu principal')

            opcao = input('Escolha uma opção: ')

            if opcao == '1':
                codigo = input('Codigo do produto: ')
                descricao = input('Descricao=: ')
                quantidade = int(input('Quantidade: '))
                valor = float(input('Valor unitário: '))
                produto = Produto(codigo, descricao, quantidade, valor)
                empresa.estoque.adicionar_produto(produto)
                print('Produto adicionado com sucesso!')

            elif opcao == '2':
                codigo = input('Codigo do produto: ')
                nova_qtd = int(input('Quantidade: '))
                empresa.estoque.atualizar_quantidade(codigo, nova_qtd)

            elif opcao == '3':
                codigo = input('Codigo do produto: ')
                empresa.estoque.remover_produto(codigo)
                print('Produto removido (se existir')

            elif opcao == '4':
                empresa.estoque.listar_estoques()

            elif opcao == '5':
                break

            else:
                print('Opção Invalida!')

    def listar_funcionarios(self):
        if not self.empresas:
           print('Nenhuma empresa cadastrada ainda')
           return

        print('\nSelecione a empresa para ver os funcionarios')
        for i, empresa in enumerate(self.empresas, 1):
           print(f'{i} - {empresa.nome_fantasia}')

        try:
            escolha = int(input('Número da empresa: ')) - 1
            empresa = self.empresas[escolha]


            print(f'\n-- Funcionário da empresa {empresa.nome_fantasia} --')

            if not empresa.funcionarios:
                print('Nenhum funcionario cadastrado')
            else:
                for i, func in enumerate(empresa.funcionarios, 1):
                    print(f'\nFuncionário {i}:')
                    print(f'Nome: {func.nome}')
                    print(f'Cpf: {func.cpf}')
                    print(f'Cargo: {func.cargo}')
                    print(f'Salario: {func.salario:2f}')
        except (ValueError, IndexError):
            print('Seleção Inválida!')

    def gerenciarPatrimonio(self):
        if not self.empresas:
            print('Nenhuma empresa cadastrada ainda')
            return

        print('\nSelecione a empresa para gerenciar o patrimonios')
        for i, empresa in enumerate(self.empresas, 1):
            print(f'{i} - {empresa.nome_fantasia}')

        try:
            escolha = int(input('Número da empresa: ')) - 1
            empresa = self.empresas[escolha]

        except (ValueError, IndexError):
            print("Seleção inválida!")
            return

        while True:
            print('\n-- Patrimonio de {empresa.nome_fantasia}')
            print('1 - Adicionar Bem Patrimonial')
            print('2 - Remover Bem Patrimonial')
            print('3 - Listar Bem Patrimonial')
            print('4 - Voltar ao menu principal')

            opcao = input('Escolha a opção: ')

            if opcao == '1':
                codigo = input('Codigo do bem: ')
                descricao = input('Descricao: ')
                valor= float(input('Valor do bem: '))
                data = input('Data de aquisição (dd/mm/aaa): ')
                bem = bemPatrimonial(codigo, descricao, valor, data)
                empresa.patrimonio.append(bem)
                print('Bem patrimonial adicionado com sucesso!')

            elif opcao == '2':
                codigo = input('Codigo do bem a remover: ')
                original = len(empresa.patrimonio)
                empresa.patrimonio = [b for b in empresa.patrimonio if b.codigo != codigo]
                if len(empresa.patrimonio) < original:
                    print('Bem removido com sucesso!')
                else:
                    print('Bem não encontrado!')

            elif opcao == '3':
                if not empresa.patrimonio:
                    print('Nenhum patrimonio cadastrado! ')
                else:
                    for i, bem in enumerate(empresa.patrimonio, 1):
                        print(f'\nBem {i}: ')
                        print(f'Código: {bem.codigo}')
                        print(f'Descricao: {bem.descricao}')
                        print(f'Valor: R${bem.valor_unitario:.2f}')
                        print(f'Data de Aquisição: {bem.data_aquisicao}')
            elif opcao == '4':
                break
            else:
                print('Opção Invalida!')

if __name__ == '__main__':
    sistema = SistemaEmpresa()
    sistema.menu_principal()

