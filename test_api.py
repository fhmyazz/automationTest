import requests

getResponse = requests.get('https://jsonplaceholder.typicode.com/posts')
print(getResponse.text)

data = {'title': 'recommendation',
        'body': 'motorcycle',
        'userId': 12}
postResponse = requests.post(url='https://jsonplaceholder.typicode.com/posts', data=data)
print(postResponse.text)