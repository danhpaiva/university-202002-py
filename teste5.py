import requests

response = requests.post('https://httpbin.org/post', json={'id': 1, 'name': 'Elson'})

print("Status code: ", response.status_code)
print("Resposta de entrada:")
print(response.json())