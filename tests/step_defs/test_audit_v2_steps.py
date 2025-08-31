from playwright.sync_api import expect
from pytest_bdd import scenarios, then
from Base.global_functions import GlobalFunctions
from Base.common_functions import CommonFunctions
from Base.api_functions import ApiFunctions
from Base.celery_task_runner import run_celery_task
from Pages.audit_v2_page import AuditV2Page, AuditV2Details

import logging

logging.basicConfig(
     level=logging.INFO,
     format="%(asctime)s - %(levelname)s - %(message)s",
     handlers=[logging.StreamHandler()]
 )


scenarios('../features/audit_v2.feature')
delay = 0


@then('creates a Batch and assign it to a worker')
def step_then(set_up, data_load):
   page=set_up
   data=data_load
   
   gf = GlobalFunctions(page)
   cf = CommonFunctions(page)
   ap = AuditV2Page(page)
   apd = AuditV2Details(page)

   cf.select_tenant(data["child_tenant"])
   gf.secuential_navigation(cf.menu_wms, cf.menu_audit_v2)
   gf.selectSubMenu(cf.menu_audit_v2_batches)

   ap.click_create_batch_button()
   apd.select_facility(data["facility_code"])
   apd.select_count_mode(data["count_mode"])
   apd.check_freeze_inventory(data["freeze_inventory"])
   apd.input_instant_recount_attempts(data["instant_recount_attempts"])
   apd.check_select_all_location_types(data["select_all_location_types"])
   apd.select_limit_to_location_types(data["location_types"])
   apd.input_sku_codes_list(data["sku_code_list"])
   apd.input_sku_barcodes_list(data["sku_barcodes_list"])
   apd.input_location_barcode_range_start(data["location_barcode_start"])
   apd.input_location_barcode_range_end(data["location_barcode_end"])
   batch_id = apd.click_button_submit()
   ap.gf.search(ap.element_search_table, batch_id)
   result = ap.gf.validateText(ap.element_search_table, batch_id)
   print(f"EL RESULTADO DE SI LO ENCONTRO O NO ES {result}")
   
   
@then('the worker works the Batch')
def step_then(set_up, data_load):
   page=set_up
   data=data_load
   
   gf = GlobalFunctions(page)
   cf = CommonFunctions(page)
   ap = AuditV2Page(page)
   apd = AuditV2Details(page)

   cf.select_tenant(data["child_tenant"])
   gf.secuential_navigation(cf.menu_wms, cf.menu_audit_v2)
   gf.selectSubMenu(cf.menu_audit_v2_work)



@then('the worker post variances')
def step_then(set_up, data_load):
   pass

@then('creates a Batch with multiple active locations and assign it to the worker')
def step_then(set_up, data_load):
   page=set_up
   data=data_load
   
   gf = GlobalFunctions(page)
   cf = CommonFunctions(page)
   ap = AuditV2Page(page)
   apd = AuditV2Details(page)

   cf.select_tenant(data["child_tenant"])
   gf.secuential_navigation(cf.menu_wms, cf.menu_audit_v2)
   gf.selectSubMenu(cf.menu_audit_v2_batches)

   ap.click_create_batch_button()
   apd.select_facility(data["facility_code"])
   apd.select_limit_to_location_types("Active")
   apd.input_location_list(data["location_types"])
   batch_id = apd.click_button_submit()

   gf.search(ap.element_search_field, batch_id)   
   result = gf.validateText(ap.element_search_table, batch_id)
   if result:
      try:
         row = ap.element_search_table.locator(f"text={batch_id}").locator("xpath=ancestor::tr")
         checkbox = row.locator("input[type='checkbox']")
         expect(checkbox).to_be_visible()
         checkbox.click()
         logging.info(f"Checkbox asociado al valor '{batch_id}' fue seleccionado correctamente.")
      except Exception as e:
         logging.error(f"Error al intentar seleccionar el checkbox {e}")

   logging.info(f"result {result}")
   # Save the new Batch generated in the data file
   ap.cf.save_data_attribute(data, "ia_v2_batch", batch_id)

   ap.click_assign_batch_button()
   ap.select_worker("developer")
   ap.click_asign_worker_batch_button()
   