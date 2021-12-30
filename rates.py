import requests

url = 'https://v6.exchangerate-api.com/v6/f30681b156e77c4d338453cd/pair/USD/ZAR'




# Where USD is the base currency you want to use


# Making our request
response = requests.get(url)
data = response.json()
rate = data['conversion_rate']
# Your JSON object
print(rate)
		
