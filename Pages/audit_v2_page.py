from Base.global_functions import GlobalFunctions
from Base.common_functions import CommonFunctions
from Base.api_functions import ApiFunctions
from Base.database_functions import DataBaseFunctions
from playwright.sync_api import expect

import logging

logging.basicConfig(
     level=logging.INFO,
     format="%(asctime)s - %(levelname)s - %(message)s",
     handlers=[logging.StreamHandler()]
 )


class BaseAuditV2Page:
    def __init__(self, page):
        self.page = page
        self.gf = GlobalFunctions(self.page)
        self.cf = CommonFunctions(self.page)
        self.af = ApiFunctions(self.page)
        self.dbf = DataBaseFunctions()

        self.element_button_create_batch = self.page.locator("#create-batch-btn")
        self.element_button_assign_batch = self.page.locator("#assign-batch-btn")
        self.element_search_table = self.page.locator("#DataTables_Table_0_wrapper")
        self.element_search_field = self.page.locator("#report-batch > form > div > div > div.form-group.ff > div > input")
        self.element_select_facility = self.page.locator("#bcFacility")
        self.element_select_count_mode = self.page.locator("bcCountMode")
        self.element_check_freeze_inventory = self.page.get_by_role("checkbox", name="freeze_inventory")
        self.element_input_instant_recount_attempts = self.page.locator("#bcInstantRecountAttempts")
        self.element_check_select_all_location_types =  self.page.locator('#all_location_types_checkbox')
        self.element_list_select_location_types = self.page.locator("#bcFilterLocationTypes")
        self.element_input_list_sku_codes = self.page.locator("#bcFilterParameterSkuCodes")
        self.element_input_list_sku_barcodes = self.page.locator("#bcFilterParameterSkuBarcodes")
        self.element_input_location_barcode_start = self.page.locator("#bcFilterParameterRangeStart")
        self.element_input_location_barcode_end = self.page.locator("#bcFilterParameterRangeEnd")
        self.element_input_location_list = self.page.locator("#bcFilterParameterLocationList")
        self.element_button_submit = self.page.locator('//*[@id="modal-batch-create"]/div/form/div/div[3]/button[2]')
        self.element_select_workers = self.page.locator('//*[@id="modal-batch-assign"]/div/form/div/div[2]/div[2]/span/span[1]/span/ul/li/input')
        self.element_select_workers_options = self.page.locator("#select2-baWorkers-results > li")
        self.element_button_assign_batch_submit = self.page.locator("#modal-batch-assign > div > form > div > div.modal-footer > button.btn.btn-primary")

        self.element_select_facility_work = self.page.locator("#panel-state-ready > form > div:nth-child(2) > select")
        self.element_button_begin_work = self.page.locator("#panel-state-ready > form > div.panel-footer > button")
        self.element_input_location_verify = self.page.locator("body > div.swal-overlay.swal-overlay--show-modal > div > div.swal-content > input")
        self.element_input_barcode = self.page.locator("#wtBarcode")
        self.element_button_count = self.page.locator('//*[@id="panel-work-task"]/div[2]/form/div/div/span/button')
        self.element_input_quantity_counted = self.page.locator('//*[@id="panel-work-task"]/table/tbody/tr/td[2]/input')
        self.element_button_complete = self.page.locator('//*[@id="panel-work-task"]/div[3]/button')


         

class AuditV2Page(BaseAuditV2Page):
    def __init__(self, page):
        super().__init__(page)
        
    def click_create_batch_button(self):
        self.gf.clickButton(self.element_button_create_batch)

    def click_assign_batch_button(self):
       self.gf.clickButton(self.element_button_assign_batch)

    def select_worker(self,value):
        self.element_select_workers.click()
        self.element_select_workers.fill(value)
        self.element_select_workers_options.click()
     
    def click_asign_worker_batch_button(self):
        self.gf.clickButton(self.element_button_assign_batch_submit)   
         

    def click_issue_recounts_button(self):
        pass

    def click_post_variances_button(self):
        pass

    def click_cancel_batch_button(self):
        pass

    def validate_batch_created(self, batch_number):
        self.gf.search(self.element_search_field, batch_number)
        result = self.gf.validateText(self.cf.data_table, batch_number)
        logging.info(f"resultado es {result}")

     
class AuditV2Details(BaseAuditV2Page):
    def __init__(self, page):
        super().__init__(page)

    
    def select_facility(self, facility_code):
        pass

    def select_count_mode(self, value):
        pass

    def check_freeze_inventory(self, value):
        pass

    def input_instant_recount_attempts(self, value):
        pass

    def check_select_all_location_types(self, value):
        self.gf.checkBox(self.element_check_select_all_location_types)

    def select_limit_to_location_types(self, value):
        self.gf.selectValue(self.element_list_select_location_types, value)

    def input_sku_codes_list(self, value):
        pass

    
    def input_sku_barcodes_list(self, value):
        pass

    def input_location_barcode_range_start(self, value):
        pass

    def input_location_barcode_range_end(self, value):
        pass

    def input_location_list(self, value):
        self.gf.writeText_v2(self.element_input_location_list, value)


    def click_button_submit(self):
        with self.page.expect_response(lambda resp: "api/v1/wms/inventory-audit/batch" in resp.url and resp.status == 201) as resp_info:
            self.gf.clickButton(self.element_button_submit)

        response = resp_info.value
        data = response.json()
        batch_id = data.get("batch_id")
        return batch_id