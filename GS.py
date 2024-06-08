# Dados para cada parâmetro
dados = {
    "pH": {
        "informacao": "O pH da água deve estar entre 7.0 e 8.5 para garantir a saúde dos organismos marinhos.",
        "referencia": "https://pt.m.wikipedia.org/wiki/Acidifica%C3%A7%C3%A3o_oce%C3%A2nica"
    },
    "salinidade": {
        "informacao": "A salinidade da água do mar varia entre 3.5% e 3.7%, sendo crucial para a sobrevivência de diversas espécies.",
        "referencia": "https://pt.m.wikipedia.org/wiki/Salinidade"
    },
    "temperatura": {
        "informacao": "A temperatura da água afeta diretamente a vida marinha, sendo ideal que se mantenha estável e dentro dos limites normais da região.",
        "referencia": "https://www.temperaturadomar.pt/#:~:text=Com%20uma%20m%C3%A9dia%20que%20varia,agrad%C3%A1vel%20durante%20o%20ano%20todo."
    },
    "turbidez": {
        "informacao": "A turbidez da água pode indicar a presença de partículas em suspensão, afetando a penetração da luz e a vida marinha.",
        "referencia": "https://hidromares.com.br/blog/blog-turbidez-da-agua-do-mar/#:~:text=Os%20cientistas%20costumam%20considerar%20a,que%20n%C3%A3o%20est%C3%A3o%20funcionando%20adequadamente."
    }
}

# Função para exibir informações sobre o parâmetro escolhido pelo usuário
def exibir_informacoes(parametro):
    if parametro in dados:
        print("Informação:", dados[parametro]["informacao"])
        print("Referência:", dados[parametro]["referencia"])
    else:
        print("Parâmetro não encontrado. Por favor, escolha entre pH, salinidade, temperatura ou turbidez.")

# Programa principal
while True:
    parametro = input("Digite o parâmetro que deseja consultar (pH, salinidade, temperatura, turbidez) ou 'sair' para encerrar: ").lower()
    if parametro == 'sair':
        break
    exibir_informacoes(parametro)
