# Monitoramento Ambiental

monitoramento_agua = [] # Lista para armazenar dados de qualidade da água

# Função para registrar dados de qualidade da água
def registrar_monitoramento(data, local, pH, turbidez, hidrocarbonetos):
    registro = {
        "data": data,
        "local": local,
        "pH": pH,
        "turbidez": turbidez,
        "hidrocarbonetos": hidrocarbonetos
    }
    monitoramento_agua.append(registro)

# Função para exibir relatórios de monitoramento
def exibir_relatorio_monitoramento():
    print("")
    print("Relatório de Monitoramento de Qualidade da Água")
    for registro in monitoramento_agua:
        print(f'Data: {registro['data']}, Local: {registro['local']}, pH: {registro['pH']}, Turbidez: {registro['turbidez']}, Hidrocarbonetos: {registro['hidrocarbonetos']}')
        print("")

# Gestão de Resíduos

gestao_residuos = [] # Lista para armazenar dados de resíduos

# Função para registrar resíduos gerados
def registrar_residuo(data, tipo, quantidade):
    registro = {
        "data": data,
        "tipo": tipo,
        "quantidade": quantidade
    }
    gestao_residuos.append(registro)

# Função para exibir relatórios de gestão de resíduos
def exibir_relatorio_residuos():
    print("")
    print("Relatório de Gestão de Resíduos")
    for registro in gestao_residuos:
        print(f"Data: {registro['data']}, Tipo: {registro['tipo']}, Quantidade: {registro['quantidade']} kg")
        print("")

# Criação de um Menu
while(True):
    print("---Menu---")
    print("[1] Monitoramento da Qualidade da Água")
    print("[2] Monitoramento dos Resíduos")
    print("[3] Sair")
    escolha = int(input("Insira a opção desejada: "))

    while escolha != 1 and escolha != 2 and escolha != 3:
        print("opção inválida!")
        print("")
        print("---Menu---")
        print("[1] Monitoramento da Qualidade da Água")
        print("[2] Monitoramento dos Resíduos")
        print("[3] Sair")
        escolha = int(input("Insira a opção desejada: "))

    
    if escolha == 1:
        # Registrando dados de monitoramento ambiental
        print("")
        print("Monitoramento da Qualidade da Água")
        print("")
        data_Agua = input("Insira a data: ")
        local_Agua = input("Insira o local: ")
        pH = float(input("Insira o pH: "))
        turbidez = input("Insira a turbidez: ")
        hidrocarbonetos = float(input("Insira os hidrocarbonetos: "))
        registrar_monitoramento(data_Agua, local_Agua, pH, turbidez, hidrocarbonetos)

        # Exibindo relatório de monitoramento ambiental

        exibir_relatorio_monitoramento()

    if escolha == 2:    
        # Registrando dados de gestão de resíduos
        print("")
        print("Monitoramento dos Resíduos")
        print("")
        data_Residuos = input("Insira a data: ")
        tipo_Residuo = input("Insira o tipo do resíduo na água: ")
        quantidade_Residuo = float(input("Insira a quantidade aproximada de resíduos (em Kg): "))
        registrar_residuo(data_Residuos, tipo_Residuo, quantidade_Residuo)

        # Exibindo relatório de gestão de resíduos
        exibir_relatorio_residuos()
    
    if escolha == 3:
        break

print("")
print("---Programa Finalizado---")