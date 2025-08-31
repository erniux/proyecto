from Base.global_functions import GlobalFunctions
from Base.common_functions import CommonFunctions
from Base.api_functions import ApiFunctions
from Base.database_functions import DataBaseFunctions


class BaseReceivingStandardPage:
    def __init__(self, page):
        self.page = page
        self.gf = GlobalFunctions(self.page)
        self.cf = CommonFunctions(self.page)
        self.af = ApiFunctions(self.page)
        self.dbf = DataBaseFunctions()

        self.element_select_facility = self.page.locator("#facility")
        self.element_select_business_type = self.page.locator("#business_type")
        self.element_input_purchase_order = self.page.locator("#po-number")
        self.element_input_shipment_number = self.page.locator("#shipment-number")
        self.element_input_quantity = self.page.locator("#input-quantity")
        self.element_input_sku_barcode = self.page.locator("#sku-barcode")
        self.element_button_close_container_F9 = self.page.locator("#btn_close-container-primary")
        self.element_button_close_container_modal = self.page.locator("#btn_close-container-modal")
        self.element_input_container_barcode = self.page.locator("#container-barcode")
        self. element_input_parent_container = self.page.locator("#parent-barcode")
        self.element_button_complete_container = self.page.locator("#btn_complete-container-modal")
        self.element_button_complete_F10 = self.page.locator("#btn_complete-container-primary")

        
class ReceivingStandardPage(BaseReceivingStandardPage):
    def __init__(self, page):
        super().__init__(page)
        
    def select_facility(self, facility):
        self.gf.selectValue(self.element_select_facility, facility)

    def select_business_type(self, business_type):
        self.gf.selectValue(self.element_select_business_type, business_type)

    def input_po_number(self, po):
        self.gf.writeText_v2(self.element_input_purchase_order, po)

    def input_shipment_number(self, shipment_number):
        self.gf.writeText_v2(self.element_input_shipment_number, shipment_number)

    def input_quantity(self, quantity):
        self.gf.writeText_v2(self.element_input_quantity, quantity)
        
    def input_sku_barcode(self, barcode):
        self.gf.writeText_v2(self.element_input_sku_barcode, barcode)
        self.gf.clickEnter(self.page.locator("#content-table"), barcode)
        #self.gf.validateToast("SKU Found")
        #self.page.wait_for_load_state()
        
    def click_button_close_container_F9(self):
        self.gf.clickButton(self.element_button_close_container_F9)

    def input_container_barcode(self, barcode):
        self.gf.writeText_v2(self.element_input_container_barcode, barcode)

    def click_button_close_container_modal(self):
        self.gf.clickButton(self.element_button_close_container_modal)
        #self.gf.validateToastHidden("SKU Found")   

    def click_button_complete_F10(self):
        self.gf.clickButton(self.element_button_complete_F10)
        self.gf.clickButton(self.element_button_complete_container)
        

        


     
 