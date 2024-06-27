<h1>Implementação de algumas funcionalidades em um sistema bancário utilizando <u>Python</u>.</h1> 
<h2>
#Funcionalidades: 
</h2>
'''mermaid
graph TD;
    A[Menu] -->|Selecionar opção| B{Opção selecionada?}
    B -->|Depositar| C(Depositar)
    B -->|Sacar| D(Sacar)
    B -->|Extrato| E(Extrato)
    B -->|Novo usuário| F(Novo usuário)
    B -->|Nova conta| G(Nova conta)
    B -->|Listar contas| H(Listar contas)
    B -->|Sair| I(Sair)
    C --> A
    D --> A
    E --> A
    F --> A
    G --> A
    H --> A
    I --> J{Confirmar saída?}
    J -->|Sim| K(Terminar execução)
    J -->|Não| A


'''
<h3>#Python DOCs:</h3>https://docs.python.org/3/

