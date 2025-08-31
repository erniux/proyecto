import re
import time
import json
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from Base.global_functions import GlobalFunctions


delay = 0

class CommonFunctions:
    
    def __init__(self, page):
        self.page = page
        self.globalFunction = GlobalFunctions(page)

        self.input_username = '#id_username'
        self.input_password = '#id_password'
        self.button_login = self.page.locator("#login")
        self.button_acceptance_message = self.page.locator("#acceptable-use-modal-accept")

        #Menu Orders
        self.menu_orders = "Orders"
        self.menu_create_order = "Create Order"

        #Menu Inventory
        self.menu_inventory = "Inventory"
        self.menu_items ="Items"
        self.menu_adjustments = "Adjustments"
        self.menu_business_type_transfer = "Business Type Transfer"
        self.menu_purchase_orders = "Purchase Orders"


        #Menu System
        self.menu_system = "System"
        self.menu_facilities = "Facilities"
        self.menu_tenants = "Tenants"
        self.menu_departments = "Departments"
        self.menu_sales_tax = "Sales Tax"
        self.menu_class_tax = "Class Tax"
        self.menu_vendor_groups = "Vendor Groups"
        self.menu_workstations = "Workstations"
        self.menu_control_setings = "Control Settings"
        self.menu_sales_person = "Salesperson"
        self.menu_vendors = "Vendors"
        self.menu_client_setup = "Client Setup"
        self.menu_shipping = "Shipping"
        
        #Menu Users and groups
        self.menu_users_groups = "Users and Groups"
        self.menu_groups = "//a[@href='/account/manage-groups']"  
        self.menu_users = "//a[@href='/account/manage-users']"  
        self.user_security = "User Security"
        self.reset_password = "Reset Worker Password"

        #Menu Client Setup
        self.menu_business_types = "Business Types"
        self.menu_allocation = "Allocation"
        self.menu_offers = "Offers"
        self.menu_appeasements = "Appeasement Types"
        self.menu_sources = "Sources"
        self.menu_cancel_reasons = "Cancellation Reasons"
        self.menu_exception_reasons = "Exception Reasons"
        self.menu_exception_resolution_reasons = "Exception Resolution Reasons"
        self.menu_hold_reasons = "Hold Reasons"
        self.menu_inventory_transaction_reasons = "Inventory Transaction Reasons"
        self.menu_override_reasons = "Override Reasons"
        self.menu_card_type_setup = "Payment Setup"

        #Menu Shipping
        self.menu_carriers = "Carriers"
        self.menu_shipcodes = "Ship Codes"
        self.menu_translation = "Translation"
        self.menu_disposition_codes = "Disposition Codes"
        self.menu_flat_rate_shipping = "Flat Rate Shipping"
        self.menu_freight_rates = "Freight Rates"

        #Menu WMS
        self.menu_wms = "WMS"
        self.menu_wms_dashboard = "Dashboard"
        self.menu_wms_dashboard_v2Beta = "Dashboard V2 Beta"
        self.menu_adjust_to_active = "Adjust To Active"
        self.menu_batch_picking = "Batch Picking"
        self.menu_induction = "Induction"
        self.menu_label_packing = "Label Packing"
        self.menu_label_packing_wms = "Packing (WMS)"
        self.menu_projects = "Projects"
        self.menu_receiving = "Receiving"
        self.menu_putaway = "Putaway"
        self.menu_warehouse = "Warehouse"
        self.menu_waves = "Waves"
        self.menu_audit_v2 = "Inventory Audit V2"

        #Menu Inventory Audit Task V2
        self.menu_audit_v2_batches = "//a[@href='/wms/inventory-audit/batches']"
        self.menu_audit_v2_tasks = "//a[@href='/wms/inventory-audit/tasks']"
        self.menu_audit_v2_variances = "//a[@href='/wms/inventory-audit/variances']"
        self.menu_audit_v2_work = "//a[@href='/wms/inventory-audit/work']"
        
        #Putaway
        self.menu_putaway_active = "Putaway - Active"
        self.menu_putaway_reserve = "Putaway - Reserve"

        #Menu Receiving
        self.menu_by_asn = "By ASN"
        self.menu_standard = "Standard"
        self.menu_print_barcodes = "Print Barcode"


        #Menu Warehouse
        self.menu_warehouse = "Warehouse"
        self.menu_locations = "Locations"
        self.menu_carts = "Carts"
        self.menu_waves = "Waves"
        
        #Django admin
        self.menu_admin_groups = "Groups"

        #Generic elements
        self.data_table = self.page.locator(".dataTables_scroll")
        self.input_search = self.page.locator("//input[@type='search']")
        self.button_save = self.page.locator("//button[contains(.,'Save Changes')]")
        self.element_select_tenant = self.page.locator("#view-as-tenant-select")
#view-as-tenant-select

    def login(self, user, password):
        self.globalFunction.writeText(self.input_username, user)
        self.globalFunction.writeText(self.input_password, password)

        self.globalFunction.clickButton(self.button_login)

        self.globalFunction.clickButton(self.button_acceptance_message)

    
    def select_tenant(self, tenant):
        self.globalFunction.selectValue(self.element_select_tenant, tenant)
    

    def get_order_number_from_url(self):
        return  (str(self.page.url)).split('/')[5]
    

    def get_pct_from_ui(self):
        try:
            u = self.page.locator("#pick-tickets").all_text_contents()
            v = u[0].split('\n')
            pct = v[4].replace(" ", "")
            pick_ticket = pct[17:]
        except:
            pick_ticket = "Not Found"

        return pick_ticket
    

    def save_data_attribute(self, file_data, field, value):
        file_data[field]=value
        with open('Data/data_localjson', 'w') as file:
            json.dump(file_data, file, indent=2)

 

    

    