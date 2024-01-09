from cleantext import clean
text = """🚨🚨🚨  Traavley: oportunidades de resgate 🚨🚨🚨

👉 Origem: GRU-São Paulo
👉 Destino: RAK-Marrakech
👉 Programa de Fidelidade: Smiles 

🛎 Datas de ida:
Abril: 3

💰 Preço: 78.900 milhas o trecho.

💰 Taxas: R$183,20

💺 Classe: Econômica. 

✈ Cia Aérea Operando o Voo: AirEuropa

📍 Continente: África

Traavley: oportunidades de resgate

👉 Origem: POA-Porto Alegre
👉 Destino: USH-Ushuaia
👉 Programa de Fidelidade: Smiles

🛎 Datas de ida:
Julho: 1

🛎 Datas de volta:
Julho: 8

💰 Preço: 46.100 milhas o trecho.

💰 Taxas: R$470,34 ida e volta

💺 Classe: Econômica. 

✈ Cia Aérea Operando o Voo: Sky

📍 Continente: América do Sul


Traavley: oportunidades de resgate

👉 Origem: CNF-Belo Horizonte
👉 Destino: LAX-Los Angeles
👉 Programa de Fidelidade: LatamPass

🛎 Datas de ida:
Abril: 21

🛎 Datas de volta:
Maio: 1

💰 Preço: 37.706 milhas o trecho.

💰 Taxas: R$280,01 a ida e R$188,42 a volta

💺 Classe: Econômica. 

✈ Cia Aérea Operando o Voo: Latam

📍 Continente: América do Norte

É necessário pesquisar ida e volta para encontrar esses valores. Pesquise datas próximas.
"""
clean_text = (clean(text, no_emoji=True, lower=False, no_line_breaks=False))

split_text = clean_text.split('Traavley: oportunidades de resgate')


# regex: Origem: (\s*.*)
# Destino: (\s*.*)
# Programa de Fidelidade: (\s*.*)