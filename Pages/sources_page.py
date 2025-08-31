from Base.global_functions import GlobalFunctions
from Base.common_functions import CommonFunctions
from Base.api_functions import ApiFunctions
from Base.database_functions import DataBaseFunctions


class BaseSourcesPage:
    def __init__(self, page):
        self.page = page
        self.gf = GlobalFunctions(self.page)
        self.cf = CommonFunctions(self.page)
        self.af = ApiFunctions(self.page)
        self.dbf = DataBaseFunctions()

        self.element_button_new_source = self.page.locator("#new-source")
        self.element_input_source_code = self.page.locator("#source_code")
        self.element_input_source_description = self.page.locator("#description")
        self.element_select_offer = self.page.locator("//span[@aria-labelledby='select2-offer_code-container']")
        self.element_select_offer_search = self.page.locator("//input[@class='select2-search__field']")
        self.element_select_offer_results = self.page.locator(".select2-results")
        self.element_select_is_active = self.page.locator("#is_active")
        self.element_select_calendar_start_promotion = self.page.locator("#start_promotion")
        self.element_select_calendar_end_promotion = self.page.locator("#end_promotion")
        self.element_input_promotion_price = self.page.locator("#promotion_price")
        self.element_select_billing_type = self.page.locator("#billing_type")
        self.element_select_allocation_facility = self.page.locator("#allocation_facility")
        self.element_button_save = self.page.locator("#modal-sources-save")
        self.element_select_is_pre_dimmed = self.page.locator("input[name='pre_dimmed_enabled']")
        self.element_link_edit_source = self.page.locator("#source-table > tbody > tr > th > a > i")



class SourcesPage(BaseSourcesPage):
    def __init__(self, page):
        super().__init__(page)
        
    def click_new_source_button(self):
        self.gf.clickButton(self.element_button_new_source)

    def click_link_edit_source(self):
        self.gf.clickLink(self.element_link_edit_source)

     
class SourcesDetails(BaseSourcesPage):
    def __init__(self, page):
        super().__init__(page)

    
    def input_source_code(self, source_code):
        self.gf.writeText_v2(self.element_input_source_code, source_code)

    def input_source_description(self, source_description):
        self.gf.writeText_v2(self.element_input_source_description, source_description)

    def select_offer(self, offer_code):
        self.gf.select2Value_2(self.element_select_offer, self.element_select_offer_search,
                             self.element_select_offer_results, offer_code, offer_code)

    def select_is_active(self, is_active):
        self.gf.selectValue(self.element_select_is_active, is_active)

    def select_start_promotion(self, start_promotion):
        self.gf.selectCalendar(self.element_select_calendar_start_promotion, start_promotion)

    def select_end_promotion(self, end_promotion):
        self.gf.selectCalendar(self.element_select_calendar_end_promotion, end_promotion)

    def input_promotion_price(self, price):
        #self.page.pause()
        self.gf.writeText_v2(self.element_input_promotion_price, price)

    def select_billing_type(self, billing_type):
        self.gf.selectValue(self.element_select_billing_type, billing_type)

    def select_allocation_facility(self, allocation_facility):
        self.gf.selectValue(self.element_select_allocation_facility, allocation_facility)
        
    def click_button_save(self):
        self.gf.clickButton(self.element_button_save)

    def is_pre_dimmed_enabled_field_visible(self):
        return self.element_select_is_pre_dimmed.is_visible()
    
    
        

     
     
