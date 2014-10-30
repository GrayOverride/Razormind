from porc import Client
import requests

#Db connection
client = Client("7ea55ba5-4aa3-4bc0-8c2c-722a638f36ef")
client.ping().raise_for_status()

#datainsamling
arbetsfor = requests.get('https://www.kimonolabs.com/api/ay62uqwk?apikey=296d7af19aa06eafb66d56159770aab5')
metrojobb = requests.get('https://www.kimonolabs.com/api/93vsz4g4?apikey=296d7af19aa06eafb66d56159770aab5')
monster = requests.get('https://www.kimonolabs.com/api/5ke77d8q?apikey=296d7af19aa06eafb66d56159770aab5')


arbetsforData = arbetsfor.json()
metrojobbdata = metrojobb.json()
monsterData = monster.json()


#skapa arrayer att appenda till den relevanta filtrerade datan
metroRelinfo = []
arbetsforRelinfo = []
monsterRelinfo = []


#Filtrera arbetsförmedlingens data
for i in arbetsforData['results']['collection1']:
    arbetsforRelinfo.append(i['Rubrik'])
arbetsAntal = len(arbetsforRelinfo)

#Filtrera Metrojobb
for i in metrojobbdata['results']['collection1']:
    metroRelinfo.append(i['jobb'])
metroAntal = len(metroRelinfo)

#Metro jobb
for i in monsterData['results']['collection1']:
    monsterRelinfo.append(i['Titel'])
monsterAntal = len(monsterRelinfo)


#räkna ihop antal lediga jobb, for fun mostly
print(arbetsAntal+metroAntal+monsterAntal)
print(monsterRelinfo)


def dbupdate():
    client.put('Gamma','jobb', {
      "arbetsformedlingen": arbetsforRelinfo,
      "metrojobb": metroRelinfo,
      "monsterjobb": monsterRelinfo
    })
def dbget():
    alphaTest = client.get('Beta', 'jobb')


#dbupdate()