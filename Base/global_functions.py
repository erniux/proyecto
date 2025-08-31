import re
from socket import timeout
from tabnanny import check
import time
from playwright.sync_api import expect, sync_playwright
import logging
from difflib import get_close_matches

logging.basicConfig(
     level=logging.INFO,
     format="%(asctime)s - %(levelname)s - %(message)s",
     handlers=[logging.StreamHandler()]
 )


class GlobalFunctions:
    
    def __init__(self, page):
        self.page = page

    
    def Wait(self, delay):
        time.sleep(delay)


    def writeText(self, element, value):
        self.page.wait_for_selector(element)
        text = self.page.locator(element)
        expect(text).to_be_visible()
        expect(text).to_be_enabled()
        #expect(text).to_be_empty()
        text.highlight()
        text.fill(value)

    def writeText_v2(self, element, value):
        #logging.info(f"ya dentro del write_textv2 con el value == {value}")
        expect(element).to_be_visible()
        expect(element).to_be_enabled()
        element.highlight()
        element.fill(value)
    

    def keyboardType(self, element, value):
        text = element
        expect(text).to_be_visible()
        expect(text).to_be_enabled()
        text.highlight()
        text.press_sequentially(value)


    def saveScreenShot(self, path):
        self.page.screenshot(path=path)
         

    def clickLink(self, element):
        if isinstance(element, str):
            link = self.page.locator(element)
        else:
            link = element
            
        #link.scroll_into_view_if_needed()
        expect(link).to_be_visible()
        expect(link).to_be_enabled()
        link.highlight()
        link.click()
        self.page.wait_for_load_state()
    

    def dragAndDrop(self, drag_element, drop_element, delay):
        rule = self.page.locator(drag_element)
        rule.drag_to(drop_element)
        self.Wait(2)


    def clickButton(self, element):
        self.validateToastHidden()
        
        if isinstance(element, str):
            button = self.page.locator(element)
        else:
            button = element

         
        expect(button).to_be_visible()
        expect(button).to_be_enabled()

        if button.count() == 0:
            raise Exception(f"El botón {element} no existe en la página.")

        button.highlight()
        button.click()

        self.page.wait_for_load_state()


    def clickTab(self, element):
        tab =element
        expect(tab).to_be_visible()
        expect(tab).to_be_enabled()
        tab.highlight()
        tab.click()
        self.page.wait_for_load_state()


    def clickEnter(self, element, sku):
        self.page.keyboard.press("Enter")
        expect(element).to_be_visible()
        #expect(element).to_contain_text(sku)
        self.page.wait_for_load_state()


    def search(self, element, value):
        if isinstance(element, str):
            search_element = self.page.locator(element)
        else:
            search_element = element

        expect(search_element).to_be_visible()
        search_element.fill(str(value))
        self.page.keyboard.press("Enter")
        self.page.wait_for_load_state()


    def HumanSearch(self, text, delay):
        self.page.keyboard.press("Tab")
        self.page.keyboard.press("Tab")
        self.page.keyboard.press("Enter")
        self.page.keyboard.insert_text(text)
        self.Wait(delay)
        self.page.keyboard.press("Enter")
        self.Wait(delay)
        self.page.wait_for_load_state()


    def selectValue(self, element, value):
        if isinstance(element, str):
            select = self.page.locator(element)
        else:
            select = element
        
        expect(select).to_be_visible()
        
        select.highlight()
        select.select_option(value)
        self.page.wait_for_load_state()
    

    def selectValue_v2(self,element,value):
        not_found = []
        expect(element).to_be_visible()
        
        results = element.all_text_contents()
        for r in results:
            #logging.info(f"first result is {r}")
            if value in r:
                element.wait_for()
                expect(element.locator(f"text={r.strip()}")).to_be_visible()
                element.locator(f"text={r.strip()}").click()
                break
            else:
                not_found.append(value)
        self.page.wait_for_load_state()
        return not_found                 
        

    def checkBox(self, element):
        if isinstance(element, str):
            checkbox = self.page.locator(element)
        else:
            checkbox = element
        
        expect(checkbox).to_be_visible()

        if not checkbox.is_checked():
            checkbox.check()
         
    
    def selectCalendar(self, element, date, delay=0.5):
        calendar = element
        calendar.click()
        calendar.fill(date)
        self.page.keyboard.press("Enter")
        self.page.wait_for_load_state()
        
        #year, month, day = date.split("-")
        # 
        #self.page.get_by_role("cell", name="March 2024 Toggle Date and").click()
        #self.page.get_by_role("cell", name="Toggle Date and Time Screens").click()
        #self.page.get_by_text(year, exact=True).click()
        #self.page.get_by_text("Dec").click()
        #self.page.get_by_role("cell", name=day).click()
        #self.page.keyboard.press("Enter")
         

    def select2Value(self, element, element_search, element_results, value, result, delay=0.5):
        select2 = element
        expect(select2).to_be_visible
        element.click()
        element_search.fill(value) 
        expect(element_results).to_be_visible
        expect(element_results).to_contain_text(result)
        element_results.click()
        self.Wait(delay)


    def select2Value_2(self, element, element_search, element_results, value, result, delay=0.5):
        expect(element).to_be_visible()
        element.highlight()
        element.click()
        self.Wait(delay)
        if not element_search.is_visible():
            element.click()

        element_search.fill(value)
        self.Wait(delay)
        element_search.highlight()
        expect(element_results).to_be_visible
         
        options = self.page.locator("li.select2-results__option")
        option_count = options.count()

        if option_count == 0:
            logging.info("No options found for {value} :: {result}.")
            return

        option_texts = [options.nth(i).inner_text().strip() for i in range(option_count)]
        closest_match = get_close_matches(result, option_texts, n=1, cutoff=0.5)

        if closest_match:
            closest_index = option_texts.index(closest_match[0])
            options.nth(closest_index).click()
        else:
            self.page.get_by_text(result).first.click()
   
        self.Wait(delay)


    def multiSelectValue(self,element,value, result):
        multi_select = element
        expect(multi_select).to_be_visible()
        multi_select.highlight()
        multi_select.fill(value)

        results = self.page.get_by_role("treeitem", name=result)
        expect(results).to_be_visible()
        results.click()
         
       
    def selectMenu(self, value): 
        self.Wait(1) 
        menu = self.page.get_by_role("link", name=value).first
        expect(menu).to_be_visible()
        menu.highlight()
        menu.click()
        
    
    def selectSubMenu(self, element):
        self.Wait(1)
        menu = self.page.locator(element)
        expect(menu).to_be_visible()
        menu.highlight()
        menu.click()


    def secuential_navigation(self, *args):
        for menu in args:
            self.selectMenu(menu)
           

    def validatePageName(self, value):
        expect(self.page).to_have_title(value)


    def validatePageUrl(self, value):
        expect(self.page).to_have_url(re.compile(value))


    def validateText(self, element, value):
        #self.page.pause()
        if isinstance(element, str):
            t = self.page.locator(element)
        else:
            t = element
            
        try:
            found = t.locator(f"//td[contains(text(), '{value}')] | //th[contains(text(), '{value}')]")
            return found.first.is_visible()

        except Exception as e:
            print(f"Error al buscar el valor en la tabla: {e}")
            return False
        
        
    def goToUrl(self, url):
        self.page.goto(''+ url)
        self.page.wait_for_load_state()


    def validateToast(self, message):
        try:
            expect(self.page.get_by_text(message)).to_be_visible()
            return True
        except:
            expect(self.page.get_by_text(message).first).to_be_visible()
            return True
        else:
            return False
        

    def  validateToastHidden(self,timeout=5000):
        #toastr = self.page.locator("#toast-container")
#
        #toasts = toastr.all()  # Lista de todos los toastrs
#
        #logging.info(f'TOTAL TOASTS ABIERTOS: {len(toasts)}')
#
        #if len(toasts) > 0:
        #    for toast in toasts:
        #        try:
        #            expect(toast).to_be_hidden(timeout=5000)  # Espera hasta 5s para que se oculte
        #        except:
        #            logging.warning("❌ Un toastr sigue visible.")
        #            return False  # Si al menos uno sigue visible, retorna False
#
        #logging.info("✅ Todos los toastrs desaparecieron.")
        #return True  # Solo retorna True si todos están ocultos

        timeout = int(timeout)
        start_time = time.time()
        toastr = self.page.locator("#toast-container")

        while time.time() - start_time < timeout / 1000:
            if toastr.count() == 0 or all(toast.is_hidden() for toast in toastr.all()):
                logging.info("✅ Todos los toastrs desaparecieron.")
                return True  # Si no hay toastrs o están ocultos, retorna True
            
            time.sleep(0.2)  # Espera 200ms antes de verificar nuevamente

        logging.warning("❌ Hay toastrs visibles después del tiempo de espera.")
        return False  # Si sigue habiendo toastrs visibles, retorna False