from shodan import Shodan
from Componentes import ApiShodan

api = Shodan(ApiShodan)

# Lookup an IP
ipinfo = api.host('sosmatic.es')
print(ipinfo)

