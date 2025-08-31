from Base.global_functions import GlobalFunctions
from Base.common_functions import CommonFunctions
from Base.api_functions import ApiFunctions
from Base.database_functions import DataBaseFunctions


class BaseAllocationRulesPage:
    def __init__(self, page):
        self.page = page
        self.gf = GlobalFunctions(self.page)
        self.cf = CommonFunctions(self.page)
        self.af = ApiFunctions(self.page)
        self.dbf = DataBaseFunctions()

        self.avaliable_allocation_rules = self.page.locator("#sortable1")
        self.assigned_allocation_rules = self.page.locator("#sortable2" )
        self.allocation_rule1 = "//strong[contains(.,'"
        self.allocation_rule2 = "')]"
        
       
        
#sortable1 > li:nth-child(2)
class AllocationRulesPage(BaseAllocationRulesPage):
    def __init__(self, page):
        super().__init__(page)
        
 