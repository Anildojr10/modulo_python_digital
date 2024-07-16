import pandas as pd
from datetime import datetime

def capturar_dados_cliente():
    clientes = []
    while True:
        cliente = {}
        cliente['nome'] = input("Digite o nome do cliente: ")
        cliente['email'] = input("Digite o email do cliente: ")
        cliente['telefone'] = input("Digite o telefone do cliente: ")
        cliente['data_cadastro'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        clientes.append(cliente)
        
        continuar = input("Deseja adicionar outro cliente? (s/n): ")
        if continuar.lower() != 's':
            break

    return clientes

def salvar_dados_excel(clientes, arquivo):
    # Tenta ler o arquivo existente, se não existir, cria um DataFrame vazio
    try:
        df_existente = pd.read_excel(arquivo)
    except FileNotFoundError:
        df_existente = pd.DataFrame(columns=["nome", "email", "telefone", "data_cadastro"])

    # Converte os novos clientes em um DataFrame
    df_novos_clientes = pd.DataFrame(clientes)

    # Adiciona os novos dados ao DataFrame existente
    df_atualizado = pd.concat([df_existente, df_novos_clientes], ignore_index=True)

    # Salva o DataFrame atualizado de volta no arquivo Excel
    df_atualizado.to_excel(arquivo, index=False)

def main():
    clientes = capturar_dados_cliente()
    salvar_dados_excel(clientes, 'clientes_pre_cadastro.xlsx')
    print("Dados dos clientes salvos com sucesso em clientes_pre_cadastro.xlsx.")

if __name__ == "__main__":
    main()
