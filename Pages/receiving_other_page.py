from Base.global_functions import GlobalFunctions
from Base.common_functions import CommonFunctions
from Base.api_functions import ApiFunctions
from Base.database_functions import DataBaseFunctions


class BaseReceivingOtherPage:
    def __init__(self, page):
        self.page = page
        self.gf = GlobalFunctions(self.page)
        self.cf = CommonFunctions(self.page)
        self.af = ApiFunctions(self.page)
        self.dbf = DataBaseFunctions()


        self.element_select_facility = "#facility"
        self.element_select_business_type = "#business_type"
        self.element_input_purchase_order = "#po-number"
        self.element_input_shipment_number = "#shipment-number"
        self.element_input_quantity = "#input-quantity"
        self.element_input_sku_barcode = "#sku-barcode"
        self.element_button_close_container_F9 = "#btn_close-container-primary"

        self.element_button_close_container_modal = "#btn_close-container-modal"
        self.element_input_container_barcode = "#container-barcode"
        self. element_input_parent_container = "#parent-barcode"

        self.element_button_complete_container = "#btn_complete-container-modal"
        
        self.element_button_complete_F10 = "#btn_complete-container-primary"

        



class ReceivingOtherPage(BaseReceivingOtherPage):
    def __init__(self, page):
        super().__init__(page)
        
    def select_facility(self, facility):
        self.gf.selectValue(self.element_select_facility, facility)

    def select_business_type(self, business_type):
        self.gf.selectValue(self.element_select_business_type, business_type)

    def input_po_number(self, po):
        self.gf.writeText(self.element_input_purchase_order, po)

    def input_shipment_number(self, shipment_number):
        self.gf.writeText(self.element_input_shipment_number, shipment_number)

    def input_quantity(self, quantity):
        self.gf.writeText(self.element_input_quantity, quantity)
        
    def input_sku_barcode(self, barcode):
        self.gf.writeText(self.element_input_sku_barcode, barcode)
        self.page.keyboard.press("Enter")

    def click_button_close_container_F9(self):
        self.gf.clickButton(self.element_button_close_container_F9)

    def input_container_barcode(self, barcode):
        self.gf.writeText(self.element_input_container_barcode, barcode)

    def click_button_close_container_modal(self):
        self.gf.clickButton(self.element_button_close_container_modal)
        self.gf.Wait(1)

    def click_button_complete_container(self):
        self.gf.clickButton(self.element_button_complete_container)

    def click_button_complete_F10(self):
        self.gf.clickButton(self.element_button_complete_F10)

        


     
 