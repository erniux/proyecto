from Base.global_functions import GlobalFunctions
from Base.common_functions import CommonFunctions
from Base.api_functions import ApiFunctions
from Base.database_functions import DataBaseFunctions


class BaseCartsPage:
    def __init__(self, page):
        self.page = page
        self.gf = GlobalFunctions(self.page)
        self.cf = CommonFunctions(self.page)
        self.af = ApiFunctions(self.page)
        self.dbf = DataBaseFunctions()

        self.element_table_carts = self.page.locator("#cart-table")
        self.element_button_new_cart =  self.page.locator("//button[@class='btn btn-primary'][contains(.,'New')]")
        self.element_input_name = self.page.locator("#name")
        self.element_select_facility = self.page.locator("//span[@role='combobox']")
        self.element_select_facility_search = self.page.locator("(//input[@type='search'])[2]")
        self.element_select_facility_results = self.page.locator(".select2-results")
        self.element_input_description = self.page.locator("#description")

        #NEW FIELDS
        self.element_check_supertote = self.page.locator("#is_supertote")
        self.element_check_exception = self.page.locator("#is_exception")
        self.element_check_b2b = self.page.locator("#is_b2b")
        self.element_check_labelpacking = self.page.locator("#is_labelpacking")
        self.element_check_identipack = self.page.locator("#is_identipack")
        self.element_check_pick_module = self.page.locator("#is_pickmodule")
        self.element_check_is_jit = self.page.locator("#is_jit")
        self.element_check_replenishment_only = self.page.locator("#is_replenonly")
        self.element_check_is_prepack_container = self.page.locator("#is_prepack_container")
        self.element_check_is_conveyor = self.page.locator("#is_conveyorpicking")
        self.element_check_is_locus = self.page.locator("#is_locus")

        self.element_input_rows = self.page.locator("#rows")
        self.element_input_cols = self.page.locator("#columns")
        self.element_input_units_per_bin = self.page.locator("#units_per_bin")
        self.element_button_save = self.page.locator("button#modal-cart-save")
        
        
        


class CartsPage(BaseCartsPage):
    def __init__(self, page):
        super().__init__(page)
        
    def click_new_cart_button(self):
        self.gf.clickButton(self.element_button_new_cart)

     
class CartsDetails(BaseCartsPage):
    def __init__(self, page):
        super().__init__(page)

    
    def input_name(self, cart_name):
        self.gf.writeText_v2(self.element_input_name, cart_name)

    def select_facility_code(self, facility_code):
        self.gf.select2Value_2(self.element_select_facility, self.element_select_facility_search,
                             self.element_select_facility_results, facility_code, facility_code )

    def input_description(self, desc):
        self.gf.writeText_v2(self.element_input_description, desc) 
    
    def check_is_supertote(self):
        self.gf.checkBox(self.element_check_supertote)

    def check_is_exception(self):
        self.gf.checkBox(self.element_check_exception)

    def check_is_b2b(self):
        self.gf.checkBox(self.element_check_b2b)

    def check_is_label_packing(self):
        self.gf.checkBox(self.element_check_labelpacking)

    def check_is_identipack(self):
        self.gf.checkBox(self.element_check_identipack)

    def check_is_pick_module(self):
        self.gf.checkBox(self.element_check_pick_module)

    def check_is_jit(self):
        self.gf.checkBox(self.element_check_is_jit)

    def check_is_replenishment(self):
        self.gf.checkBox(self.element_check_replenishment_only)
    
    def check_is_prepack(self):
        self.gf.checkBox(self.element_check_replenishment_only)

    def check_is_conveyor(self):
        self.gf.checkBox(self.element_check_replenishment_only)

    def check_is_prepack_container(self):
        self.gf.checkBox(self.element_check_is_prepack_container)

    def check_is_locus(self):
        self.gf.checkBox(self.element_check_is_locus)

    def input_rows(self, rows):
        self.gf.writeText_v2(self.element_input_rows, rows)
    
    def input_cols(self, cols):
        self.gf.writeText_v2(self.element_input_cols, cols)
    
    def input_units_per_bin(self, units):
        self.gf.writeText_v2(self.element_input_units_per_bin, units)

    def click_button_save(self):
        self.element_button_save.scroll_into_view_if_needed()
        self.gf.clickButton(self.element_button_save)
        #self.element_button_save.click()
        #self.page.keyboard.press("Enter")
        #self.page.wait_for_load_state()


        
            
        

     
     
