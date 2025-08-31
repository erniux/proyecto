from Base.global_functions import GlobalFunctions
from Base.common_functions import CommonFunctions
from Base.api_functions import ApiFunctions
from Base.database_functions import DataBaseFunctions


class BaseCancelReasonsPage:
    def __init__(self, page):
        self.page = page
        self.gf = GlobalFunctions(self.page)
        self.cf = CommonFunctions(self.page)
        self.af = ApiFunctions(self.page)
        self.dbf = DataBaseFunctions()

        self.element_button_new_cancel_reason = self.page.locator("#new-reason")
        self.element_input_cancel_reason_code = self.page.locator("#reason_code")
        self.element_input_cancel_reason_description = self.page.locator("#description")
        self.element_warehouse_service_failure = self.page.locator("#service_failure")
        
        self.element_button_save = self.page.locator("#modal-reasons-save")


class CancelReasonsPage(BaseCancelReasonsPage):
    def __init__(self, page):
        super().__init__(page)
        
    def click_new_button(self):
        self.gf.clickButton(self.element_button_new_cancel_reason)

     
class CancelReasonsDetails(BaseCancelReasonsPage):
    def __init__(self, page):
        super().__init__(page)

    
    def input_cancel_reason_code(self, cancel_reason_code):
        self.gf.writeText_v2(self.element_input_cancel_reason_code, cancel_reason_code)

    def input_cancel_reason_description(self, cancel_reason_description):
        self.gf.writeText_v2(self.element_input_cancel_reason_description, cancel_reason_description)
 
    def input_warehouse_service_failure(self, indicates_failure):
        self.gf.checkBox(self.element_warehouse_service_failure, indicates_failure)
        
    def click_button_save(self):
        self.gf.clickButton(self.element_button_save)
        
