from Base.global_functions import GlobalFunctions
from Base.common_functions import CommonFunctions
from Base.api_functions import ApiFunctions
from Base.database_functions import DataBaseFunctions


class BasePutawayPage:
    def __init__(self, page):
        self.page = page
        self.gf = GlobalFunctions(self.page)
        self.cf = CommonFunctions(self.page)
        self.af = ApiFunctions(self.page)
        self.dbf = DataBaseFunctions()

        self.element_select_facility = self.page.locator("#facility")
        self.element_input_container_barcode = self.page.locator("#container")
        self.element_input_location_barcode = self.page.locator("#location")
        self.element_input_sku_barcode = self.page.locator("#sku")
        self.element_button_add = self.page.locator("//button[@type='submit'][contains(.,'Add')]")
        self.element_input_location_barcode = self.page.locator("//input[contains(@name,'target')]")
        self.element_button_select_location = self.page.locator("//button[@type='submit'][contains(.,'Select')]")
        self.element_button_complete_putaway = self.page.locator("//button[@type='button'][contains(.,'Complete Putaway')]")


class PutawayActivePage(BasePutawayPage):
    def __init__(self, page):
        super().__init__(page)


    def select_facility(self, facility):
        self.gf.selectValue(self.element_select_facility, facility)
        
    def input_container_barcode(self, barcode):
        self.gf.writeText_v2(self.element_input_container_barcode, barcode)
        #self.page.pause()

    def click_add_container(self, barcode):
        self.gf.clickButton(self.element_button_add)
        #is_valid = self.gf.validateToast("Barcode Used: " + barcode)
        ##print(is_valid)
        #if is_valid:
        #    return False


    def input_location_barcode(self, location):
        self.gf.writeText_v2(self.element_input_location_barcode, location)

    def click_select_location(self):
        self.gf.clickButton(self.element_button_select_location)

    def click_complete_putaway(self):
        self.gf.clickButton(self.element_button_complete_putaway)

     
class PutawayOtherPage(BasePutawayPage):
    def __init__(self, page):
        super().__init__(page)

    
    def input_container_barcode(self, barcode):
        self.gf.writeText_v2(self.element_input_container_barcode, barcode)

    def click_add_container(self):
        self.gf.clickButton(self.element_button_add)
        
