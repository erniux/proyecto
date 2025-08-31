from Base.global_functions import GlobalFunctions
from Base.common_functions import CommonFunctions
from Base.api_functions import ApiFunctions
from Base.database_functions import DataBaseFunctions


class BaseShipCodesPage:
    def __init__(self, page):
        self.page = page
        self.gf = GlobalFunctions(self.page)
        self.cf = CommonFunctions(self.page)
        self.af = ApiFunctions(self.page)
        self.dbf = DataBaseFunctions()

        self.element_ship_code_table = self.page.locator("#shipcode-table_grapper")
        self.element_button_new_ship_code = self.page.locator("//button[@type='button'][contains(.,'New')]")
        self.element_button_edit_ship_code = page.get_by_role("button", name="Edit")
        self.element_button_save = self.page.locator("#modal-shipcode-save")

        self.element_input_ship_code_description = self.page.locator("#description")
        self.element_input_ship_code = self.page.locator("#ship_code")
        self.element_input_fulfillment_ship_code = self.page.locator("#fulfillment_ship_code")
        self.element_input_custom_carrier_code = self.page.locator("#custom_carrier_code")
        self.element_select_is_rush = self.page.locator("#is_rush")
        self.element_select_is_pack_and_hold = self.page.locator("#pack_and_hold")
        self.element_select_exclude_return_labels = self.page.locator("#exclude_return_labels")
        self.element_input_dimensional_weight_factor = self.page.locator("#dim_factor")
        self.element_input_dimensional_wf_minimum_volume = self.page.locator("#dim_factor_minimum_volume")
        self.element_input_nqd = self.page.locator("#nqd_volume")
        self.element_select_block_translations_based_on_nqd_trigger = self.page.locator("#nqd_trigger")
        self.element_select_uses_combined_label_packing = self.page.locator("#uses_combined_label_and_ps")
        self.element_select_requires_lot_container = self.page.locator("#require_lot_container")


class ShipCodesPage(BaseShipCodesPage):
    def __init__(self, page):
        super().__init__(page)

    def click_new_ship_code_button(self):
        self.gf.clickButton(self.element_button_new_ship_code)

    def click_ship_code_link(self):
        self.gf.clickButton(self.element_button_edit_ship_code)


class ShipCodesDetails(BaseShipCodesPage):
    def __init__(self, page):
        super().__init__(page)


    def input_ship_code(self, code):
        self.gf.writeText_v2(self.element_input_ship_code, code)

    def input_ship_code_description(self, description):
        self.gf.writeText_v2(self.element_input_ship_code_description, description)

    def input_fulfillment_ship_code(self, value):
        self.gf.writeText_v2(self.element_input_fulfillment_ship_code, value)

    def input_custom_carrier_code(self, value):
        self.gf.writeText_v2(self.element_input_custom_carrier_code, value)

    def select_is_rush(self, value):
        self.gf.selectValue(self.element_select_is_rush, value)

    def select_is_pack_and_hold(self, value):
        self.gf.selectValue(self.element_select_is_pack_and_hold, value)

    def select_exclude_return_labels(self, value):
        self.gf.selectValue(self.element_select_exclude_return_labels, value)

    def input_dimensional_weight_factor(self, value):
        self.gf.writeText_v2(self.element_input_dimensional_weight_factor, value)

    def input_dimensional_wf_minimum_volume(self, value):
        self.gf.writeText_v2(self.element_input_dimensional_wf_minimum_volume, value)

    def input_nqd(self, value):
        self.gf.writeText_v2(self.element_input_nqd, value)

    def select_block_translations_base_on_nqd_trigger(self, value):
        self.gf.selectValue(self.element_select_block_translations_based_on_nqd_trigger, value)

    def select_uses_combined_label_packing(self, value):
        self.gf.selectValue(self.element_select_uses_combined_label_packing, value)

    def select_requires_lot_container(self, value):
        self.gf.selectValue(self.element_select_requires_lot_container, value)

    def click_button_save(self):
        self.gf.clickButton(self.element_button_save)     