from Base.global_functions import GlobalFunctions
from Base.common_functions import CommonFunctions




class BaseAdjustmentPage:
    def __init__(self, page):
        self.page = page
        self.gf = GlobalFunctions(self.page)
        self.cf = CommonFunctions(self.page)

        self.element_select_facility = self.page.locator('#facility')
        self.element_button_start_adjustment = self.page.locator("#assign")

        self.element_select_sku = self.page.locator("#inventory-adjustments-sku-select-parent > span > span.selection")
        self.element_select_sku_search = self.page.locator("[type='search']")
        self.element_select_sku_results = self.page.locator(".select2-results")

        self.element_input_adjustment_quantity = self.page.locator("#oms-adjustment-quantity")
        self.element_select_business_type = self.page.locator("#oms-adjustment-business-type")
        self.element_select_adjustment_reason = self.page.locator("#oms-adjustment-reason")
        self.element_input_adjustment_note = self.page.locator("#oms-adjustment-note")

        self.element_button_submit_adjustment = self.page.locator("#oms-submit-adjustment")


class AdjustmentPage(BaseAdjustmentPage):
    def __init__(self, page):
        super().__init__(page)

    
    def select_facility(self, facility):
        self.gf.selectValue(self.element_select_facility, facility)
        
    def click_button_start_adjustment(self):
        self.gf.clickButton(self.element_button_start_adjustment)

    def search_sku(self, value):
        self.gf.select2Value_2(self.element_select_sku, self.element_select_sku_search, self.element_select_sku_results, value, value)

    def input_adjustment_quantity(self, value):
        self.gf.writeText_v2(self.element_input_adjustment_quantity, value)


    def select_business_type(self, value):
        self.gf.selectValue(self.element_select_business_type, value)


    def select_adjustment_reason(self, value):
        self.gf.selectValue(self.element_select_adjustment_reason, value)

    
    def input_note(self, value):
        self.gf.writeText_v2(self.element_input_adjustment_note, value)

    
    def click_button_submit_adjustment(self):
        self.gf.clickButton(self.element_button_submit_adjustment)

