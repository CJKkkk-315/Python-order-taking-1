import requests

url = "https://www.1miba.com/soutu/upload"

f = open('20220305094906.png','rb')
files={
  'file':f

}
response = requests.post(url,files=files)

print(response.text)
