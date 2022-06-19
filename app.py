import requests as request
from bs4 import BeautifulSoup

def updating_data(request_object, data, url):
    final1 = request_object.post(url,verify=False, data=data)
    temp_html = BeautifulSoup(final1.content,"lxml")
    viewstate = temp_html.find_all("input", type="hidden")
    data['__VIEWSTATE'] = viewstate[0]['value']
    data['__EVENTVALIDATION'] = viewstate[2]['value']
    return data, temp_html

def getting_list(html_code, request_object,url):
    selects = html_code.find_all("select",attrs={"class":"input"})
    viewstate = html_code.find_all("input", type="hidden")
    values = [2022, 6, 31, 2328, 22]
    data = {}

    for i in range(3):
        data.update({viewstate[i]['name'] : viewstate[i]['value']})
        data.update({selects[i]['name'] : values[i]})
        if (i == 2):
            data, final_html = updating_data(request_object, data, url)
    
    for i in range(2):
        data.update({selects[i+3]['name'] : values[i+3]})
        data, final_html = updating_data(request_object, data, url)
    print(final_html)

def main():
    request_object = request.Session()

    url = "https://app.cfe.mx/Aplicaciones/CCFE/Tarifas/TarifasCRENegocio/Tarifas/GranDemandaMTO.aspx"

    fetching_request_soup = request_object.get(url)

    pre_html_code = BeautifulSoup(fetching_request_soup.content, "lxml")

    getting_list(pre_html_code, request_object, url)

if __name__ == "__main__":
    main()
