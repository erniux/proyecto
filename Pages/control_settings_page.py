from Base.global_functions import GlobalFunctions
from Base.common_functions import CommonFunctions
from Base.api_functions import ApiFunctions
from Base.database_functions import DataBaseFunctions


class BaseControlSettingsPage:
    def __init__(self, page):
        self.page = page
        self.gf = GlobalFunctions(self.page)
        self.cf = CommonFunctions(self.page)
        self.af = ApiFunctions(self.page)
        self.dbf = DataBaseFunctions()

        self.element_check_setting1 = "//input[@type='checkbox'])["
        self.element_check_setting1 = "]"
        self.element_button_save = self.page.locator("//button[@id='save-control-settings']")


class ControlSettingsPage(BaseControlSettingsPage):
    def __init__(self, page):
        super().__init__(page)
        

    def check_setting(self, index):
        try:
            self.gf.checkBox(f"(//input[@type='checkbox'])[{index}]")
        except:
            pass

    def save_settings(self):
        self.gf.clickButton(self.element_button_save)
