from json import load
from pytest_bdd import scenarios, parsers, given, when, then
from Base.global_functions import GlobalFunctions
from playwright.sync_api import expect
from Pages.tenant_page import TenantPage

scenarios('../features/tenant.feature')
delay = 0


@then('prints all elements on page')
def step_then(set_up,data_load) :
    page=set_up
    data=data_load
    tp = TenantPage(page, data)
    elements = tp.total_elements()
    print(elements)

@then('clicks on New Button')
def step_then(set_up, data_load):
    tp = TenantPage(page=set_up, data=data_load)
    tp.click_new_tenant_button()

@then('enters the tenant details')
def step_then(set_up, data_load):
    tp =TenantPage(page=set_up, data=data_load)
    pass

@then('enters the time zone')
def step_then(set_up, data_load):
    tp =TenantPage(page=set_up, data=data_load)
    pass

@then('enters the contact details')
def step_then(set_up, data_load):
    tp =TenantPage(page=set_up, data=data_load)
    pass

@then('enters the messaging details')
def step_then(set_up, data_load):
    tp =TenantPage(page=set_up, data=data_load)
    pass

@then('enters the emails domains')
def step_then(set_up, data_load):
    tp =TenantPage(page=set_up, data=data_load)
    pass

@then('enters the general settings')
def step_then(set_up, data_load):
    tp =TenantPage(page=set_up, data=data_load)
    pass

@then('enters the carrier notifications')
def step_then(set_up, data_load):
    tp =TenantPage(page=set_up, data=data_load)
    pass

@then('enters the integration settings')
def step_then(set_up, data_load):
    tp =TenantPage(page=set_up, data=data_load)
    pass

@then('enters the payment settings')
def step_then(set_up, data_load):
    tp =TenantPage(page=set_up, data=data_load)
    pass

@then('enters the warehouse settings')
def step_then(set_up, data_load):
    tp =TenantPage(page=set_up, data=data_load)
    pass

@then('enterrs the virtual shipment settings')
def step_then(set_up, data_load):
    tp =TenantPage(page=set_up, data=data_load)
    pass

@then('enters the sftp settings')
def step_then(set_up, data_load):
    tp =TenantPage(page=set_up, data=data_load)
    pass

@then('selects the facilities')
def step_then(set_up, data_load):
    tp =TenantPage(page=set_up, data=data_load)
    pass

@then('selects Facility for returns')
def step_then(set_up, data_load):
    tp =TenantPage(page=set_up, data=data_load)
    pass

@then('clicks on Save Changes button')
def step_then(set_up, data_load):
    tp =TenantPage(page=set_up, data=data_load)
    pass
