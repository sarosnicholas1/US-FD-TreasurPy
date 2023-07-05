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
        
    def format_filters(self, filters):
        """
        filters passed into parameters as list of strings 
        ["foo_bar==2023-06-30", "foo_bar<=20"]
        valid conditionals are:
        <, <=, >, >=, ==, === 
        """

        filter_conditional = {
            "<" : "lt",
            "<=" : "lte",
            ">" : "gt",
            ">=" : "gte",
            "==" : "eq",
            "===" : "in"
        }

        for index, filter in enumerate(filters):
            for condition in filter_conditional:
                if condition in filter:
                    filter = filter.replace(condition, ":"+filter_conditional[condition]+":")
                    filters[index] = filter

        filters_str = ','.join(filters)
        return filters_str
    

    def format_pagination(self, pagination):
        """
        take in paignation dictionary and return formatted string 
        page[number]={value}&page[size]={value}
        """
        pagination_arr = []
        for value in pagination:
            if value == "number" or value == "size":
                pagination_arr.append(f"page[{value}]={pagination[value]}")

            else:
                print("error wrong paignation format")

        pagination_str = '&'.join(pagination_arr)
        return pagination_str
                    




    def get_debt_to_penny(self, parameters):
        endpoint = "v2/accounting/od/debt_to_penny"

        if "fields" in parameters:
            endpoint = endpoint + "?fields=" + parameters["fields"]

        if "filters" in parameters:
            formatted_filters = self.format_filters(parameters["filters"])
            endpoint = endpoint + "?filter=" + formatted_filters


        if "pagination" in parameters:
            formatted_pagination = self.format_pagination(parameters["pagination"])
            endpoint = endpoint + "?"+formatted_pagination


        response = requests.get(self.base_url + endpoint)
        return self.checkResponse(response)



wrapper = TreasurPy()
print(wrapper.get_debt_to_penny({
    "pagination": {
        "number":1,
        "size": 10
    }

}))