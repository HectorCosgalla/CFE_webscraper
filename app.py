import requests as request
import json
from bs4 import BeautifulSoup

def updating_data(request_object, data, url):
    temp_request_object = request_object.post(url,verify=False, data=data)
    temp_html = BeautifulSoup(temp_request_object.content,"lxml")
    viewstate = temp_html.find_all("input", type="hidden")
    data['__VIEWSTATE'] = viewstate[0]['value']
    data['__EVENTVALIDATION'] = viewstate[2]['value']
    return data, temp_html

def getting_table(html_code, request_object,url):
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
    
    price_table = final_html.find_all("table", attrs={"class":"table"})
    return price_table

def main():
    request_object = request.Session()

    url = "https://app.cfe.mx/Aplicaciones/CCFE/Tarifas/TarifasCRENegocio/Tarifas/GranDemandaMTO.aspx"

    fetching_request_soup = request_object.get(url)

    pre_html_code = BeautifulSoup(fetching_request_soup.content, "lxml")

    price_table = getting_table(pre_html_code, request_object, url)

    parsed_price_table = BeautifulSoup(str(price_table), "html.parser")

    print(parsed_price_table)
    
    rows = parsed_price_table.find_all("tr")

    data = []
    for row in rows:
        cells = row.find_all("td")
        items = []
        for index in cells:
            items.append(index.text.strip())
        data.append(items)
    print(json.dumps(data, indent=4))

    #print(json.dumps(dict(table_data)))

if __name__ == "__main__":
    main()
