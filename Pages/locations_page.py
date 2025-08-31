from Base.global_functions import GlobalFunctions
from Base.common_functions import CommonFunctions
from Base.api_functions import ApiFunctions
from Base.database_functions import DataBaseFunctions


class BaseLocationsPage:
    def __init__(self, page):
        self.page = page
        self.gf = GlobalFunctions(self.page)
        self.cf = CommonFunctions(self.page)
        self.af = ApiFunctions(self.page)
        self.dbf = DataBaseFunctions()

        self.element_table_locations = self.page.locator("//table[@id='location-table']")
        self.element_button_new_location = self.page.locator("//button[contains(.,'New')]")
        self.element_select_facility = self.page.locator("//span[@role='combobox']")
        self.element_select_facility_search = self.page.locator("(//input[@type='search'])[2]")
        self.element_select_facility_results = self.page.locator(".select2-results")
        self.element_select_location_type = self.page.locator("#location_type")
        self.element_input_pick_path_order = self.page.locator("#pick_path_order")
        self.element_input_building = self.page.locator("#building")
        self.element_input_aisle = self.page.locator("#aisle")
        self.element_input_rack = self.page.locator("#rack")
        self.element_input_shelf = self.page.locator("#shelf")
        self.element_input_bin = self.page.locator("#bin")
        self.element_input_location = self.page.locator("#location")
        self.element_input_barcode = self.page.locator("#barcode")
        self.element_input_width = self.page.locator("#width")
        self.element_input_height = self.page.locator("#height")
        self.element_input_depth = self.page.locator("#depth")
        self.element_input_min_qty = self.page.locator("#min_qty")
        self.element_input_max_qty = self.page.locator("#max_qty")
        self.element_checkbox_dynamic_extensions = self.page.locator("#allow_dynamic_extensions")
        self.element_select_velocity = self.page.locator("#velocity")
        self.element_input_facility_visualizer_mapping = self.page.locator("#facility_visualizer_mapping")
        self.element_check_is_enabled = self.page.locator("//input[@class='form-check-input'][contains(@id,'enabled')]")

        self.element_button_save = self.page.locator("#modal-reasons-save")


class LocationsPage(BaseLocationsPage):
    def __init__(self, page):
        super().__init__(page)
        
    def click_new_location_button(self):
        self.gf.clickButton(self.element_button_new_location)

     
class LocationsDetails(BaseLocationsPage):
    def __init__(self, page):
        super().__init__(page)

    
    def select_facility_code(self, facility_code):
        self.gf.select2Value_2(self.element_select_facility, self.element_select_facility_search,
                             self.element_select_facility_results, facility_code, facility_code )

    def select_location_type(self, location_type):
        self.gf.selectValue(self.element_select_location_type, location_type) 
        
    def input_pick_path_order(self, order):
        self.gf.writeText_v2(self.element_input_pick_path_order, order)

    def input_building(self, building):
        self.gf.writeText_v2(self.element_input_building, building)

    def input_aisle(self, aisle):
        self.gf.writeText_v2(self.element_input_aisle, aisle)

    def input_rack(self, rack):
        self.gf.writeText_v2(self.element_input_rack, rack)

    def input_shelf(self, shelf):
        self.gf.writeText_v2(self.element_input_shelf, shelf)

    def input_bin(self, bin):
        self.gf.writeText_v2(self.element_input_bin, bin)

    def select_velocity(self, velocity):
        self.gf.selectValue(self.element_select_velocity, velocity)

    def input_location(self, location):
        self.gf.writeText_v2(self.element_input_location, location)

    def input_barcode(self, barcode):
        self.gf.writeText_v2(self.element_input_barcode, barcode)

    def input_width(self, width):
        self.gf.writeText_v2(self.element_input_width, width)

    def input_height(self, height):
        self.gf.writeText_v2(self.element_input_height, height)
    
    def input_depth(self, depth):
        self.gf.writeText_v2(self.element_input_depth, depth)
    
    def input_min_qty(self, min_qty):
        self.gf.writeText_v2(self.element_input_min_qty, min_qty)
    
    def input_max_qty(self, max_qty):
        self.gf.writeText_v2(self.element_input_max_qty, max_qty)
    
    def input_facility_visualizer_mapping(self, map):
        self.gf.writeText_v2(self.element_input_facility_visualizer_mapping, map)

    def check_is_enabled(self):
        self.gf.checkBox(self.element_check_is_enabled)

    def click_button_save(self):
        self.gf.clickButton(self.element_button_save)
        

     
     
