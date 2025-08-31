from Base.global_functions import GlobalFunctions
from Base.common_functions import CommonFunctions
from Base.api_functions import ApiFunctions
from Base.database_functions import DataBaseFunctions


class BaseWavePage:
    def __init__(self, page):
        self.page = page
        self.gf = GlobalFunctions(self.page)
        self.cf = CommonFunctions(self.page)
        self.af = ApiFunctions(self.page)
        self.dbf = DataBaseFunctions()

        self.element_button_new_wave = self.page.locator("//a[contains(.,'New Wave')]")
        
        self.element_select_facility = self.page.locator("#wave-form > div > div.panel-body > fieldset:nth-child(1) > div > div:nth-child(1) > div > span > span.selection > span") #(".select2-container--focus > span:nth-child(1) > span:nth-child(1)") #"//span[contains(@aria-labelledby,'select2-cart-hg-container')]"
        self.element_select_facility_search = self.page.locator("span > span.select2-search.select2-search--dropdown > input")
        self.element_select_facility_results = self.page.locator(".select2-results")
         
        self.element_select_cart = self.page.locator("#cart_type_selector_parent > span > span.selection > span")
        self.element_select_cart_search = self.page.locator("#cart_type_selector_parent > span:nth-child(4) > span > span.select2-search.select2-search--dropdown > input")
        self.element_select_cart_results = self.page.locator('.select2-results')

        self.element_button_order_bulk_add = self.page.locator("#wave-multiple-orders-btn")
        self.element_input_order_list = self.page.locator("#multiple-orders-list")
        self.element_button_add_orders = self.page.locator("#add-multiple-orders")

        self.element_check_exclude_singles = self.page.locator("#exclude-singles")

        self.element_button_preview_wave = self.page.locator("#filter-selection-submit")
        self.element_button_submit_wave = self.page.locator("#submit-wave")



class WavePage(BaseWavePage):
    def __init__(self, page):
        super().__init__(page)

    def create_new_wave(self):
        self.gf.clickButton(self.element_button_new_wave)


class NewWavePage(BaseWavePage):
    def __init__(self, page):
        super().__init__(page)

    def select_facility(self, value):
        self.gf.select2Value(self.element_select_facility, self.element_select_facility_search, self.element_select_facility_results, value, value)
        
    def select_cart_type(self, value):
        self.gf.select2Value(self.element_select_cart, self.element_select_cart_search, self.element_select_cart_results, value, value) 

    def click_button_order_bulk_add(self):
        self.gf.clickButton(self.element_button_order_bulk_add)

    def input_order_list(self, orders):
        print(orders)
        order_to_bulk = ", ".join(orders)
        self.gf.writeText_v2(self.element_input_order_list, order_to_bulk)

    def click_button_add_bulk_orders(self):
        self.gf.clickButton(self.element_button_add_orders)

    def click_button_preview_wave(self):
        self.gf.clickButton(self.element_button_preview_wave)

    def validate_checkbox_exclude_singles_checked(self):
        if self.element_check_exclude_singles.is_checked():
            self.element_check_exclude_singles.uncheck()

    def click_button_submit_wave(self):
        self.gf.clickButton(self.element_button_submit_wave)
            
 