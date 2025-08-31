from Base.global_functions import GlobalFunctions
from Base.common_functions import CommonFunctions
from Base.api_functions import ApiFunctions
from Base.database_functions import DataBaseFunctions


class BaseCarriersPage:
    def __init__(self, page):
        self.page = page
        self.gf = GlobalFunctions(self.page)
        self.cf = CommonFunctions(self.page)
        self.af = ApiFunctions(self.page)
        self.dbf = DataBaseFunctions()

        self.element_carrier_table = self.page.locator("#DataTables_Table_0")
        self.element_button_new_carrier = self.page.locator("#add-carrier")
        self.element_select_carrier = self.page.locator("//select[@name='carrier']")
        self.element_input_carrier_name = self.page.locator("//input[@name='name']")
        self.element_select_status = self.page.locator('//*[@id="carrierModal"]/div/div/div[2]/form/div[3]/select')
        self.element_button_save = self.page.locator("//button[@name='save']")

         
class CarriersPage(BaseCarriersPage):
    def __init__(self, page):
        super().__init__(page)
        
    def click_new_carrier_button(self):
        self.gf.clickButton(self.element_button_new_carrier)

     
class CarriersDetails(BaseCarriersPage):
    def __init__(self, page):
        super().__init__(page)

    
    def select_carrier(self, carrier):
        self.gf.selectValue_v2(self.element_select_carrier, carrier)

    def input_carrier_name(self, carrier_code):
        self.gf.writeText_v2(self.element_input_carrier_name, carrier_code)

    def select_carrier_status(self, status):
        self.gf.selectValue_v2(self.element_select_status, status)
        
    def click_button_save(self):
        self.gf.clickButton(self.element_button_save)
        