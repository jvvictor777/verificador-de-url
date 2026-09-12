url = input("digite a URL: ")
risco = 0

if url.startswith("https://"):
    print('HTTPS: Sim, Protocolo seguro')
else:
    print('HTTPS: Não, Alerta')
    risco += 2

if len(url)> 100:
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
"secure"
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
