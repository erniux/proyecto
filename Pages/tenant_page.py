from Base.global_functions import GlobalFunctions
from Base.common_functions import CommonFunctions
from Base.api_functions import ApiFunctions
from Base.database_functions import DataBaseFunctions
import logging

logging.basicConfig(
     level=logging.INFO,
     format="%(asctime)s - %(levelname)s - %(message)s",
     handlers=[logging.StreamHandler()]
 )


class BaseTenantPage:
    def __init__(self, page):
        self.page = page
        self.gf = GlobalFunctions(self.page)
        self.cf = CommonFunctions(self.page)
        self.af = ApiFunctions(self.page)
        self.dbf = DataBaseFunctions()

        self.element_button_new_tenant = self.page.locator("#add-row-button")
        self.element_input_tenant_name = self.page.locator("//input[@data-field='name']")
        self.element_input_tenant_code = self.page.locator("//input[@data-field='tenant']")
        self.element_select_tenant_role = self.page.locator("//select[@data-field='tenant_role']")
        self.element_select_time_zone = self.page.locator("//select[@data-field='timezone']")
        self.element_button_tenant_save = self.page.locator("//button[contains(.,'Save Changes')]")
        self.element_toastr_save_success = "Saved Successfully!"
        self.element_link_tenant_found1 = "//a[contains(.,'"
        self.element_link_tenant_found2 = "')]"
        self.element_check_facility1 =  "//input[contains(@value,'"
        self.element_check_facility2 = "')]"
        

class TenantPage(BaseTenantPage):
    def __init__(self, page):
        super().__init__(page)
        

    def click_new_tenant_button(self):
        #self.page.pause()
        self.gf.clickButton(self.element_button_new_tenant)


    def click_link_tenant(self, tenant_code):
        element = self.page.locator(f'{self.element_link_tenant_found1}{tenant_code}{self.element_link_tenant_found2}')
        logging.info(f"element in click_link_tenant is {element}")
        self.gf.clickLink(element)
        

     
class TenantDetails(BaseTenantPage):
    def __init__(self, page):
        super().__init__(page)

    def input_tenant_code(self, tenant_code):
        self.gf.writeText_v2(self.element_input_tenant_code, tenant_code) 


    def input_tenant_name(self, tenant_name):
        self.gf.writeText_v2(self.element_input_tenant_name, tenant_name)  


    def select_tenant_role(self, tenant_role):
        self.gf.selectValue(self.element_select_tenant_role, tenant_role)


    def select_time_zone(self, time_zone):
        self.gf.selectValue(self.element_select_time_zone, time_zone)


    def check_facility_code(self, facility_code):
        logging.info(f"value of facility code is ::: {facility_code}")
        #self.page.pause()
        element = self.element_check_facility1 + facility_code + self.element_check_facility2
        element = self.page.locator(element)
        element.highlight()
        logging.info(f"and the element xpath/locator is ::: {element}")
        self.gf.checkBox(element)


    def click_button_save(self):
        self.gf.clickButton(self.element_button_tenant_save)
        
        
        

     
     
