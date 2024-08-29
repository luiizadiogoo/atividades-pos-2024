import zeep
import json

wsdl_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"

client = zeep.Client(wsdl=wsdl_url)

functions = [
    ('CountryCurrency', 'NZ'), 
    ('CountryName', 'FR'),      
    ('CountryISOCode', 'DE') 
]

for function, country_code in functions:
    result = getattr(client.service, function
                     )(sCountryISOCode=country_code)
    
    print(f"O resultado da função {function} para o país {country_code} é {result}")

    json_str = json.dumps(zeep.helpers.serialize_object(result), indent=4)
    
    print(json_str)
