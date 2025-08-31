from Base.global_functions import GlobalFunctions
from Base.common_functions import CommonFunctions
from Base.api_functions import ApiFunctions
from Base.database_functions import DataBaseFunctions


class BaseExceptionResolutionReasonsPage:
    def __init__(self, page):
        self.page = page
        self.gf = GlobalFunctions(self.page)
        self.cf = CommonFunctions(self.page)
        self.af = ApiFunctions(self.page)
        self.dbf = DataBaseFunctions()

        self.element_button_new_resolution_exception_reason = self.page.locator("#new-reason")
        self.element_input_exception_resolution_reason_code = self.page.locator("#reason_code")
        self.element_input_exception_resolution_reason_description = self.page.locator("#description")
        self.element_select_status_resolution_reason = self.page.locator("#is_active")
        self.element_button_save = self.page.locator("#modal-reasons-save")


class ExceptionResolutionReasonsPage(BaseExceptionResolutionReasonsPage):
    def __init__(self, page):
        super().__init__(page)
        
    def click_new_button(self):
        self.gf.clickButton(self.element_button_new_resolution_exception_reason)

     
class ExceptionResolutionReasonsDetails(BaseExceptionResolutionReasonsPage):
    def __init__(self, page):
        super().__init__(page)

    
    def input_exception_reason_code(self, exception_resolution_reason_code):
        self.gf.writeText_v2(self.element_input_exception_resolution_reason_code, exception_resolution_reason_code)

    def input_exception_reason_description(self, exception_resolution_reason_description):
        self.gf.writeText_v2(self.element_input_exception_resolution_reason_description, exception_resolution_reason_description)
 
    def select_exception_resoulution_reason_status(self, status):
        self.gf.selectValue_v2(self.element_select_status_resolution_reason, status)
        
    def click_button_save(self):
        self.gf.clickButton(self.element_button_save)
        
