from binance.spot import Spot
from connect_setting import key,secret

client = Spot()
print(client.time())

