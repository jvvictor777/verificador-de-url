import csv
from datetime import datetime
from urllib.parse import urlparse 

def salvar_historico(url, risco):
    with open ("historico.csv", "a", newline="", encoding = "utf-8") as file:
        escritor = csv.writer(file)

        escritor.writerow([datetime.now().strftime("%d%m%Y %H%M%S"),
                        url,
                        risco,])

while True:
    url = input("digite a URL: ")
    risco = 0

    dados = urlparse(url)
    dominio = dados.hostname

    print("Dominío:", dominio)

    if dominio and len(dominio) > 15:
        print("domínio muito longo")
        risco += 1
    else:
        print("tamanho do domínio: normal")

    if dominio:
        quantidade = dominio.count(".")

    print("quant. pontos:", quantidade)


    if quantidade > 3:
        print("muitos subdomínios")
        risco += 1
    else:
        print("quant. subdomínios: normal")   



    if url.startswith("https://"):
        print('HTTPS: Sim, Protocolo seguro')
    else:
        print('HTTPS: Não, Alerta')
    risco += 2

    if len(url)> 75:
        print("URL muito longa: Acima do recomendado, alerta")
        risco += 1
    else:
        print("URL muito longa: não, ok")


    if "192.168" in url:
        print ("Possui ip: IP no lugar do domínio, alerta")
        risco += 2
    else:
        print ("Possui ip: não, ok")


    palavras_suspeitas = [ 
"login",
"verify",
"verification",
"password",
"account",
"confirm",
"secure",
"signin",
"sign-in",
"authenticate",
"authentication",
"credential",
"credentials",
"update",
"validate",
"validation",
"recover",
"recovery",
"reset",
"unlock",
"suspended",
"suspension",
"security",
"purchase",
"payment",
"deadline",
"transfer"

]
    encontradas = []

    for palavra in palavras_suspeitas:
        if palavra in url.lower():
            encontradas.append(palavra)


    if encontradas:
        print("Palavras suspeitas: encontradas:" + ", ".join(encontradas))
        risco += len(encontradas)
    else:
        print("palavras suspeitas: não")

    print('pontuação', risco)

    if risco <= 1:
        print("Risco: Baixo")
    elif risco <= 3:
        print("Risco: Médio")
    else:
        print("Risco: Alto")

    salvar_historico(url, risco,)
    print("análise salva no histórico")

    continuar = input("Deseja analisar outra URL? (sim/não):").lower()

    if continuar != "sim":
        print("encerrando programa...")
    break 

