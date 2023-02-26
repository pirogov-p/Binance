from binance.spot import Spot as Client
from connect_setting import api_key2, api_secret2

client = Client(api_key2, api_secret2)
print(client.account())
