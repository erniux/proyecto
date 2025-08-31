from Base.global_functions import GlobalFunctions
from Base.common_functions import CommonFunctions
from Base.api_functions import ApiFunctions
from Base.database_functions import DataBaseFunctions


class BaseCardPaymentsPage:
    def __init__(self, page):
        self.page = page
        self.gf = GlobalFunctions(self.page)
        self.cf = CommonFunctions(self.page)
        self.af = ApiFunctions(self.page)
        self.dbf = DataBaseFunctions()

        self.element_button_noc_cash = self.page.locator("//input[contains(@id,'card_check_input_CASH_[NOC]NoCharge')]")
        self.element_checkbox_ui_enable = self.page.locator("#ui_enabled_input")
        self.element_button_save_setup = self.page.locator("#tenant-payment-type-card-type-modal-save-btn")
        


class CardPaymentsPage(BaseCardPaymentsPage):
    def __init__(self, page):
        super().__init__(page)
        
    def enable_noc_cash_payment_setup(self):
        self.gf.clickButton(self.element_button_noc_cash)


class CardPaymentsDetails(BaseCardPaymentsPage):
    def __init__(self, page):
        super().__init__(page)

    def click_ui_enabled(self):
        self.gf.checkBox(self.element_checkbox_ui_enable)
    
    def click_save_button(self):
        self.gf.clickButton(self.element_button_save_setup)

    

     
     
