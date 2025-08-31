from Base.global_functions import GlobalFunctions
from Base.common_functions import CommonFunctions
from Base.api_functions import ApiFunctions
from Base.database_functions import DataBaseFunctions


class BaseInventoryTransactionsPage:
    def __init__(self, page):
        self.page = page
        self.gf = GlobalFunctions(self.page)
        self.cf = CommonFunctions(self.page)
        self.af = ApiFunctions(self.page)
        self.dbf = DataBaseFunctions()

        self.element_button_new_transaction_reason = self.page.locator("#new-reason")
        self.element_input_transaction_reason_code = self.page.locator("#reason_code")
        self.element_input_transaction_reason_description = self.page.locator("#description")
        self.element_select_transaction_type = self.page.locator("#transaction_type")
        self.element_check_require_note = self.page.locator("#require_note")
        self.element_check_require_input = self.page.locator("#require_input")
        self.element_input_prompt = self.page.locator("#input_prompt")
        self.element_select_status = self.page.locator("#status")
        
        self.element_button_save = self.page.locator("#modal-reasons-save")


class InventoryTransactionsPage(BaseInventoryTransactionsPage):
    def __init__(self, page):
        super().__init__(page)
        
    def click_new_button(self):
        self.gf.clickButton(self.element_button_new_transaction_reason)

     
class InventoryTransactionsDetails(BaseInventoryTransactionsPage):
    def __init__(self, page):
        super().__init__(page)

    def input_transaction_reason_code(self, code):
        self.gf.writeText_v2(self.element_input_transaction_reason_code, code)

    def input_transaction_reason_desc(self, desc):
        self.gf.writeText_v2(self.element_input_transaction_reason_description, desc)

    def select_transaction_type(self, transaction_type):
        self.gf.selectValue_v2(self.element_select_transaction_type, transaction_type)

    def check_require_note(self, require_note):
        self.gf.checkBox(self.element_check_require_note, require_note)
        
    def check_require_input(self, require_input):
        self.gf.checkBox(self.element_check_require_input, require_input)

    def select_status(self, status):
        self.gf.selectValue_v2(self.element_select_status, status)

    def click_button_save(self):
        self.gf.clickButton(self.element_button_save)

    
    
        
