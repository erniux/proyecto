from Base.global_functions import GlobalFunctions
from Base.common_functions import CommonFunctions
from Base.api_functions import ApiFunctions
from Base.database_functions import DataBaseFunctions


class BaseOverrideReasonsPage:
    def __init__(self, page):
        self.page = page
        self.gf = GlobalFunctions(self.page)
        self.cf = CommonFunctions(self.page)
        self.af = ApiFunctions(self.page)
        self.dbf = DataBaseFunctions()

        self.element_button_new_override = self.page.locator("#add-row-button")
        self.element_input_override_reason = self.page.locator("//input[@name='override_reason_code']")
        self.element_input_override_description = self.page.locator("//input[contains(@name,'description')]")
        self.element_button_save = self.page.locator("#modal-add-save-btn")


class OverrideReasonsPage(BaseOverrideReasonsPage):
    def __init__(self, page):
        super().__init__(page)
        
    def click_new_override_button(self):
        self.gf.clickButton(self.element_button_new_override)

     
class OverrideReasonsDetails(BaseOverrideReasonsPage):
    def __init__(self, page):
        super().__init__(page)

    
    def input_override_type_code(self, override_type_code):
        self.gf.writeText_v2(self.element_input_override_reason, override_type_code)

    def input_override_description(self, override_description):
        self.gf.writeText_v2(self.element_input_override_description, override_description)

    def click_button_save(self):
        self.gf.clickButton(self.element_button_save)
        

     
     
