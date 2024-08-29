import zeep
import json

wsdl_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"

client = zeep.Client(wsdl=wsdl_url)

country_code = "NZ"

result = client.service.CapitalCity(sCountryISOCode=country_code)

print(f"A capital da Nova Zelândia ({country_code}) é {result}")

json_str = json.dumps(zeep.helpers.serialize_object(result), indent=4)

print(json_str)
