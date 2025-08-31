from Base.global_functions import GlobalFunctions
from Base.common_functions import CommonFunctions
from Base.api_functions import ApiFunctions
from Base.database_functions import DataBaseFunctions


class BaseDispositionCodesPage:
    def __init__(self, page):
        self.page = page
        self.gf = GlobalFunctions(self.page)
        self.cf = CommonFunctions(self.page)
        self.af = ApiFunctions(self.page)
        self.dbf = DataBaseFunctions()

        self.element_button_new_disposition_code = self.page.locator("#add-row-button")
        self.element_input_disposition_code = self.page.locator("//input[contains(@name,'disposition_code')]")
        self.element_input_disposition_description = self.page.locator("//input[contains(@name,'description')]")
        self.element_select_add_to_inventory = self.page.locator("//select[contains(@name,'add_to_inventory')]")
        self.element_select_refund_eligible = self.page.locator("//select[contains(@name,'refund_eligible')]")
        self.element_select_use_business_type = self.page.locator("//select[contains(@name,'use_business_type')]")
        self.element_select_business_type = self.page.locator("//select[contains(@name,'business_type_code')]")
        
        self.element_button_save = self.page.locator("#modal-add-save-btn")


class DispositionCodesPage(BaseDispositionCodesPage):
    def __init__(self, page):
        super().__init__(page)
        
    def click_new_button(self):
        self.gf.clickButton(self.element_button_new_disposition_code)

     
class DispositionCodesDetails(BaseDispositionCodesPage):
    def __init__(self, page):
        super().__init__(page)

    
    def input_disposition_code(self, disposition_code):
        self.gf.writeText_v2(self.element_input_disposition_code, disposition_code)

    def input_disposition_description(self, disposition_description):
        self.gf.writeText_v2(self.element_input_disposition_description, disposition_description)
 
    def click_button_save(self):
        self.gf.clickButton(self.element_button_save)
        
