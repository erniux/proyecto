import logging
from playwright.sync_api import expect
from pytest_bdd import scenarios, parsers, given, when, then
from Base.global_functions import GlobalFunctions
from Base.common_functions import CommonFunctions
from Base.api_functions import ApiFunctions
from Pages.wave_page import WavePage, NewWavePage
from Base.database_functions import DataBaseFunctions

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)

scenarios('../features/ocx.feature')


def _initialize_objects(set_up):
    page = set_up
    gf = GlobalFunctions(page)
    cf = CommonFunctions(page)
    wp = WavePage(page)
    nwp = NewWavePage(page)
    db = DataBaseFunctions()
    ap = ApiFunctions(page) 
    
    return page, gf, cf, wp, nwp, db, ap

 
@given('a wave is created with orders and conveyor cart')
def step_def(set_up, data_load):
    page, gf, cf, wp, nwp, db, ap = _initialize_objects(set_up)

    cf.select_tenant(data_load["child_tenant"])

    gf.secuential_navigation(cf.menu_wms, cf.menu_warehouse, cf.menu_waves)
    wp.create_new_wave()
    page.pause()
    nwp.select_facility(data_load['facility_name'])
    nwp.select_cart_type(data_load['conveyor_asyncLabel'])

    sql = "SELECT oo.order_number FROM order_order oo INNER join shipping_pick sp ON sp.order_id = oo.id WHERE oo.status = 'PRINTED' AND sp.wave_id IS NULL ORDER BY oo.id LIMIT 4;"
    rows = db.db_connection(sql)
    order_list = list(zip(*rows))[0]

    nwp.click_button_order_bulk_add()
    nwp.input_order_list(order_list)
    nwp.click_button_add_bulk_orders()
    nwp.validate_checkbox_exclude_singles_checked()
    nwp.click_button_preview_wave()
    nwp.click_button_submit_wave()


@when('the system triggers the TMS API with order details') #(weights, dims, addresses)
def step_def(set_up, data_load):
    page, gf, cf, wp, nwp, db, ap = _initialize_objects(set_up)
    pass

@then('the TMS returns labels with tracking numbers')
def step_def(set_up, data_load):
    page, gf, cf, wp, nwp, db, ap = _initialize_objects(set_up)
    pass

@then('the labels are stored in the shipping pre-shipment model with pick_ids')
def step_def(set_up, data_load):
    page, gf, cf, wp, nwp, db, ap = _initialize_objects(set_up)
    pass

@then('the labels are associated with the shipping carton determined by SKU, dims, and dimming algorithm')
def step_def(set_up, data_load):
    page, gf, cf, wp, nwp, db, ap = _initialize_objects(set_up)
    pass
