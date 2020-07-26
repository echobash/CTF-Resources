
a = ['0haaerw', '0Haaerw', '0hAaerw', '0HAaerw', '0haAerw', '0HaAerw', '0hAAerw', '0HAAerw', '0haaErw', '0HaaErw', '0hAaErw', '0HAaErw', '0haAErw', '0HaAErw', '0hAAErw', '0HAAErw', '0haaeRw', '0HaaeRw', '0hAaeRw', '0HAaeRw', '0haAeRw', '0HaAeRw', '0hAAeRw', '0HAAeRw', '0haaERw', '0HaaERw', '0hAaERw', '0HAaERw', '0haAERw', '0HaAERw', '0hAAERw', '0HAAERw', '0haaerW', '0HaaerW', '0hAaerW', '0HAaerW', '0haAerW', '0HaAerW', '0hAAerW', '0HAAerW', '0haaErW', '0HaaErW', '0hAaErW', '0HAaErW', '0haAErW', '0HaAErW', '0hAAErW', '0HAAErW', '0haaeRW', '0HaaeRW', '0hAaeRW', '0HAaeRW', '0haAeRW', '0HaAeRW', '0hAAeRW', '0HAAeRW', '0haaERW', '0HaaERW', '0hAaERW', '0HAaERW', '0haAERW', '0HaAERW', '0hAAERW', '0HAAERW']
import requests

def url_ok(url):
    r = requests.head(url)
    return r.status_code == 200
for i in a:
    print(i,url_ok("https://imgur.com/"+i))


