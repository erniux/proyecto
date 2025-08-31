from Base.global_functions import GlobalFunctions
from Base.common_functions import CommonFunctions
from Base.api_functions import ApiFunctions
from Base.database_functions import DataBaseFunctions

 

class SystemShippingPage:
    def __init__(self, page):
        self.page = page
        self.gf = GlobalFunctions(self.page)
        self.cf = CommonFunctions(self.page)
        self.af = ApiFunctions(self.page)
        self.dbf = DataBaseFunctions()


#class SystemShippingPage(SystemShippingPage):
#    def __init__(self, page, data):
#        super().__init__(page)
        #self.data = data
        
        #Menus
        self.menu_system = "System"
        self.menu_system_shipping = "Shipping"
        self.menu_carriers = "Carriers"
        self.menu_cons_address = ""
        self.menu_disposition_codes = ""
        self.menu_flat_rate_shipping = ""
        self.menu_fright_rate = ""
        self.menu_holidays = ""
        self.menu_ship_codes = "Ship Codes"
        self.menu_translations = ""

        self.new_order_buton="//button[contains(.,'New Order')]"
