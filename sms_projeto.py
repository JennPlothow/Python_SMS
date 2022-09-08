import pandas as pd
from twilio.rest import Client
account_sid = "ACf1fb2765a8b017358e8e0359d0d09a98"
auth_token  = "df722d53265ba2c0bd07ab151920b077"
client = Client(account_sid, auth_token)

lista_meses=['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',]
for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor= tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas=tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mes de {mes}, vendedor {vendedor} bateu a meta com {vendas} de vendas')
    message = client.messages.create(
        to="+5511958033352", 
        from_="+12513128777",
        body='Parabéns você conquistou meu coração!')
    print(message.sid)
        



        