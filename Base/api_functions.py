from playwright.sync_api import  expect
from Base.common_functions import CommonFunctions
from Base.global_functions import GlobalFunctions
import json
import logging

logging.basicConfig(
     level=logging.INFO,
     format="%(asctime)s - %(levelname)s - %(message)s",
     handlers=[logging.StreamHandler()]
 )

delay = 0
with open('Data/data_local.json', 'r') as file:
    data = json.load(file)

class ApiFunctions:
     
    def __init__(self, page):
        self.page = page

        self.cf = CommonFunctions(self.page)
        
    def get_token(self, base_url, username, password, delay=0.5):
        cookies = self.page.context.cookies()
        base_url = base_url

        session_cookie = next((cookie for cookie in cookies if cookie['name'] == 'csrftoken'), None)
        sessionid = f"sessionid={session_cookie}"
        headers = {"Content-Type": "application/json",
                   "Cookie": sessionid}
        
        body = {
            "username": username, 
            "password": password
        }

        api_request_context = self.page.context.request

        response = api_request_context.post(base_url + 'api/token/',
                                            headers = headers,
                                            data = body,
                                            )
        
        assert response.ok
        return response.json()
    
    def import_order(self):
        #self.cf.select_tenant(data["child_tenant"])
        #self.page.wait_for_load_state()

        token = self.get_token(data["base_url"], data["user_name"], data["password"])
        #logging.info(f"THE TOKEN IS {token}")
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Token ' + token['token'],
            'Tenant': data['tenant_code'],
        }
        logging.info(f"THE HEADERS IS {headers}")
        
        with open('Data/order_import_single_sku.json', 'r') as file:
            body = json.load(file)
            logging.info(f"THE BODY IS {body}")

        base_url = data["base_url"]
        logging.info(f"THE BASE URL IS {base_url}")
        api_request_context = self.page.context.request

        response = api_request_context.post(base_url + 'api/v1/order/import',
                                           headers = headers,
                                           data = body,
                                            )
        
        logging.info(f"THE RESPONSE IS {response}")
        if response.ok:
            order_number = response.json()["order_number"]
        else:
            order_number = None
            logging.info(f"response is order Not created {response}")

        return order_number


    def get_order_extended(self, order_number):
        token = self.get_token(data["base_url"], data["user_name"], data["password"])
        params = {
            'extended': '1'
        }
        headers = {
            'Content-Type': 'text/plain',
            'Authorization': 'Token ' + token['token'],
            'Tenant': data['tenant_code'],
        }

        status = "New"
        validation = 0
        api_request_context = self.page.context.request
        
        
        response = api_request_context.get(data["base_url"] + 'api/v1/order/get/' + order_number,
                                            headers = headers,
                                            params=params
                                         )
            
        if response.ok:
            status = response.json()["status"]
            logging.info(f"RESPONSE DEL API REQUEST a api/v1/order/get/{order_number} es ::: {status}")
        elif validation == 1000:
            status = "FAILED"
                 
        results = response.json()["status"]
        return results