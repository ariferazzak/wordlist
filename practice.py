import requests

api_key = '0ae2c66a-6f49-4e5c-ba1c-2145a8f9b786'
word = 'voluminous'
root_url = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json'
final_url = f'{root_url}/{word}?key={api_key}'
r = requests.get(final_url)
results = r.json()

for result in results:
    print(result)