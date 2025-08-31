from Base.global_functions import GlobalFunctions
from Base.common_functions import CommonFunctions
from Base.api_functions import ApiFunctions
from Base.database_functions import DataBaseFunctions
import logging
import time

logging.basicConfig(
     level=logging.INFO,
     format="%(asctime)s - %(levelname)s - %(message)s",
     handlers=[logging.StreamHandler()]
 )

class BaseUserPage:
    def __init__(self, page):
        self.page = page
        self.gf = GlobalFunctions(self.page)
        self.cf = CommonFunctions(self.page)
        self.af = ApiFunctions(self.page)
        self.dbf = DataBaseFunctions()


        self.element_link_edit_user = self.page.locator("#datatables-grid > tbody > tr > th > a")
        self.element_input_first_name = self.page.locator("//input[@name='first_name']")
        self.element_input_last_name = self.page.locator("//input[@name='last_name']")

        self.element_user_facilities = self.page.locator("//span[contains(@class,'select2-selection select2-selection--multiple')]")
        self.element_input_facility_search = self.page.locator("input[type=\"search\"]")
        self.element_select_time_zone = self.page.locator( "#select2-timezone-container")
        self.element_button_save_user = self.page.locator("#edit-user")


class BaseGroupPage:
    def __init__(self, page):
        self.page = page
        self.gf = GlobalFunctions(self.page)
        self.cf = CommonFunctions(self.page)
        self.af = ApiFunctions(self.page)
        self.dbf = DataBaseFunctions()
         
        self.element_button_new_group = self.page.locator("#add-row-button")
        self.element_input_group_name = self.page.locator("//input[@placeholder='Group Name']")

        self.element_select_group_tenant = self.page.locator(".select2-selection").nth(0)
        self.element_select_group_tenant_search = self.page.locator(".select2-search__field").nth(1)
        self.element_select_group_tenant_results = self.page.locator('.select2-results__option').nth(1)

        self.element_select_group_permissions = self.page.locator(".select2-selection").nth(1)
        self.element_select_group_permissions_search = self.page.locator(".select2-search__field").nth(0)
        self.element_select_group_permissions_results = self.page.locator(".select2-results__option").nth(0)

        self.element_button_group_permissions_save = self.page.locator("#modal-add-save-btn")

class BaseAdminGroupPage:
    def __init__(self, page):
        self.page = page
        self.gf = GlobalFunctions(self.page)
        self.cf = CommonFunctions(self.page)
        self.af = ApiFunctions(self.page)
        self.dbf = DataBaseFunctions()

        self.element_button_admin_group_new = self.page.locator("//a[contains(.,'Add group')]")
        self.element_input_admin_group_name = self.page.locator('//*[@id="id_name"]')  # //*[@id="id_name"]
        self.element_input_admin_permission_name = self.page.locator("#id_permissions_input")
        self.element_select_admin_permission_list = self.page.locator( "#id_permissions_from")
        self.element_link_permissions_add = self.page.locator("#id_permissions_add_link")
        self.element_link_permissions_remove = self.page.locator("#id_permissions_remove_link")
        self.element_button_save_admin_group = self.page.locator(".default")
        self.element_button_save_and_another_admin_group = self.page.locator(".submit-row > input:nth-child(2)")


class UserPage(BaseUserPage):
    def __init__(self, page):
        super().__init__(page)
        

    def click_edit_user_link(self):
        self.gf.clickLink(self.element_link_edit_user)


class GroupPage(BaseGroupPage):
    def __init__(self, page):
        super().__init__(page)

    
    def click_new_group(self,):
        self.gf.clickButton(self.element_button_new_group)
        

class AdminGroupPage(BaseAdminGroupPage):
    def __init__(self, page):
        super().__init__(page)

    
    def click_admin_group_new_group(self,):
        self.gf.clickButton(self.element_button_admin_group_new)


class AdminGroupDetailPage(BaseAdminGroupPage):
    def __init__(self, page):
        super().__init__(page)


    def input_group_name_and_permissions(self, group_name):
        not_found = []
        
        for group, permission in group_name.items():
            
            self.gf.writeText_v2(self.element_input_admin_group_name, group)
            for p in permission:
                #time.sleep(0.25)
                #logging.info(f'permission=> {p}')
                self.gf.writeText_v2(self.element_input_admin_permission_name, p)
                self.page.keyboard.press("Enter")
                not_found.append(self.gf.selectValue_v2(self.element_select_admin_permission_list, p))
                self.gf.clickButton(self.element_link_permissions_add)
            time.sleep(1)    
            self.gf.clickButton(self.element_button_save_admin_group) # .element_button_save_and_another_admin_group)
            #self.page.pause()
             

        if len(not_found) > 0:        
            logging.info(f"NOT FOUND ===> {not_found}")


    def click_save_admin_group_button(self):
        self.gf.clickButton(self.element_button_save_admin_group)

class UserDetails(BaseUserPage):
    def __init__(self, page):
        super().__init__(page)

    def input_user_first_name(self, first_name):
        self.gf.writeText_v2(self.element_input_first_name, first_name)


    def input_user_last_name(self, last_name):
        self.gf.writeText_v2(self.element_input_last_name, last_name)


    def input_facility_to_user(self, facility_code):
        result = self.gf.validateText(self.element_user_facilities, facility_code)
        if result == False:
            self.gf.multiSelectValue(self.element_input_facility_search, facility_code, facility_code)

    
    def select_time_zone(self, time_zone):
        self.page.keyboard.press("Tab")
        self.page.keyboard.press("Tab")
        self.page.keyboard.press("Enter")
        self.page.keyboard.insert_text(time_zone)        
        self.page.keyboard.press("Enter")


    def click_button_save(self):
        self.gf.clickButton(self.element_button_save_user)

     
class GroupDetailPage(BaseGroupPage):
    def __init__(self, page):
        super().__init__(page)

    def select_group_tenant(self, tenant, tenant_code):
        #self.page.pause()
        self.gf.select2Value_2(self.element_select_group_tenant, self.element_select_group_tenant_search,
                             self.element_select_group_tenant_results, tenant, tenant_code ) 


    def input_group_name_and_permissions(self, group_name):
        #logging.info(f'group name desde el user_page ::: {(group_name)}' )
        for group, permission in group_name.items():
            #logging.info(f'group::: {group} permission ::: {permission} ') 
            self.gf.writeText_v2(self.element_input_group_name, group)
            for p in permission:
                logging.info(f'permission=> {p}')
                self.gf.select2Value_2(self.element_select_group_permissions, self.element_select_group_permissions_search, 
                                       self.element_select_group_permissions_results, p, p)


    def click_button_save(self):
        self.gf.clickButton(self.element_button_group_permissions_save)            
        

    


 

        















         
 