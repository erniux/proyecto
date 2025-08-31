from playwright.sync_api import expect
from pytest_bdd import given, scenarios, then, when
from pytest_bdd import parsers

from Pages.wave_page import WavePage, NewWavePage


scenarios('../features/label_packing.feature')


@when(parsers.cfparse('the user selects {orders:d} order for label packing wave'))
def search_available_orders(set_up, data_load, orders):
    page = set_up
    data = data_load
    wp = WavePage(page)
    nwp = NewWavePage(page)

    tenant = data["tenant_code"]
    sql = f"SELECT order_number FROM order_order WHERE tenant_id in (SELECT id FROM system_tenant where tenant = '{tenant}') limit {orders};"
     
    orders = wp.dbf.db_connection(sql)

    for elemento in orders:
        print(elemento[0])

    wp.cf.select_tenant(data["child_tenant"])
    wp.gf.secuential_navigation(wp.cf.menu_wms, wp.cf.menu_warehouse, wp.cf.menu_waves)
    wp.create_new_wave()
    #page.pause()
    #nwp.select_facility(data["facility_name"])


    



@when('a replenishment task has been created')
def _():
    """a replenishment task has been created."""
    raise NotImplementedError


@then('The user set a Sku country of origin')
def _():
    """The user set a Sku country of origin."""
    raise NotImplementedError


@then('The user work the replenishment task')
def _():
    """The user work the replenishment task."""
    raise NotImplementedError


@then('the sku most have country of origin')
def _():
    """the sku most have country of origin."""
    raise NotImplementedError


@then('the sku most have inner carton code')
def _():
    """the sku most have inner carton code."""
    raise NotImplementedError


@then('the sku most have weight > 0')
def _():
    """the sku most have weight > 0."""
    raise NotImplementedError



