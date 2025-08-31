import pytest
import json
from playwright.sync_api import Playwright
from Base.common_functions import CommonFunctions
from Base.global_functions import GlobalFunctions
from Base.api_functions import ApiFunctions
from pytest_bdd import parsers, given, when, then

#hooks
@given('the User has a session open on Jazz')
def session_user(set_up):
    if set_up is None:
        raise Exception("La sesión no se ha abierto correctamente")


@given('the order is created with a payload', target_fixture="order")
def order(set_up, scope="function"):
    
    af = ApiFunctions(page=set_up)
    order = af.import_order()
    return order


@when('validates the order status', target_fixture="status")
@then('validates the order status', target_fixture="status")
def status(set_up, order, scope="function"):

    af = ApiFunctions(page=set_up)
    status = af.get_order_extended(order)
    print(status)
    return order, status


#Fixtures
@pytest.fixture(scope="session")
def data_load():
    with open('Data/data_local.json', 'r') as file:
        data = json.load(file)
    return data


@pytest.fixture(scope="session")
def set_up(playwright: Playwright, data_load):
    data = data_load
    browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
    context = browser.new_context(
        extra_http_headers={"X-BLUEWASH-ENABLED": "true"},
        no_viewport=True
    )
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    
    commonFunctions = CommonFunctions(page)
    
    
    page.goto(data["base_url"])
    commonFunctions.login(data['user_name'], data['password'])
    page.wait_for_load_state()


    context.tracing.stop(path="trace.zip")

    yield page

    context.close()
    browser.close()
