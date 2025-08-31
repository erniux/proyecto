from Base.global_functions import GlobalFunctions
from Base.common_functions import CommonFunctions
from Base.api_functions import ApiFunctions
from Base.database_functions import DataBaseFunctions
 

class BaseOrderPage:
    def __init__(self, page):
        self.page = page
        self.gf = GlobalFunctions(self.page)
        self.cf = CommonFunctions(self.page)
        self.af = ApiFunctions(self.page)
        self.dbf = DataBaseFunctions()

         
        self.element_button_new_order = self.page.locator("//button[contains(.,'New Order')]")
        self.element_table_open_orders = "#open-orders-table_wrapper"

        #Source (select2)
        self.element_select_source = "#create-order-source-code-parent"
        self.element_select_source_search = "[type='search']"
        self.element_select_source_results = ".select2-results"

        #Order details
        self.element_table_row_column_ordered_first_element = "tr.odd:nth-child(1) > td:nth-child(9)"
        self.element_table_row_column_new_first_element = "tr.odd:nth-child(1) > td:nth-child(10)"
        self.element_table_row_column_allocated_first_element = "tr.odd:nth-child(1) > td:nth-child(11)"
        self.element_table_row_column_printed_first_element = "tr.odd:nth-child(1) > td:nth-child(12)"
        self.element_table_row_column_backordered_first_element = "tr.odd:nth-child(1) > td:nth-child(13)"
        self.element_table_row_column_shipped_first_element = "tr.odd:nth-child(1) > td:nth-child(14)"
        self.element_table_row_column_canceled_first_element = "div.col-md-2:nth-child(11)" #"div.col-md-2:nth-child(11)" #"tr.odd:nth-child(1) > td:nth-child(15)"

        self.element_input_cancel_units = "#order-summary-quantities > :nth-child(11)"
        self.element_select_cancel_reason = self.page.get_by_label("reason-code") #"':nth-child(1) > .col-md-7 > :nth-child(7) > .form-control'"
        
        self.element_button_submit_cancel_units = "#submitCancel"

        #page.get_by_label("cancel-quantity").click()
        #page.get_by_label("cancel-quantity").fill("01")
        #page.get_by_label("reason-code").select_option("4000")
        #page.get_by_role("button", name=" Cancel Units").click()
        #page.get_by_role("button", name="Confirm").click()
        #page.get_by_role("button", name="OK").click()

        #Items
        self.element_select_item = "#create-order-item-lookup-parent"
        #self.element_select_item_search = "[type='search']"   
        self.element_select_item_search = "//input[contains(@class,'select2-search__field')]"
        self.element_select_item_results = ".select2-results"
        self.element_search_sku = "//input[contains(@type,'search')]"
        self.element_input_sku_quantity = ".add-item-quantity"
        self.element_button_add_item_to_cart = "//button[@type='button'][contains(.,'Add to Cart')]"

        self.element_select_ship_code = '#ship-code-lookup'

        self.element_select_customer = "#select2-customer-lookup-container"
        self.element_select_customer_search = ".select2-search__field"
        self.element_select_customer_results = "#select2-customer-lookup-results"
        self.element_link_ship_to_address_same_as_customer = "//a[@id='shipto-copy-customer']"
        self.element_input_search_sku = "#product_info_filter"
        self.element_table_search_results_sku = "#product_info"
        
        #Not required elements
        self.element_input_order_number = "#order_number"
        self.element_select_salesperson = "#select2-salesperson_lookup-container"
        self.element_input_po_number = "#po_number"
        self.element_calendar_order_date = "#order_date"
        self.element_calendar_ship_by_date = "#ship_date"
        self.element_candelar_cancel_date = "#cancel_date"
        self.element_select_hold_reason = "#hold_reason"
        self.element_input_sku_item_to_search = "#product_info_filter"
        self.element_checkbox_carton_contents_label_required = "#carton-contents-required"
        
        #New Customer
        self.element_button_add_customer = "#add-customer-link > button:nth-child(1)"
        self.element_input_customer_firstname = "#first_name_select"
        self.element_input_customer_lastname = "#last_name_select"
        self.element_input_customer_company = "#company_select"
        self.element_input_customer_email = "#email_select"
        self.element_input_customer_phone_number = "#phone_number_select"
        self.element_input_customer_address_line1 = "#address1_select"
        self.element_input_customer_address_line2 = "#address2_select"
        self.element_input_customer_zipcode = "#zipcode_select"
        self.element_input_customer_city = "#city_select"
        self.element_select_customer_state = "#state_select-parent"
        self.element_select_customer_country = "#select2-country_select-container"
        self.element_button_save_customer = "#edit-customer-address-modal > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)"
        self.element_button_save_customer_changes="#modal-edit-customer-save-btn"

        #Ship to address
        self.shipto_add_ship_to_address_button="#add-shipto-link > button:nth-child(1)"
        self.shipto_firstname_input="#shipTo-first-name"
        self.shipto_lastname_input="#shipTo-last-name"
        self.shipto_company_input=""
        self.shipto_email_input=""
        self.shipto_phonenumber_input=""
        self.shipto_address1_input=""
        self.shipto_address2_input=""
        self.shipto_zipcode_input=""
        self.shipto_city_input=""
        self.shipto_state_select="#select2-shipTo-State-container"
        self.shipto_country_select="#select2-shipTo-country-container"
        self.shipto_savechanges_button="#modal-edit-shipping-save-btn"
        self.shipto_closemodal_button="#edit-ship-to-address-modal > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)"

        #payment
        self.element_button_add_payment = "//button[contains(.,'Add Payment')]"
        self.element_buton_next_add_payment = "//a[@href='#next']"
        self.element_link_same_as_customer = "//a[@id='billing-copy-customer']"
        self.element_link_add_payment = "//a[@href='#finish']"
        self.element_input_payment_ammount = "#paymentAmount"
        self.element_select_cardtype = "#cardTypes"
        
        #Button create order
        self.element_button_create_order_ = "#submit"

    def click_new_button(self):
        self.gf.clickButton(self.element_button_new_order)
        

