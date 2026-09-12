url = input("digite a URL: ")
risco = 0

if url.startswith("https://"):
    print('HTTPS: V')
else:
    print('HTTPS: X')
    risco += 2

if len(url)> 100:
    print("URL muito longa: X")
    risco += 1
else:
    print("URL muito longa: V")


if "192.168" in url:
    print ("Possui ip: X")
    risco += 2
else:
    print ("Possui ip: V")


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
        print("Palavras suspeitas: encontradas")
        risco += len(encontradas)
else:
        print("palavras suspeitas: V")

print('pontuação', risco)

if risco <= 1:
    print("Risco: Baixo")
elif risco <= 3:
    print("Risco: Médio")
else:
    print("Risco: Alto")
