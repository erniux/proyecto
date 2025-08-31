from Base.global_functions import GlobalFunctions
from Base.common_functions import CommonFunctions
from Base.api_functions import ApiFunctions
from Base.database_functions import DataBaseFunctions


class BaseOffersPage:
    def __init__(self, page):

        self.page = page
        self.gf = GlobalFunctions(self.page)
        self.cf = CommonFunctions(self.page)
        self.af = ApiFunctions(self.page)
        self.dbf = DataBaseFunctions()

        self.element_button_new_offer = self.page.locator("#add-row-button")
        self.element_input_offer_code = self.page.locator("//input[contains(@name,'offer_code')]")
        self.element_input_offer_desc = self.page.locator("//input[@name='description']")
        self.element_select_business_type = self.page.locator("//span[@role='combobox']")
        self.element_select_business_type_search = self.page.locator("//input[@class='select2-search__field']")
        self.element_select_business_type_results = self.page.locator(".select2-results" )
        self.element_input_offer_year = self.page.locator("//input[@name='offer_year']")
        self.element_calendar_start_date = self.page.locator("#datepicker-start_date")
        self.element_calendar_end_date = self.page.locator("#datepicker-end_date")
        self.element_button_save = self.page.locator("#modal-add-save-btn")

        

class OffersPage(BaseOffersPage):
    def __init__(self, page):
        super().__init__(page)
        
    def click_new_offer_button(self):
        self.gf.clickButton(self.element_button_new_offer)
    

class OffersDetails(BaseOffersPage):
    def __init__(self, page):
        super().__init__(page)

    def input_offer_code(self, offer_code):
        self.gf.writeText_v2(self.element_input_offer_code, offer_code) 

    def input_offer_description(self, offer_description):
        self.gf.writeText_v2(self.element_input_offer_desc, offer_description)

    def select_offer_business_type(self, business_type):
        #self.page.pause()
        self.gf.select2Value_2(self.element_select_business_type, 
                                    self.element_select_business_type_search,
                                    self.element_select_business_type_results ,business_type, business_type, 1) 
        
    def select_input_offer_year(self, year):
        self.gf.writeText_v2(self.element_input_offer_year, year)

    def select_calendar_start_date(self, start_date):
        self.gf.selectCalendar(self.element_calendar_start_date, start_date )

    def select_calendar_end_date(self, end_date):
        self.gf.selectCalendar(self.element_calendar_end_date, end_date )

    def button_save(self):
        self.gf.clickButton(self.element_button_save)

 