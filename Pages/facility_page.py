from Base.global_functions import GlobalFunctions
from Base.common_functions import CommonFunctions
from Base.api_functions import ApiFunctions
from Base.database_functions import DataBaseFunctions


class BaseFacilityPage:
    def __init__(self, page):
        self.page = page
        self.gf = GlobalFunctions(self.page)
        self.cf = CommonFunctions(self.page)
        self.af = ApiFunctions(self.page)
        self.dbf = DataBaseFunctions()

        self.element_button_new_facility = self.page.locator("#add-row-button")
        self.element_link_facility1 = "//a[contains(.,'"
        self.element_link_facility2 = "')]"
        self.element_select_shipping_method_status = "(//select[@name='status'])[]"
        self.element_input_facility_name = self.page.locator("//input[@data-field='name']")
        self.element_input_facility_code = self.page.locator("//input[@data-field='facility_code']")
        self.element_select_work_flow = self.page.locator("//select[@data-field='workflow_type']")
        self.element_select_time_zone = self.page.locator("//select[@data-field='timezone']")
        self.element_input_director_name = self.page.locator("//input[@id='facilityDirector']")
        self.element_input_address1 = self.page.locator("//input[@data-field='address1']")
        self.element_input_address2 = self.page.locator("//input[@data-field='address2']")
        self.element_input_zipcode = self.page.locator("//input[@data-field='zipcode']")
        self.element_input_phone_number = self.page.locator("//input[@data-field='phone_number']")
        self.element_check_days1 = "//input[@data-day='"
        self.element_check_days2 = "']"
        self.element_select_active = self.page.locator("//select[@data-field='active']")
        self.element_select_pctl_generation = self.page.locator("//select[contains(@data-field,'generation')]")
        self.element_select_enable_allocation = self.page.locator("//select[@data-field='allocation_enabled']")
        self.element_input_carts_before_batching = self.page.locator("//input[contains(@data-field,'carts_before_batch')]")
        self.element_button_facility_save = self.page.locator("#add-facility-btn")
        self.element_button_facility_edit = self.page.locator("#edit-facility-btn")
        

class FacilityPage(BaseFacilityPage):
    def __init__(self, page):
        super().__init__(page)

    def click_new_facility_button(self):
        self.gf.clickButton(self.element_button_new_facility)  

    def click_faciliy_link(self, facility):
        self.gf.clickLink(self.element_link_facility1 + facility + self.element_link_facility2)


class FacilityDetails(BaseFacilityPage):
    def __init__(self, page):
        super().__init__(page)

    def input_facility_code(self, facility_code):
        self.gf.writeText_v2(self.element_input_facility_code, facility_code) 

    def input_facility_name(self, facility_name):
        self.gf.writeText_v2(self.element_input_facility_name, facility_name)

    def select_work_flow(self, workflow):
        self.gf.selectValue(self.element_select_work_flow, workflow)

    def select_time_zone(self, time_zone):
        self.gf.selectValue(self.element_select_time_zone, time_zone)

    def input_director_name(self, director_name):
        self.gf.writeText_v2(self.element_input_director_name, director_name)

    def input_address1(self, address):
        self.gf.writeText_v2(self.element_input_address1, address)

    def input_address2(self, address):
        self.gf.writeText_v2(self.element_input_address2, address)

    def input_zipcode(self, zipcode):
        self.gf.keyboardType(self.element_input_zipcode, zipcode)

    def input_phone_number(self, phone_number):
        self.gf.writeText_v2(self.element_input_phone_number, phone_number)

    def check_facility_days(self, days):
        for day in days:
            element = self.element_check_days1 + day + self.element_check_days2
            self.gf.checkBox(element)
            element = ""

    def select_facility_active(self, value):
        self.gf.selectValue_v2(self.element_select_active, value)
        
    def select_pctl_generation(self, value):
        self.gf.selectValue_v2(self.element_select_pctl_generation, value)

    def select_enable_allocation(self, value):
        self.gf.selectValue_v2(self.element_select_enable_allocation, value)

    def input_carts_before_batch(self,value):
        #self.page.pause()
        self.gf.writeText_v2(self.element_input_carts_before_batching, value)

    def click_save_facility(self):
        self.gf.clickButton(self.element_button_facility_save)
        
    def select_shipcode_status(self, status):
        #self.page.pause()
        for i in range(1,3):
            shipping_method = self.page.locator(self.element_select_shipping_method_status.replace("[]", f"[{i}]"))
            self.gf.selectValue(shipping_method, status)

    def select_carton_status(self, status):
        for i in range(3,5):
            shipping_method = self.page.locator(self.element_select_shipping_method_status.replace("[]", f"[{i}]"))
            self.gf.selectValue(shipping_method, status)

    def click_edit_facility(self):
        self.gf.clickButton(self.element_button_facility_edit)


        

    



    

    
