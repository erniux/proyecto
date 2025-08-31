from Base.global_functions import GlobalFunctions
from Base.common_functions import CommonFunctions
from Base.api_functions import ApiFunctions
from Base.database_functions import DataBaseFunctions


class BaseItemsPage:
    def __init__(self, page):
        self.page = page
        self.gf = GlobalFunctions(self.page)
        self.cf = CommonFunctions(self.page)
        self.af = ApiFunctions(self.page)
        self.dbf = DataBaseFunctions()

        self.element_button_new_cart = self.page.locator("#add-row-button")
        
        self.element_select_item = self.page.locator("//span[@role='combobox']")
        self.element_select_item_search = self.page.locator("(//input[@type='search'])[2]")
        self.element_select_item_results = self.page.locator(".select2-results")
        
        self.element_item_status = self.page.locator("#status")
        self.element_item_code = self.page.locator("#item_code")
        self.element_item_desc = self.page.locator("#description")
        self.element_item_original_price = self.page.locator("#original_price")
        self.element_item_cost = self.page.locator("#cost")
        self.element_item_marketing_desc = self.page.locator("#marketing_description")

        self.element_item_button_save = self.page.locator("//button[contains(.,'Save Changes')]")

        self.element_item_tab_sku_details = self.page.locator("//a[@data-toggle='tab'][contains(.,'SKU Details')]")
        self.element_item_tab_sku_attributes = self.page.locator("//a[@data-toggle='tab'][contains(.,'SKU Attributes')]")
        
        self.element_sku_button_add = self.page.locator(".jsgrid-mode-button")
        self.element_sku_input_code = self.page.locator("(//input[@type='text'])[35]")
        self.element_sku_input_desc = self.page.locator("textarea")
        self.element_sku_input_barcode = self.page.locator("(//input[@type='text'])[36]")
        self.element_sku_input_original_price = self.page.locator("(//input[@type='text'])[37]")
        #manage-skus-table > div.jsgrid-grid-header.jsgrid-header-scrollbar > table > tbody > tr.jsgrid-insert-row > td:nth-child(5) > input[type=text]
        self.element_sku_input_current_price = self.page.locator("(//input[@type='text'])[38]")
        
        self.element_sku_input_cost = self.page.locator("(//input[@type='text'])[39]")
        self.element_sku_checkbox_backorderable = self.page.locator(".jsgrid-insert-row > td:nth-of-type(11) > input[type='checkbox']")
        
        self.element_sku_input_inventory_threshold = self.page.locator("(//input[contains(@type,'text')])[44]")
        self.element_sku_input_box_quantity =  self.page.locator("(//input[contains(@type,'text')])[45]")
        self.element_sku_checkbox_uses_inventory = self.page.locator("(//input[contains(@type,'checkbox')])[7]")
        #self.element_sku_check_box_signature_label = "(//input[contains(@type,'checkbox')])[11]"
        self.element_sku_button_insert = self.page.locator("(//input[contains(@title,'Insert')])[1]")

        self.element_sku_table_detail = self.page.locator("#manage-skus-table > div.jsgrid-grid-body > table")


class ItemsPage(BaseItemsPage):
    def __init__(self, page):
        super().__init__(page)
        
    def click_new_cart_button(self):
        self.gf.clickButton(self.element_button_new_cart)

    def search_item(self, item):
        self.gf.select2Value_2(self.element_select_item, self.element_select_item_search,
                             self.element_select_item_results )

     
class ItemsDetails(BaseItemsPage):
    def __init__(self, page):
        super().__init__(page)


    def input_item_code(self, item_code):
        self.gf.writeText_v2(self.element_item_code, item_code)

    def input_item_desc(self, desc):
        self.gf.writeText_v2(self.element_item_desc, desc)

    def input_item_original_price(self, original_price):
        self.gf.writeText_v2(self.element_item_original_price, original_price)

    def input_item_cost(self, item_cost):
        self.gf.writeText_v2(self.element_item_cost, item_cost)

    def click_item_button_save(self):
        self.gf.clickButton(self.element_item_button_save)


class ItemsAttributes(BaseItemsPage):
    def __init__(self, page):
        super().__init__(page)

    def input_item_marketing_description(self, desc):
        self.gf.writeText_v2(self.element_item_marketing_desc, desc)


class SkuDetails(BaseItemsPage):
    def __init__(self, page):
        super().__init__(page)

    def click_tab_sku_details(self):
        self.gf.clickTab(self.element_item_tab_sku_details)

    def click_sku_button_insert(self):
        self.gf.clickButton(self.element_sku_button_add)

    def input_sku_code(self, sku_code):
        self.gf.writeText_v2(self.element_sku_input_code, sku_code)

    def input_sku_description(self, desc):
        self.gf.writeText_v2(self.element_sku_input_desc, desc)

    def input_sku_barcode(self, barcode):
        self.gf.writeText_v2(self.element_sku_input_barcode, barcode)

    def input_sku_original_price(self, price):
        self.gf.writeText_v2(self.element_sku_input_original_price, price)

    def input_sku_current_price(self, price):
        self.gf.writeText_v2(self.element_sku_input_current_price, price)

    def input_sku_cost(self, cost):
        self.gf.writeText_v2(self.element_sku_input_cost, cost)

    def check_sku_backorderable(self):
        self.gf.checkBox(self.element_sku_checkbox_backorderable)

   # def check_sku_signature_label_required(self):
   #     self.gf.checkBox(self.element_sku_check_box_signature_label)

    def input_sku_inventory_threshold(self, qty):
        self.gf.writeText_v2(self.element_sku_input_inventory_threshold, qty)

    def input_sku_box_quantity(self, qty):
        self.gf.writeText_v2(self.element_sku_input_box_quantity, qty)

    def click_sku_button_save(self):
        self.gf.clickButton(self.element_sku_button_insert)
        self.gf.validateToast("Data successfully saved")
        

    def  validate_sku_saved(self, sku):
        self.gf.validateText(self.element_sku_table_detail, sku)
        

class SkuAttributes(BaseItemsPage):
    def __init__(self, page):
        super().__init__(page)

    def click_tab_sku_attributes(self):
        self.gf.clickTab(self.element_item_tab_sku_attributes)


class Kitting(BaseItemsPage):
    def __init__(self, page):
        super().__init__(page)


class PriceGroups(BaseItemsPage):
    def __init__(self, page):
        super().__init__(page)


class SkuAddition(BaseItemsPage):
    def __init__(self, page):
        super().__init__(page)