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
    print("Relatório de Gestão de Resíduos")
    for registro in gestao_residuos:
        print(f"Data: {registro['data']}, Tipo: {registro['tipo']}, Quantidade: {registro['quantidade']} kg")

# Exemplo de uso do projeto

# Registrando dados de monitoramento ambiental
data = input("Insira a data: ")
local = input("Insira o local: ")
pH = float(input("Insira o pH: "))
turbidez = input("Insira a turbidez: ")
hidrocarbonetos = float(input("Insira os hidrocarbonetos: "))
registrar_monitoramento(data, local, pH, turbidez, hidrocarbonetos)

# Exibindo relatório de monitoramento ambiental

exibir_relatorio_monitoramento()