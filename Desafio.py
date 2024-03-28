import textwrap

def menu():
    menu = """\n 
    ================Menu==============
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]Sair
    =>"""
    return input(textwrap.dedent(menu))

def depositar(saldo,valor,extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito:\tR$ {valor:2f}\n'
        print('\n=== Depósito realizado com sucesso')
    else:
        print('\n@@@ Operação falhou: O valor informado é inválido. @@@')
    return saldo,extrato

def sacar(*, saldo, valor, limite, numero_saques, limite_saques, extrato):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saques > limite_saques

    if excedeu_saldo:
        print('\n@@@ Operação falhou! Voçê não tem saldo sufuciente. @@@')
    elif excedeu_limite:
        print('\n@@@ Operação falhou! O valor de saque exede o limite. @@@')
    elif excedeu_saque:
        print('\n@@@ Operação falhou! Número de saques excedido. @@@')
    
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque:\t\tR$ {valor :.2f}\n'
        numero_saques += 1
        print('\n=== Saque realizado com secesso! ===')

    return saldo, extrato

def exibir_extrato(saldo,/,*,extrato):
    print('\n=============== EXTRATO =============')
    print('Não foram relaizadas movimentaçãoes.' if not extrato else extrato)
    print(f'\n Saldo:\t\tR$ {saldo:.2f}')
    print('\n=====================================')

def criar_usuários(usuários):
    cpf = input('Informe o CPF (somente números): ')
    usuários = filtrar_usuários(cpf,usuários)
    if usuários:
        print('\n@@@ Já existe usuário com esse CPF; @@@')
        return
    
    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereço = input('Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ')
    
    newUser = ({"nome":nome,"data_nascimento":data_nascimento,"cpf":cpf,"endereço":endereço})
    print('=== Usuário criado com sucesso! ===')
    return newUser
    

def filtrar_usuários(cpf, usuários):
    usuários_filtrados = [usuário for usuário in usuários if usuários['cpf'] == cpf]
    return usuários_filtrados[0] if usuários_filtrados else None

def criar_conta(agencia, numero_conta, usuários):
    cpf = input('Informe o CPF do usuário')
    usuários = filtrar_usuários(cpf,usuários)

    if usuários:
        print('\n=== Conta criada com secesso! ===')
        return {'agencia': agencia, 'numero_conta':numero_conta, 'usuários':usuários}
    print('\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado. @@@')

def listar_contas(contas):
    for conta in contas:
        linha = f'''\
                Agência:\t{conta['agencia']}
                C/C:\t\t{conta['número_conta']}
                Titular:\t{conta['usuário']['nome']}
        '''
        print('='*100)
        print(textwrap.dedent(linha))


def Main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuários = []
    contas = []

    while True:
        opção = menu()
        
        if opção == 'd':
            valor = float(input('Informe o valor do depósito'))

            saldo,extrato = depositar(saldo, valor,extrato)
        elif opção == 's':
            valor = float(input('Informe o valor de saque'))
             
            saldo,extrato = sacar(
                saldo = saldo,
                valor = valor,
                limite = limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
                extrato=extrato
            )
        elif opção == 'e':
            
            exibir_extrato(saldo, extrato=extrato)
        elif opção == 'nu':
            criar_usuários(usuários)
            usuários.append(criar_usuários(usuários))

        elif opção == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuários)
            if conta:
                contas.append(conta)

        elif opção == 'lc':
            listar_contas(contas)

        elif opção == 'q':
            
            break
        else:
            print('Operação invalida, por favor selecione novamente a operação desejada.')

Main()
