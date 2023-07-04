import requests


class TreasurPy():
    def __init__(self):
        self.base_url = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service/"

    def checkResponse(self, resp):
        if resp.status_code == 200:
            return resp.json()
        
        #checks validity of fields
        elif resp.status_code == 400:
            return "Fields not valid"
        else:
            return resp.status_code



    def get_debt_to_penny(self, parameters):
        endpoint = "v2/accounting/od/debt_to_penny"

        if "fields" in parameters:
            endpoint = endpoint + "?fields=" + parameters["fields"]


        if "pagination" in parameters:
            endpoint = endpoint + "?page[number]=" + parameters["pagination"]["number"] + "&page[size]=" + parameters["pagination"]["size"]


        response = requests.get(self.base_url + endpoint)
        return self.checkResponse(response)



wrapper = TreasurPy()
print(wrapper.get_debt_to_penny({
    "pagination": {
        "number":"2",
        "size":"500"
    }

}))