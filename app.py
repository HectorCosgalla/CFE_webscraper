import requests as request
from bs4 import BeautifulSoup

def getting_list(html_code):
    selects = html_code.find_all("select",attrs={"class":"input"})
    viewstate = html_code.find_all("input", type="hidden")
    values = [2022, 6, 31, 2328, 22]
    data = {}

    for i in range(3):
        data.update({viewstate[i]['name'] : viewstate[i]['value']})
        data.update({selects[i]['name'] : values[i]})
        if (i == 2):
            final1 = request_object.post(url,verify=False, data=data)
            soup1 = BeautifulSoup(final1.content,"lxml")
            viewstate = soup1.find_all("input", type="hidden")
            data['__VIEWSTATE'] = viewstate[0]['value']
            data['__EVENTVALIDATION'] = viewstate[2]['value']
    
    for i in range(2):
        data.update({selects[i+3]['name'] : values[i+3]})
        final1 = request_object.post(url,verify=False, data=data)
        soup1 = BeautifulSoup(final1.content,"lxml")
        viewstate = soup1.find_all("input", type="hidden")
        data['__VIEWSTATE'] = viewstate[0]['value']
        data['__EVENTVALIDATION'] = viewstate[2]['value']
        print(soup1)




request_object = request.Session()

url = "https://app.cfe.mx/Aplicaciones/CCFE/Tarifas/TarifasCRENegocio/Tarifas/GranDemandaMTO.aspx"

fetching_request_soup = request_object.get(url)

pre_html_code = BeautifulSoup(fetching_request_soup.content, "lxml")

getting_list(pre_html_code)
"""

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
"""
