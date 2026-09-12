# verificador-de-url
sistema em python que analisa urls e identifca caracteristicas que podem indicar riscos de segurança.
o verificador analisa a url informada pelo usuário e verifica alguns indicadores de risco, como:
uso de https
tamanho da url
tamamho do domínio e o próprio domínio
presença de endereço ip
palavras potencialmente suspeitas
pontuação de risco

a classificação do risco  é baseada em regras definidas no programa e não representa a probabilidade real de uma url ser maliciosa


(utiliza regras simples de análise e não garante que uma url seja segura ou maliciosa. a pontuação representa apenas os indicadores encontrados)


uma url com pontuação baixa não é necessariamente segura, da mesma forma que uma com pontuação alta não é necessariamente maliciosa.

as análises ficam salvas no csv com a data e o horário, a url analisada e a pontuação do risco e pode se testar mais de uma url em seguida