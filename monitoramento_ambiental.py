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

