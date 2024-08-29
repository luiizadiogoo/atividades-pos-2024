import zeep

wsdl_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"

client = zeep.Client(wsdl=wsdl_url)

country_code = "NO"

result = client.service.CapitalCity(sCountryISOCode=country_code)

print(f"A capital da Noruega ({country_code}) é {result}")
