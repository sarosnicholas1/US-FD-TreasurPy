import requests

def checkResponse(resp):
        if resp.status_code == 200:
            return resp.json()
        
        #checks validity of fields
        else:
            return "API call failed check formatting. Status code: " + resp.status_code
        

def format_fields(fields):
        """
        fields passed in as list of strings
        return list as comma seperated string
        """
        fields_str = ','.join(fields)
        return fields_str

        
def format_filters(filters):
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


def format_pagination(pagination):
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
    

def format_sorting(sorting):
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
    

def format_output(format):
        """
        formats the output type of the request
        takes in string 
        """
        output_opt = ["csv", "json", "xml"]
        
        if format not in output_opt:
            print("error on output format options")
        else:
            return format

def add_parameters(parameters, endpoint):
        """
        function for adding all parameters to a specified endpoint
        previously was included in each get function but remove to clean code
        takes in a parameters dictionary and an endpoint string 
        returns an endpoit string that has been formatted with the provided parameters
        """

        if "fields" in parameters:
            formatted_fields = format_fields(parameters["fields"])
            endpoint = endpoint + "?fields=" + formatted_fields

        if "filters" in parameters:
            formatted_filters = format_filters(parameters["filters"])
            endpoint = endpoint + "?filter=" + formatted_filters

        if "pagination" in parameters:
            formatted_pagination = format_pagination(parameters["pagination"])
            endpoint = endpoint + "?"+formatted_pagination

        if "sorting" in parameters:
            formatted_sorting = format_sorting(parameters["sorting"])
            endpoint = endpoint + "?sort=" + formatted_sorting

        if "format" in parameters:
            formatted_output = format_output(parameters["format"])
            endpoint = endpoint + "?format=" + formatted_output

        return endpoint


def get_debt_to_penny(parameters):
        endpoint = "v2/accounting/od/debt_to_penny"
        formatted_endpoint = add_parameters(parameters, endpoint)
        base_url = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service/"
        
        response = requests.get(base_url + formatted_endpoint)
        return checkResponse(response)
    

def get_daily_treasury_statement(parameters):
        """
        function for accessing the daily treasury statement dataset
        """
        endpoint = "v1/accounting/dts/dts_table_1"
        formatted_endpoint = add_parameters(parameters, endpoint)
        base_url = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service/"

        response = requests.get(base_url + formatted_endpoint)
        return checkResponse(response)
    

    
def get_120_day_delinquent_debt_referral_compliance_report(parameters):
        """
        function for accessing the 120_day_delinquent_debt_referral_compliance_report dataset
        """
        endpoint = "v2/debt/tror/data_act_compliance"
        formatted_endpoint = add_parameters(parameters, endpoint)
        base_url = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service/"

        response = requests.get(base_url + formatted_endpoint)
        return checkResponse(response)
    

    
def get_gold_reserve(parameters):
        """
        function for accessing the get_us_treasury_owned_gold dataset
        """
        endpoint = "v2/accounting/od/gold_reserve"
        formatted_endpoint = add_parameters(parameters, endpoint)
        base_url = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service/"


        response = requests.get(base_url + formatted_endpoint)
        return checkResponse(response)
    

def get_record_setting_auction(parameters):
        """
        function for accessing the get recordSetting_treasury_securities_auction_data 
        """
        endpoint = "v2/accounting/od/record_setting_auction"
        formatted_endpoint = add_parameters(parameters, endpoint)
        base_url = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service/"


        response = requests.get(base_url + formatted_endpoint)
        return checkResponse(response)
    

def get_slgs_securities(parameters):
        """
        function for accessing the get recordSetting_treasury_securities_auction_data 
        """
        endpoint = "v1/accounting/od/slgs_securities"
        formatted_endpoint = add_parameters(parameters, endpoint)
        base_url = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service/"

        response = requests.get(base_url + formatted_endpoint)
        return checkResponse(response)


    
def get_tror(parameters):
        """
        function for accessing the get Treasury Report on Receivables (TROR)
        """
        endpoint = "v2/debt/tror"
        formatted_endpoint = add_parameters(parameters, endpoint)
        base_url = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service/"


        print(base_url+formatted_endpoint)
        response = requests.get(base_url + formatted_endpoint)
        return checkResponse(response)


def get_schedules_fed_debt_daily_activity(parameters):
        """
        function for accessing the get Schedules of Federal Debt by Day Activity
        this table is for daily activity
        """
        endpoint = "/v1/accounting/od/schedules_fed_debt_daily_activity"
        formatted_endpoint = add_parameters(parameters, endpoint)
        base_url = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service/"

        response = requests.get(base_url + formatted_endpoint)
        return checkResponse(response)

def get_schedules_fed_debt_daily_summary(parameters):
        """
        function for accessing the get Schedules of Federal Debt by Day Summary
        this table is for daily summary
        """
        endpoint = "/v1/accounting/od/schedules_fed_debt_daily_summary"
        formatted_endpoint = add_parameters(parameters, endpoint)
        base_url = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service/"

        response = requests.get(base_url + formatted_endpoint)
        return checkResponse(response)

