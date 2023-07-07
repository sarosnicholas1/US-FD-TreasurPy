import requests


class TreasurPy():
    def __init__(self):
        self.base_url = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service/"

    def checkResponse(self, resp):
        if resp.status_code == 200:
            return resp.json()
        
        #checks validity of fields
        else:
            return "API call failed check formatting. Status code: " + resp.status_code
        

    def format_fields(self, fields):
        """
        fields passed in as list of strings
        return list as comma seperated string
        """
        fields_str = ','.join(fields)
        return fields_str

        
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
    

    def format_sorting(self, sorting):
        """
        take in sorting dictionary which has a key of the feild name and a value of increasing or decreasing
        format correctly and return as comma seperated list
        """
        sorting_arr = []
        for value in sorting:
            if sorting[value] == "increasing":
                sorting_arr.append(f"+{value}")

            elif sorting[value] == "decreasing":
                sorting_arr.append(f"-{value}")

            else:
                print("error wrong sorting format format")
        
        sorting_str = ','.join(sorting_arr)
        return sorting_str
    

    def format_output(self,format):
        """
        formats the output type of the request
        takes in string 
        """
        output_opt = ["csv", "json", "xml"]
        
        if format not in output_opt:
            print("error on output format options")
        else:
            return format

    def add_parameters(self, parameters, endpoint):
        """
        function for adding all parameters to a specified endpoint
        previously was included in each get function but remove to clean code
        takes in a parameters dictionary and an endpoint string 
        returns an endpoit string that has been formatted with the provided parameters
        """

        if "fields" in parameters:
            formatted_fields = self.format_fields(parameters["fields"])
            endpoint = endpoint + "?fields=" + formatted_fields

        if "filters" in parameters:
            formatted_filters = self.format_filters(parameters["filters"])
            endpoint = endpoint + "?filter=" + formatted_filters

        if "pagination" in parameters:
            formatted_pagination = self.format_pagination(parameters["pagination"])
            endpoint = endpoint + "?"+formatted_pagination

        if "sorting" in parameters:
            formatted_sorting = self.format_sorting(parameters["sorting"])
            endpoint = endpoint + "?sort=" + formatted_sorting

        if "format" in parameters:
            formatted_output = self.format_output(parameters["format"])
            endpoint = endpoint + "?format=" + formatted_output

        return endpoint


    def get_debt_to_penny(self, parameters):
        endpoint = "v2/accounting/od/debt_to_penny"
        formatted_endpoint = self.add_parameters(parameters, endpoint)

        print(self.base_url+formatted_endpoint)
        response = requests.get(self.base_url + formatted_endpoint)
        return self.checkResponse(response)
    

    def get_daily_treasury_statement(self, parameters):
        """
        function for accessing the daily treasury statement dataset
        """
        endpoint = "v1/accounting/dts/dts_table_1"
        formatted_endpoint = self.add_parameters(parameters, endpoint)

        print(self.base_url+formatted_endpoint)
        response = requests.get(self.base_url + formatted_endpoint)
        return self.checkResponse(response)
    

    
    def get_120_day_delinquent_debt_referral_compliance_report(self, parameters):
        """
        function for accessing the 120_day_delinquent_debt_referral_compliance_report dataset
        """
        endpoint = "v2/debt/tror/data_act_compliance"
        formatted_endpoint = self.add_parameters(parameters, endpoint)

        print(self.base_url+formatted_endpoint)
        response = requests.get(self.base_url + formatted_endpoint)
        return self.checkResponse(response)
    

    
    def get_gold_reserve(self, parameters):
        """
        function for accessing the get_us_treasury_owned_gold dataset
        """
        endpoint = "v2/accounting/od/gold_reserve"
        formatted_endpoint = self.add_parameters(parameters, endpoint)

        print(self.base_url+formatted_endpoint)
        response = requests.get(self.base_url + formatted_endpoint)
        return self.checkResponse(response)
    

    def get_record_setting_auction(self,parameters):
        """
        function for accessing the get recordSetting_treasury_securities_auction_data 
        """
        endpoint = "v2/accounting/od/record_setting_auction"
        formatted_endpoint = self.add_parameters(parameters, endpoint)

        print(self.base_url+formatted_endpoint)
        response = requests.get(self.base_url + formatted_endpoint)
        return self.checkResponse(response)
    

    def get_slgs_securities(self,parameters):
        """
        function for accessing the get recordSetting_treasury_securities_auction_data 
        """
        endpoint = "v1/accounting/od/slgs_securities"
        formatted_endpoint = self.add_parameters(parameters, endpoint)

        print(self.base_url+formatted_endpoint)
        response = requests.get(self.base_url + formatted_endpoint)
        return self.checkResponse(response)


