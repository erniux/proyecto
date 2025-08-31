from Base.global_functions import GlobalFunctions
from Base.common_functions import CommonFunctions
from Base.api_functions import ApiFunctions
from Base.database_functions import DataBaseFunctions


class BaseHoldReasonPage:
    def __init__(self, page):
        self.page = page
        self.gf = GlobalFunctions(self.page)
        self.cf = CommonFunctions(self.page)
        self.af = ApiFunctions(self.page)
        self.dbf = DataBaseFunctions()

        self.element_table_hold_reasons = self.page.locator("#hold-reasons")
        self.element_button_new_hold = self.page.locator("#new-reason")
        self.element_input_hold_reason_code = self.page.get_by_role("textbox", name="Code")
        self.element_input_hold_description = self.page.get_by_role("textbox", name="Description")
        self.element_button_save = self.page.locator("#modal-hold-reason-save-btn")


class HoldReasonPage(BaseHoldReasonPage):
    def __init__(self, page):
        super().__init__(page)
        
    def click_new_hold_button(self):
        self.gf.clickButton(self.element_button_new_hold)

     
class HoldReasonDetails(BaseHoldReasonPage):
    def __init__(self, page):
        super().__init__(page)

    
    def input_hold_reason_code(self, hold_reason_code):
        self.element_input_hold_reason_code.click()
        self.element_input_hold_reason_code.fill(hold_reason_code)
    

    def input_hold_reason_description(self, hold_reason_description):
        self.element_input_hold_description.click()
        self.element_input_hold_description.fill(hold_reason_description)

        
    def click_button_save(self):
        self.gf.clickButton(self.element_button_save)
        

     
     
