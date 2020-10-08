# guardar-paginaweb.py

import urllib.request, urllib.error, urllib.parse

#url = 'https://sites.google.com/site/cryonicsfactsheet/cold-filter'
url = input('URL: ')
pagename = input('name: ')
respuesta = urllib.request.urlopen(url)
contenidoWeb = respuesta.read()
page='{}.html'.format(pagename)
f = open(page, 'wb')
f.write(contenidoWeb)
f.close()
