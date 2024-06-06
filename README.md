### README

# Monitoramento Ambiental

## Descrição

Este projeto implementa um sistema básico de monitoramento ambiental, focando na qualidade da água e na gestão de resíduos. O sistema permite registrar e exibir dados de monitoramento da qualidade da água e dados de gestão de resíduos através de um menu interativo.

## Objetivo

O objetivo deste projeto é fornecer uma ferramenta simples para ajudar na coleta e visualização de dados ambientais, promovendo a conscientização e a tomada de decisões informadas sobre a qualidade da água e a gestão de resíduos.

## Funcionalidades

- **Monitoramento da Qualidade da Água**:
  - Registrar dados como data, local, pH, turbidez e hidrocarbonetos.
  - Exibir relatórios de monitoramento da qualidade da água.
  
- **Gestão de Resíduos**:
  - Registrar dados como data, tipo de resíduo e quantidade.
  - Exibir relatórios de gestão de resíduos.

## Requisitos

- Python 3.x

## Instalação

1. Clone o repositório para o seu ambiente local:
   ```bash
   git clone https://github.com/seuusuario/monitoramento-ambiental.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd monitoramento-ambiental
   ```

## Como Usar

### Executando o Programa

Para executar o programa, execute o script `monitoramento_ambiental.py`:
```bash
python monitoramento_ambiental.py
```

### Menu Interativo

Ao executar o script, você verá o menu principal:

```plaintext
---Menu---
[1] Monitoramento da Qualidade da Água
[2] Monitoramento dos Resíduos
[3] Sair
Insira a opção desejada:
```

Você pode escolher a opção desejada digitando o número correspondente:

- **[1] Monitoramento da Qualidade da Água**: Permite registrar dados de qualidade da água.
- **[2] Monitoramento dos Resíduos**: Permite registrar dados de gestão de resíduos.
- **[3] Sair**: Encerra o programa.

### Exemplo de Uso

1. **Monitoramento da Qualidade da Água**:
   - Selecione a opção 1 no menu.
   - Insira os dados solicitados: data, local, pH, turbidez e hidrocarbonetos.
   - O relatório atualizado será exibido.

   ```plaintext
   ---Menu---
   [1] Monitoramento da Qualidade da Água
   [2] Monitoramento dos Resíduos
   [3] Sair
   Insira a opção desejada: 1

   Monitoramento da Qualidade da Água

   Insira a data: 2024-06-01
   Insira o local: Praia Central
   Insira o pH: 7.5
   Insira a turbidez: Baixa
   Insira os hidrocarbonetos: 0.02

   Relatório de Monitoramento de Qualidade da Água
   Data: 2024-06-01, Local: Praia Central, pH: 7.5, Turbidez: Baixa, Hidrocarbonetos: 0.02
   ```

2. **Monitoramento dos Resíduos**:
   - Selecione a opção 2 no menu.
   - Insira os dados solicitados: data, tipo de resíduo e quantidade.
   - O relatório atualizado será exibido.

   ```plaintext
   ---Menu---
   [1] Monitoramento da Qualidade da Água
   [2] Monitoramento dos Resíduos
   [3] Sair
   Insira a opção desejada: 2

   Monitoramento dos Resíduos

   Insira a data: 2024-06-01
   Insira o tipo do resíduo na água: Plástico
   Insira a quantidade aproximada de resíduos (em Kg): 5

   Relatório de Gestão de Resíduos
   Data: 2024-06-01, Tipo: Plástico, Quantidade: 5 kg
   ```

## Código

Aqui está o código completo do projeto:

```python
# Monitoramento Ambiental

monitoramento_agua = []  # Lista para armazenar dados de qualidade da água

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
        print(f"Data: {registro['data']}, Local: {registro['local']}, pH: {registro['pH']}, Turbidez: {registro['turbidez']}, Hidrocarbonetos: {registro['hidrocarbonetos']}")
        print("")

# Gestão de Resíduos

gestao_residuos = []  # Lista para armazenar dados de resíduos

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
while True:
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
        exibir_relatorio_monitoramento()

    elif escolha == 2:
        # Registrando dados de gestão de resíduos
        print("")
        print("Monitoramento dos Resíduos")
        print("")
        data_Residuos = input("Insira a data: ")
        tipo_Residuo = input("Insira o tipo do resíduo na água: ")
        quantidade_Residuo = float(input("Insira a quantidade aproximada de resíduos (em Kg): "))
        registrar_residuo(data_Residuos, tipo_Residuo, quantidade_Residuo)
        exibir_relatorio_residuos()
    
    elif escolha == 3:
        break

print("")
print("---Programa Finalizado---")
```

## Melhorias Futuras

- Adicionar suporte para outros tipos de monitoramento ambiental.
- Implementar uma interface gráfica para facilitar o uso.
- Integrar com bancos de dados para armazenamento persistente dos registros.
- Adicionar validação de dados de entrada.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## Contato

Se você tiver alguma dúvida, entre em contato através do email: rm555080@fiap.com.br

## Alunos

Fernando Navajas RM555080
Henrique Botti RM556187
Pedro Ferrari RM554887

