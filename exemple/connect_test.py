from binance.spot import Spot


client = Spot()

# Get server timestamp
print(client.time())