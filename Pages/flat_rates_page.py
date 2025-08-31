from Base.global_functions import GlobalFunctions
from Base.common_functions import CommonFunctions
from Base.api_functions import ApiFunctions
from Base.database_functions import DataBaseFunctions


class BaseFlatRatesPage:
    def __init__(self, page):
        self.page = page
        self.gf = GlobalFunctions(self.page)
        self.cf = CommonFunctions(self.page)
        self.af = ApiFunctions(self.page)
        self.dbf = DataBaseFunctions()

        self.element_button_new_flat_rate = self.page.locator("#new-flatrate")
        self.element_table_flat_rate = self.page.locator("#flatrate-table")
        self.element_select_ship_code = self.page.locator("#ship_code")
        self.element_input_min_amount = self.page.locator("#min_cost")
        self.element_input_max_amount = self.page.locator("#max_cost")
        self.element_input_shipping_cost = self.page.locator("#shipping_cost")
        self.element_button_save = self.page.locator("#modal-flatrate-save")


class FlatRatesPage(BaseFlatRatesPage):
    def __init__(self, page):
        super().__init__(page)
        
    def click_new_override_button(self):
        self.gf.clickButton(self.element_button_new_flat_rate)


class FlatRatesDetails(BaseFlatRatesPage):
    def __init__(self, page):
        super().__init__(page)

    
    def select_ship_code(self, ship_code):
        self.gf.selectValue(self.element_select_ship_code, ship_code)

    def input_minimum_amount(self, amount):
        self.gf.writeText_v2(self.element_input_min_amount, amount)

    def input_maximum_amount(self, amount):
        self.gf.writeText_v2(self.element_input_max_amount, amount)

    def input_shipping_amount(self, amount):
        self.gf.writeText_v2(self.element_input_shipping_cost, amount)
        
    def click_save_button(self):
        self.gf.clickButton(self.element_button_save)

    

     
     
