from Base.global_functions import GlobalFunctions
from Base.common_functions import CommonFunctions
from Base.api_functions import ApiFunctions
from Base.database_functions import DataBaseFunctions


class BaseAppeasementPage:
    def __init__(self, page):
        self.page = page
        self.gf = GlobalFunctions(self.page)
        self.cf = CommonFunctions(self.page)
        self.af = ApiFunctions(self.page)
        self.dbf = DataBaseFunctions()

        self.element_button_new_appeasement = self.page.locator("#add-row-button")
        self.element_input_appeasement_type_code = self.page.locator("//input[@name='appeasement_type_code']")
        self.element_input_appeasement_description = self.page.locator("//input[contains(@name,'description')]")
        self.element_select_credit_or_debit = self.page.locator("//select[contains(@name,'credit_or_debit')]")
        self.element_select_is_active = self.page.locator("//select[contains(@name,'is_active')]")
        self.element_select_is_actionable = self.page.locator("//select[contains(@name,'is_actionable')]")
        self.element_button_save = self.page.locator("#modal-add-save-btn")


class AppeasementPage(BaseAppeasementPage):
    def __init__(self, page):
        super().__init__(page)
        
    def click_new_appeasement_button(self):
        self.gf.clickButton(self.element_button_new_appeasement)

     
class AppeasementDetails(BaseAppeasementPage):
    def __init__(self, page):
        super().__init__(page)

    
    def input_appeasement_type_code(self, appeasement_type_code):
        #self.gf.writeText(self.element_input_appeasement_type_code, appeasement_type_code)
        self.gf.writeText_v2(self.element_input_appeasement_type_code, appeasement_type_code)

    def input_appeasement_description(self, appeasement_description):
        #self.gf.writeText(self.element_input_appeasement_description, appeasement_description)
        self.gf.writeText_v2(self.element_input_appeasement_description, appeasement_description)

    def select_credit_or_debit(self, credit_or_debit):
        self.gf.selectValue_v2(self.element_select_credit_or_debit, credit_or_debit)

    def select_is_active(self, is_active):
        self.gf.selectValue_v2(self.element_select_is_active, is_active)

    def select_is_actionable(self, is_actionable):
        self.gf.selectValue_v2(self.element_select_is_actionable, is_actionable)
        
    def click_button_save(self):
        self.gf.clickButton(self.element_button_save)
        

     
     
