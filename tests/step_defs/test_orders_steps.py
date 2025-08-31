import re
from playwright.sync_api import expect
from pytest_bdd import scenarios, parsers, given, when, then
from Base.global_functions import GlobalFunctions
from Base.common_functions import CommonFunctions
from Base.api_functions import ApiFunctions
from Base.celery_task_runner import run_celery_task
from Pages.order_page import CreateOrderPage, ViewOrderPage
import logging

logging.basicConfig(
     level=logging.INFO,
     format="%(asctime)s - %(levelname)s - %(message)s",
     handlers=[logging.StreamHandler()]
 )

scenarios('../features/orders.feature')


@when('navigates to create an order')
def step_when(set_up, data_load):
     page=set_up
     data=data_load

     gf = GlobalFunctions(page)
     cf = CommonFunctions(page)

     cf.select_tenant(data["child_tenant"])
     gf.secuential_navigation(cf.menu_orders, cf.menu_create_order)
     


@then('selects a Source Code')
def step_then(set_up, data_load) :
     page = set_up
     data = data_load

     cop = CreateOrderPage(page)
     cop.search_source(data["source_code"])


@then('searches for the item')
def step_then(set_up, data_load):
     page = set_up
     data = data_load

     cop = CreateOrderPage(page)
     cop.search_item(data["item"]) 

@then('searches for the sku')
def step_then(set_up, data_load):
     page = set_up
     data = data_load

     cop = CreateOrderPage(page)
     cop.select_sku(data["skus"][0])


@then('selects the quantity of the item')
def step_then(set_up, data_load):
     page = set_up
     data = data_load

     cop = CreateOrderPage(page) 
     cop.input_sku_quantity(data["quantity_to_order"])


@then('adds the items to the order')
def step_then(set_up, data_load):
     page = set_up
     data = data_load

     cop = CreateOrderPage(page) 
     cop.add_items_to_cart()


@then('selects a shipping method')
def step_then(set_up, data_load):
     page = set_up
     data = data_load

     cop = CreateOrderPage(page) 
     cop.select_shipping_method(data["ship_code_description"][0])


@then('selects a customer')
def step_then(set_up, data_load):
     page = set_up
     data = data_load

     cop = CreateOrderPage(page) 
     cop.select_customer()


@then('selects a ship to address same as customer')
def step_then(set_up, data_load):
     page = set_up
     data = data_load

     cop = CreateOrderPage(page) 
     cop.select_ship_to_address()


@then('adds the payment details same as customer')
def step_then(set_up, data_load):
     page = set_up
     data = data_load

     cop = CreateOrderPage(page) 
     cop.add_payment()
     

@then('clicks on Create Order button')
def step_when(set_up, data_load):
     page = set_up
     data = data_load

     cop = CreateOrderPage(page) 
     cop.click_create_order_button()


 
@then(parsers.parse('adds {lines} items'))
def step_then(set_up, data_load, lines):
     page = set_up
     data = data_load
     skus = int(lines.strip('"'))

     cop = CreateOrderPage(page) 
     for item in range(skus):
          cop.search_item(data["item"]) 
          cop.select_sku(data["skus"][item])
          cop.input_sku_quantity(data["quantity_to_order"])
          cop.add_items_to_cart()


@then(parsers.parse('navigates to the url {string}'))
def step_then(set_up, data_load, string) :
     data = data_load

     gf = GlobalFunctions(page=set_up)
     cf = CommonFunctions(page=set_up)

     cf.select_tenant(data["child_tenant"])
    
     url = f'{data["base_url"]}{string.replace('"', '')}'
     #print(url)
     gf.goToUrl(url)


@then('views the order inquiry screen')
def step_then(set_up, data_load, order ) :
     page = set_up
     data = data_load

     gf = GlobalFunctions(page)
     cf = CommonFunctions(page)

     cf.select_tenant(data["child_tenant"])

     url = f'{data["base_url"] + 'order/view/' + order }'
     #print(url)
     gf.goToUrl(url)


@then(parsers.parse('cancels {qty} item'))
def step_then(set_up, data_load, qty) :
     data = data_load
     page = set_up

     eop = ViewOrderPage(page)

     eop.input_cancel_units("1")
     


@then('selects a cancel Reason')
def step_then(set_up, data_load):
     data = data_load
     page = set_up

     eop = ViewOrderPage(page)
     
     #eop.select_cancel_reason("Customer Request")

@then('clicks on cancel units button')
def step_then(set_up):
     page = set_up

     eop = ViewOrderPage(page)
     
     #eop.click_button_submit_cancel_units()

     #page.get_by_role("listitem").filter()
     page.locator("div").filter(has_text=re.compile(r"^1Canceled$")).get_by_role("heading").click()
     page.get_by_label("Processed Cancellations").get_by_role("cell", name="1", exact=True).click()
     page.get_by_label("Processed Cancellations").get_by_text("Close").click()



@then(parsers.parse('if the order status is "{string}", the user triggers the celey task'))
def execute_celery_task(set_up, data_load,order, string):
    data = data_load
    tenant = data['tenant_code']
    status = string

    if status == "Created" or status =="New":
     logging.info(f"voy a allocate")
     task_name = "allocate"   
     task_args = [tenant, order]   
     run_celery_task(task_name, task_args)
    elif status == "Allocated":
     task_name = "pickgen"   
     task_args = [tenant, order, "--noqueue"]   
     run_celery_task(task_name, task_args)


@then(parsers.parse('navigates to the url {string}'))
def step_then(set_up, data_load, string) :
     data = data_load

     gf = GlobalFunctions(page=set_up)
     cf = CommonFunctions(page=set_up)

     cf.select_tenant(data["child_tenant"])
    
     url = f'{data["base_url"]}{string.replace('"', '')}'
     #print(url)
     gf.goToUrl(url)     
     