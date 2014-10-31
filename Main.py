from porc import Client
import requests
import secrets

#Db connection
client = Client(secrets.key['orchkey']);
client.ping().raise_for_status()

#datainsamling
arbetsfor = requests.get(secrets.key['sourcerurlAF']);
metrojobb = requests.get(secrets.key['sourcerurlMJ']);
monster = requests.get(secrets.key['sourceurlMon']);


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
