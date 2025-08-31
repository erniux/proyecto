import re
import logging
from playwright.sync_api import expect
from pytest_bdd import scenarios, parsers, given, when, then
from Base.global_functions import GlobalFunctions
from Base.common_functions import CommonFunctions
from Base.api_functions import ApiFunctions
from Pages.user_page import GroupPage, GroupDetailPage, AdminGroupPage, AdminGroupDetailPage
 
logging.basicConfig(
     level=logging.INFO,
     format="%(asctime)s - %(levelname)s - %(message)s",
     handlers=[logging.StreamHandler()]
 )


scenarios('../features/users.feature')


   # When navigates to Groups
   # Then clicks on New button
   # Then enters the Group Name
   # Then selects a tenant
   # Then enters a set of group names
   # Then clicks on Save Changes button

@when('navigates to Groups')
def step_when(set_up, data_load):
     page=set_up
     data=data_load

     gf = GlobalFunctions(page)
     cf = CommonFunctions(page)

     #cf.select_tenant(data["parent_tenant"])
     gf.secuential_navigation(cf.menu_system, cf.menu_users_groups)
     gf.selectSubMenu(cf.menu_groups)
     


@then('clicks on New button')
def step_then(set_up, data_load) :
     page = set_up
     data = data_load
     gp = GroupPage(page)
     
     gp.click_new_group()
     


@then('enters the group name')
def step_then(set_up, data_load):
     page = set_up
     data = data_load

     gpd = GroupDetailPage(page)
     #logging.info(f'group name desde el test_users_steps ::: {data["group_name"]}' )
     gpd.select_group_tenant(data["parent_tenant"], data["parent_tenant_code"])
     gpd.input_group_name_and_permissions(data["group_name"])
     #gpd.click_button_save()


@then('navigates to Django admin')
def step_then(set_up, data_load):
     page=set_up
     data = data_load
     gf = GlobalFunctions(page)

     gf.goToUrl(f"{data['base_url']}snowfalltech")


@then('navigates to Admin-Groups')
def step_then(set_up, data_load):
     page=set_up
     data = data_load
     gf = GlobalFunctions(page)
     cm = CommonFunctions(page)

     gf.secuential_navigation(cm.menu_admin_groups)



@then('clicks on Add button')
def step_then(set_up, data_load):
     page=set_up
     data = data_load

     ag = AdminGroupPage(page) 

     ag.click_admin_group_new_group()


@then('congifures the Group Permission')
def step_then(set_up, data_load):
     page=set_up
     data = data_load
     
     agd = AdminGroupDetailPage(page)

     agd.input_group_name_and_permissions(data["group_name"])



@then('clicks on Save Group Permission button')
def step_then(set_up, data_load):
     page=set_up
     data = data_load
     gf=GlobalFunctions(page)
     agd = AdminGroupDetailPage(page)

     agd.click_save_admin_group_button()



