from Base.global_functions import GlobalFunctions
from Base.common_functions import CommonFunctions
from Base.api_functions import ApiFunctions
from Base.database_functions import DataBaseFunctions


class BaseWorkstationsPage:
    def __init__(self, page):
        self.page = page
        self.gf = GlobalFunctions(self.page)
        self.cf = CommonFunctions(self.page)
        self.af = ApiFunctions(self.page)
        self.dbf = DataBaseFunctions()

        self.element_table_workstations = self.page.locator("//table[@id='workstation-table']")
        self.element_button_new_workstation = self.page.locator("#new-workstation")
        self.element_select_facility = self.page.locator("#modal-workstation-form-facility-select")
        self.element_select_facility_search = self.page.locator("//input[@class='select2-search__field']")
        self.element_select_facility_results = self.page.locator(".select2-results")
        self.element_select_ws_type = self.page.locator("#modal-workstation-form-type-select")
        self.element_select_ws_type_search = self.page.locator("//input[@class='select2-search__field']")
        self.element_select_ws_type_results = self.page.locator(".select2-results")
        self.element_input_ip_address = self.page.locator("#ip_address")
        self.element_input_label_ip_address = self.page.locator("#label_address")
        self.element_input_label_port = self.page.locator("#label_port")
        self.element_input_customs_address = self.page.locator("#customs_address")
        self.element_input_customs_port = self.page.locator("#customs_port")
        self.element_input_reference = self.page.locator("#reference")
        self.element_select_is_active = self.page.locator("#is_active")
        self.element_input_attributes = self.page.locator("#attributes")
        self.element_input_paper_tray_tenants = self.page.locator("#paper_tray_tenants")
        self.element_input_paper_tray_media = self.page.locator("#paper_tray_media")
        self.element_button_save = self.page.locator("#save-workstation")


class WorkstationsPage(BaseWorkstationsPage):
    def __init__(self, page):
        super().__init__(page)
        
    def click_new_workstation_button(self):
        self.gf.validateToastHidden()
        self.gf.clickButton(self.element_button_new_workstation)

     
class WorkstationsDetails(BaseWorkstationsPage):
    def __init__(self, page):
        super().__init__(page)

    
    def select_facility_code(self, facility_code):
        #self.gf.select2Value(self.element_select_facility, self.element_select_facility_search,
        #                     self.element_select_facility_results, facility_code, facility_code )
        
        self.gf.select2Value_2(self.element_select_facility, self.element_select_facility_search,
                             self.element_select_facility_results, facility_code, facility_code )


    def select_workstation_type(self, workstation_type):
        #self.gf.select2Value(self.element_select_ws_type, self.element_select_ws_type_search,
        #                     self.element_select_ws_type_results, workstation_type, workstation_type )

        self.gf.select2Value_2(self.element_select_ws_type, self.element_select_ws_type_search,
                             self.element_select_ws_type_results, workstation_type, workstation_type )
         
        
    def input_ip_address(self, ip_address):
        #self.gf.writeText(self.element_input_ip_address, ip_address)
        self.gf.writeText_v2(self.element_input_ip_address, ip_address)


    def input_label_ip_address(self, label_ip_address):
        #self.gf.writeText(self.element_input_label_ip_address, label_ip_address)
        self.gf.writeText_v2(self.element_input_label_ip_address, label_ip_address)


    def input_label_port(self, label_port):
        #self.gf.writeText(self.element_input_label_port, label_port)
        self.gf.writeText_v2(self.element_input_label_port, label_port)


    def input_customs_ip_address(self, customs_ip_address):
        #self.gf.writeText(self.element_input_customs_address, customs_ip_address)
        self.gf.writeText_v2(self.element_input_customs_address, customs_ip_address)


    def input_customs_port(self, customs_port):
        #self.gf.writeText(self.element_input_customs_port, customs_port)
        self.gf.writeText_v2(self.element_input_customs_port, customs_port)


    def input_reference(self, reference):
        #self.gf.writeText(self.element_input_reference, reference)
        self.gf.writeText_v2(self.element_input_reference, reference)


    def select_is_active(self, is_active):
        #self.gf.selectValue(self.element_select_is_active, is_active)
        self.gf.selectValue_v2(self.element_select_is_active, is_active)


    def input_attributes(self, attributes):
        #self.gf.writeText(self.element_input_attributes, attributes)
        self.gf.writeText_v2(self.element_input_attributes, attributes)

    def input_paper_tray_tenants(self, papaer_tray_tenants):
        #self.gf.writeText(self.element_input_paper_tray_tenants, papaer_tray_tenants)
        self.gf.writeText_v2(self.element_input_paper_tray_tenants, papaer_tray_tenants)


    def input_paper_tray_media(self, paper_tray_media):
        #self.gf.writeText(self.element_input_paper_tray_media, paper_tray_media)
        self.gf.writeText_v2(self.element_input_paper_tray_media, paper_tray_media)

    def click_button_save(self):
        self.gf.clickButton(self.element_button_save)
        

     
     
