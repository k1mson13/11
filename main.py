import requests
from discord import Webhook, RequestsWebhookAdapter
from datetime import datetime
import time

loop = 0
now = datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")

discord_server = 'https://discord.com/api/webhooks/999360194674950225/_x5KvjgYdLSENAhD-GjoJ19uTa1DH3nKb8vU-tDGQXlPhjDAHlBUNPlwWIWA07B5ub9G'
webhook = Webhook.from_url(discord_server, adapter=RequestsWebhookAdapter())
sale_price = 0
headers = {
    'Host': 'eu1-search.doofinder.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Access-Control-Request-Method': 'GET',
    'Access-Control-Request-Headers': 'authorization,content-type',
    'Origin': 'https://www.pcdiga.com',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    "accept-language": "pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7,pl;q=0.6"

}

dictionary = [
    "SSD M.2 2280 Kingston NV1 1TB 3D TLC NVMe",
    "Processador AMD Ryzen 5 5600G 6-Core 3.9GHz c/ Turbo 4.4GHz 19MB SktAM4",
    "Processador AMD Ryzen 5 5600 6-Core 3.5GHz c/ Turbo 4.4GHz 35MB SktAM4",
    "Motherboard ATX MSI B450-A Pro Max",
    "Placa Gráfica Sapphire Nitro+ Radeon RX 6600 XT 8GB GDDR6 OC",
    "Fonte de Alimentação Corsair RM Series RM750 80+ Gold Full Modular",
    "Cooler CPU Cooler Master Hyper 212 LED Turbo Red Top Cover",
    "Caixa ATX Nox Hummer TGM RGB com Janela Preta",
    "Placa Gráfica Zotac Gaming GeForce RTX 3060 12GB GDDR6 Twin Edge",
    "SSD M 2 2280 Kingston NV1 1TB 3D TLC NVMe",
]
data = []
webhook.send("-------------------------------{}-------------------------------".format(current_time))
for i in dictionary:
    url = 'https://eu1-search.doofinder.com/5/search?query={}&rpp=36&hashid=640da766ebf70dbfeb06e1556cae3490'.format(i)
    html_text = requests.get(url, headers=headers)
    json_format = html_text.json()

    for each_entry in json_format['results']:
        if "title" in each_entry:
            for x in each_entry:
                if i == each_entry.get("title"):
                    if each_entry.get("availability") == "em stock":
                        stock = 'YES'
                    else:
                        stock = 'NO'
                    if each_entry.get("sale_price") == None:
                        sale_price = 0
                    else:
                        sale_price = each_entry.get("sale_price")

                    ID = each_entry.get("id")
                    Nome = each_entry.get("title")
                    price = each_entry.get("price")
                    best_price = each_entry.get("best_price")
                    print(" ID: {},\n Title: {},\n Price: {}€,\n Best_Price: {}€,\n Promotion: {}€,\n Stock: {},".format(ID, Nome, price, best_price, sale_price, stock))
                    webhook.send(" ID: {},\n Title: {},\n Price: {}€,\n Best_Price: {}€,\n Promotion: {}€,\n Stock: {},".format(ID,Nome,price,best_price,sale_price,stock))
                    webhook.send("#################################################################")
                break