class CreateOrderPage(BaseOrderPage):
    def __init__(self, page):
        super().__init__(page)

    
    def search_source(self, source):
        self.gf.select2Value(self.element_select_source, 
                             self.element_select_source_search, self.element_select_source_results,
                             source, 
                             source)
        
    
    def search_item(self, item):
        #self.page.pause()
        self.gf.select2Value(self.element_select_item, self.element_select_item_search,
                             self.element_select_item_results, item, f"Item Code: {item}")

        
    def select_sku(self, sku):
        self.gf.writeText(self.element_search_sku, sku)
        self.gf.validateText(self.element_table_search_results_sku, sku)
         
         
    def input_sku_quantity(self, quantity ):
        self.gf.writeText(self.element_input_sku_quantity, quantity)


    def add_items_to_cart(self):
        #self.gf.clickButton(self.element_button_add_item_to_cart)
        self.page.get_by_role("button", name=" Add to Cart").click()

     
    def select_shipping_method(self, ship_code):
        self.gf.selectValue(self.element_select_ship_code, ship_code)

    
    def select_customer(self):
        customer_first_name = "Mahnesmith" # self.search_customer(self.data["tenant_code"])
        self.gf.select2Value(self.element_select_customer, 
                             self.element_select_customer_search,
                             self.element_select_customer_results, 
                             customer_first_name, customer_first_name)


    def select_ship_to_address(self):
        self.gf.clickLink(self.element_link_ship_to_address_same_as_customer)
    
    
    def add_payment(self):
        self.gf.clickButton(self.element_button_add_payment)
        self.gf.clickLink(self.element_buton_next_add_payment)
        self.gf.clickLink(self.element_link_same_as_customer)
        self.gf.clickLink(self.element_link_add_payment)


    def click_create_order_button(self):
        self.gf.clickButton(self.element_button_create_order_)
         
      
    def validate_order_Status(self, order_number,expected_status):
        status = 'NEW'
        status = self.af.get_order_status(order_number)
        print(f"RESULT DESDE ORDER PAGE {status}")
        return status
    
    def select_items_with_qty_available(self, tenant, total_lines):
        sql=(f"SELECT * FROM product_inventory ")

    def search_customer(self, tenant):
        sql = f"SELECT first_name FROM customer_customer WHERE tenant_id in (SELECT id FROM system_tenant where tenant = '{tenant}') limit 1;"
        print(sql)
        rows = self.dbf.db_connection(sql)
        print(rows[0][0])
        return rows[0][0]
        

class ViewOrderPage(BaseOrderPage):
    def __init__(self, page):
        super().__init__(page)

    
    def input_cancel_units(self, qty):
        #self.gf.writeText(self.element_input_cancel_units, qty)
        self.page.get_by_label("cancel-quantity").click()
        self.page.get_by_label("cancel-quantity").fill("1")
        
        

    def select_cancel_reason(self, cancel_reason):
        #self.gf.selectValue(self.element_select_cancel_reason, cancel_reason)
        self.element_select_cancel_reason.select_option("4000")
        
        
    def click_button_submit_cancel_units(self):
        self.page.get_by_role("button", name=" Cancel Units").click()
        self.page.get_by_role("button", name="Confirm").click()
        

