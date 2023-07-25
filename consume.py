import urllib, json
import urllib.request
import urllib.parse


url="http://127.0.0.1:8000/usuario/"
#url="https://pokeapi.co/api/v2/pokemon/ditto"
response = urllib.request.urlopen(url)
data=json.loads(response.read())

print (data)
