from Base.global_functions import GlobalFunctions
from Base.common_functions import CommonFunctions
from Base.api_functions import ApiFunctions
from Base.database_functions import DataBaseFunctions


class BaseBusinessTypePage:
    def __init__(self, page):

        self.page = page
        self.gf = GlobalFunctions(self.page)
        self.cf = CommonFunctions(self.page)
        self.af = ApiFunctions(self.page)
        self.dbf = DataBaseFunctions()

        self.element_business_type_table = self.page.locator("#business-types-table")
        self.element_button_new_business_type = self.page.locator("#new-business-type")
        self.element_input_business_type_code = self.page.locator("#business_type_code")
        self.element_input_business_type_code_desc = self.page.locator("#description")
        self.element_select_maitain_inventory = self.page.locator("#maintain_inventory")
        self.element_select_billing_type = self.page.locator("#billing_type")
        self.element_input_inventory_priority = self.page.locator("#inventory_priority")
        self.element_button_business_type_save = self.page.locator("#save-business-type")


class BusinessTypePage(BaseBusinessTypePage):
    def __init__(self, page):
        super().__init__(page)
        
    def click_new_business_type_button(self):
        self.gf.clickButton(self.element_button_new_business_type)
    

class BusinessTypeDetails(BaseBusinessTypePage):
    def __init__(self, page):
        super().__init__(page)

    def input_business_type_code(self, business_type_code):
        self.gf.writeText_v2(self.element_input_business_type_code, business_type_code) 

    def input_business_type_description(self, business_type_description):
        self.gf.writeText_v2(self.element_input_business_type_code_desc, business_type_description)

    def select_maitain_inventory(self, maintain_inventory):
        self.gf.selectValue(self.element_select_maitain_inventory, maintain_inventory)

    def select_billing_type(self, billing_type):
        self.gf.selectValue_v2(self.element_select_billing_type, billing_type)

    def input_inventory_priority(self, inventory_priority):
        self.gf.writeText_v2(self.element_input_inventory_priority, inventory_priority)

    def button_save(self):
        self.gf.clickButton(self.element_button_business_type_save)

