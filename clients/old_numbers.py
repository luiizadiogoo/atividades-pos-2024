import zeep

wsdl_url = "https://www.dataaccess.com/webservicesserver/numberconversion.wso?WSDL"

client = zeep.Client(wsdl=wsdl_url)

number = 19

result = client.service.NumberToWords(ubiNum=number)

print(f"O número {number} por extenso em inglês é: {result}")
