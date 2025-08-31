import time
import logging
from playwright.sync_api import expect
from pytest_bdd import scenarios, parsers, given, when, then
from Base.global_functions import GlobalFunctions
from Base.common_functions import CommonFunctions
from Base.api_functions import ApiFunctions
from Pages.inventory_adjustments_page import AdjustmentPage
 
logging.basicConfig(
     level=logging.INFO,
     format="%(asctime)s - %(levelname)s - %(message)s",
     handlers=[logging.StreamHandler()]
 )


scenarios('../features/inventory.feature')



@then('navigates to create an adjustment')
def step_then(set_up, data_load):
    page=set_up
    data=data_load
    gf = GlobalFunctions(page)
    cf = CommonFunctions(page)

    cf.select_tenant(data["child_tenant"])
    gf.secuential_navigation(cf.menu_inventory, cf.menu_adjustments)


@then('selects a facility')
def step_then(set_up, data_load):
    page=set_up
    data=data_load

    iap = AdjustmentPage(page)
    iap.select_facility(data["facility_name"]) 


@then('create an adjustment')
def step_then(set_up, data_load):
    page=set_up
    data=data_load
    iap = AdjustmentPage(page)

    skus = data["adjustment_skus"]

    iap.click_button_start_adjustment()

    for sku in skus:
        iap.search_sku(sku)
        iap.input_adjustment_quantity("1000")
        iap.select_business_type("ECOMM")
        iap.select_adjustment_reason("6 - Warehouse Receiving Exception (Invata)")
        iap.input_note("Adjustment initial inventory")
        iap.click_button_submit_adjustment()

     
    



     
     



