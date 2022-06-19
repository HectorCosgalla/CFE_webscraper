import requests as request
from bs4 import BeautifulSoup

request_object = request.Session()

url = "https://app.cfe.mx/Aplicaciones/CCFE/Tarifas/TarifasCRENegocio/Tarifas/GranDemandaMTO.aspx"

fetching_request_soup = request_object.get(url)

soup = BeautifulSoup(fetching_request_soup.content, "lxml")
viewstate = soup.find_all("input", type="hidden")
list_of_selects = soup.find_all("select",attrs={"class":"input"})

data = {
    viewstate[0]['name']:viewstate[0]['value'],
    viewstate[1]['name']:viewstate[1]['value'],
    viewstate[2]['name']:viewstate[2]['value'],
    list_of_selects[0]['name']:2022,
    list_of_selects[1]['name']:6,
    list_of_selects[2]['name']:31
}

final1 = request_object.post(url,verify=False, data=data)
soup1 = BeautifulSoup(final1.content,"lxml")
viewstate = soup1.find_all("input", type="hidden")

data = {
    viewstate[0]['name']:viewstate[0]['value'],
    viewstate[1]['name']:viewstate[1]['value'],
    viewstate[2]['name']:viewstate[2]['value'],
    list_of_selects[0]['name']:2022,
    list_of_selects[1]['name']:6,
    list_of_selects[2]['name']:31,
    list_of_selects[3]['name']:2328
}

final1 = request_object.post(url,verify=False, data=data)
soup1 = BeautifulSoup(final1.content,"lxml")
viewstate = soup1.find_all("input", type="hidden")

data = {
    viewstate[0]['name']:viewstate[0]['value'],
    viewstate[1]['name']:viewstate[1]['value'],
    viewstate[2]['name']:viewstate[2]['value'],
    list_of_selects[0]['name']:2022,
    list_of_selects[1]['name']:6,
    list_of_selects[2]['name']:31,
    list_of_selects[3]['name']:2328,
    list_of_selects[4]['name']:22
}
final1 = request_object.post(url,verify=False, data=data)
soup1 = BeautifulSoup(final1.content,"lxml")
print(soup1)