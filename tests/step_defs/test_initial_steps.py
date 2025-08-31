from playwright.sync_api import expect
from pytest_bdd import scenarios, then
from Pages.inventory_transaction_reasons_page import InventoryTransactionsDetails, InventoryTransactionsPage 
from Pages.tenant_page import TenantPage, TenantDetails
from Pages.system_page import SystemPage
from Pages.facility_page import FacilityPage, FacilityDetails
from Pages.user_page import UserPage, UserDetails
from Pages.control_settings_page import ControlSettingsPage
from Pages.business_type_page import BusinessTypePage, BusinessTypeDetails
from Pages.allocation_rules_page import AllocationRulesPage
from Pages.offers_page import OffersPage, OffersDetails
from Pages.workstations_page import WorkstationsPage, WorkstationsDetails
from Pages.appeasements_page import AppeasementPage, AppeasementDetails
from Pages.sources_page import SourcesPage, SourcesDetails
from Pages.cancel_reasons_page import CancelReasonsPage, CancelReasonsDetails
from Pages.exception_reasons_page import ExceptionReasonsPage, ExceptionReasonsDetails
from Pages.exception_resolution_reasons_page import ExceptionResolutionReasonsPage, ExceptionResolutionReasonsDetails 
from Pages.hold_reasons_page import HoldReasonPage, HoldReasonDetails
from Pages.carriers_page import CarriersPage, CarriersDetails
from Pages.ship_codes_page import ShipCodesPage, ShipCodesDetails
from Pages.disposition_codes_page import DispositionCodesPage, DispositionCodesDetails
from Pages.override_reasons_page import OverrideReasonsPage, OverrideReasonsDetails
from Pages.flat_rates_page import FlatRatesPage, FlatRatesDetails
from Pages.card_payments_page import CardPaymentsPage, CardPaymentsDetails
from Pages.locations_page import LocationsPage, LocationsDetails
from Pages.shipping_carts_page import CartsPage, CartsDetails
from Pages.items_page import ItemsPage, ItemsDetails, SkuDetails
from Pages.putaway_page import PutawayActivePage, PutawayOtherPage
from Pages.receiving_standard_page import ReceivingStandardPage
import time

import logging

scenarios('../features/initial.feature')
delay = 0

logging.basicConfig(
     level=logging.INFO,
     format="%(asctime)s - %(levelname)s - %(message)s",
     handlers=[logging.StreamHandler()]
 )

@then('creates a Tenant')
def create_tenant(set_up,data_load) :
    page=set_up
    data=data_load

    tp = TenantPage(page)
    tdp = TenantDetails(page)
    
    tp.cf.select_tenant(data["parent_tenant"]) 
    tp.gf.secuential_navigation(tp.cf.menu_system, tp.cf.menu_tenants)
    tp.gf.search(tp.cf.input_search, data["child_new_tenant"])
    result = tp.gf.validateText(tp.cf.data_table, data["child_new_tenant"])
    if not result:
        tp.click_new_tenant_button()
        tdp.input_tenant_name(data["child_new_tenant"])
        tdp.input_tenant_code(data["tenant_new_code"])
        tdp.select_tenant_role(data["tenant_new_role"])
        tdp.select_time_zone(data["time_zone"])
        tdp.click_button_save()
        #gf.validateToast(tp.element_toastr_save_success)
        tp.gf.validatePageName(f'Tenant \"{data["child_new_tenant"]}\" — Jazz Central')
        tp.gf.validatePageUrl(data["base_url"] + "system/view-tenant/" + data["tenant_new_code"])
        print(f'tenant {data["child_new_tenant"]} created!')

    else:
        print(f'tenant {data["child_new_tenant"]} already exists')


@then('creates a facility')
def create_facility(set_up,data_load) :
    page=set_up
    data=data_load
    
    fp = FacilityPage(page)
    fdp = FacilityDetails(page)


    fp.cf.select_tenant(data["parent_tenant"]) 
    fp.gf.secuential_navigation(fp.cf.menu_system, fp.cf.menu_facilities)

    fp.gf.search(fp.cf.input_search, data["facility_code"])
    result = fp.gf.validateText(fp.cf.data_table, data["facility_code"])

    if not result:
        #fp.page.pause()
        fp.click_new_facility_button()
        fdp.input_facility_code(data["facility_code"])
        fdp.input_facility_name(data["facility_name"])
        fdp.select_work_flow(data["workflow_type"])
        fdp.select_time_zone(data["time_zone"])
        fdp.input_director_name(data["director_name"])
        fdp.input_address1(data["address1"])
        fdp.input_address2(data["address2"])
        fdp.input_zipcode(data["zipcode"])
        fdp.input_phone_number(data["phone_number"])
        fdp.check_facility_days(data["facility_days"])
        fdp.select_facility_active(data["facility_active"])
        fdp.select_pctl_generation(data["pick_ticket_generation"])
        fdp.select_enable_allocation(data["enable_alocation"])
        fdp.input_carts_before_batch(data["carts_before_batch"])
        fdp.click_save_facility()

        #fp.gf.validateToast(tp.element_toastr_save_success)
        #fp.gf.validatePageName(f'Facility Details — Jazz Central')
        #fp.gf.validatePageUrl(data["base_url"] + "system/view-facility/" + data["facility_code"])
        print(f"Facility {data["facility_code"]} created")
    else:
        print(f"Facility {data["facility_code"]} already exists")
  

@then('adds facility to user profile')
def add_facility_to_user(set_up,data_load) :
    page=set_up
    data = data_load

    up = UserPage(page)
    udp = UserDetails(page)
    page.pause()
    up.cf.select_tenant(data["parent_tenant"]) 
    up.gf.secuential_navigation(up.cf.menu_system, up.cf.menu_users_groups)
    up.gf.selectSubMenu(up.cf.menu_users)

    #page.pause()
    up.gf.search(up.cf.input_search, data["user_name"])
    result = up.gf.validateText(up.cf.data_table, data["user_name"])

    
    if not result:
        print(f'facility {data["facility_code"]} user not found')
    else:
        up.click_edit_user_link()
        udp.input_user_first_name(data["first_name"])
        udp.input_user_last_name(data["last_name"])
        udp.input_facility_to_user(data["facility_code"])
        udp.select_time_zone(data["time_zone"])
        #page.pause()
        udp.click_button_save()
        #up.gf.validateToast(tp.element_toastr_save_success)
        print(f'facility {data["facility_code"]} added to user {data["user_name"]}')
     

@then('adds facility to Tenant')
def add_facility_to_tenant(set_up, data_load) :
    page=set_up
    data=data_load

    tp = TenantPage(page)
    tdp = TenantDetails(page)

    tp.cf.select_tenant(data["parent_tenant"]) 
    tp.gf.secuential_navigation(tp.cf.menu_system, tp.cf.menu_tenants)

    tp.gf.search(tp.cf.input_search, data["tenant_code"])
    result = tp.gf.validateText(tp.cf.data_table, data["tenant_code"])
    
    print(f'result de la busqueda es {result}')
    if not result:
        print(f'Tenant {data["tenant_code"]} does not exists.')
    else:
        tp.click_link_tenant(data["tenant_code"])
        tdp.check_facility_code(data["facility_code"])
        tdp.click_button_save()
        print(f'Facility {data["facility_code"]} assigned to Tenant {data["tenant_code"]}')
        #tp.gf.validateToast(tp.element_toastr_save_success)


@then('setups control settings')
def setup_control_settings(set_up,data_load ) :
    page=set_up
    data=data_load
    
    csp = ControlSettingsPage(page)
     
    child_list = []
    parent_list = []

    for index, (key, value) in enumerate(data['control_settings'][0].items()):
        if value[3] == 'child':
            child_list.append((index, key, value))  # child tenant control settings
        elif value[3] == 'parent':
            parent_list.append((index, key, value))  # parent tenant control settings

    csp.cf.select_tenant(data["parent_tenant"]) 
    csp.gf.secuential_navigation(csp.cf.menu_system, csp.cf.menu_control_setings)

    for item in parent_list:
        if item[2][2]:
            csp.check_setting(item[0] + 2)
            
    csp.save_settings()
    #sp.gf.validateToast(tp.element_toastr_save_success)

    csp.cf.select_tenant(data["child_tenant"]) 
    csp.gf.secuential_navigation(csp.cf.menu_system, csp.cf.menu_client_setup, csp.cf.menu_control_setings)
    
    for item in child_list:
        if item[2][2]:
            csp.check_setting(item[0] + 2)
            
    csp.save_settings()
    #csp.gf.validateToast(tp.element_toastr_save_success)

 
@then('creates business types')
def create_business_types(set_up, data_load ) :
    page=set_up
    data = data_load

    btp = BusinessTypePage(page)
    btdp = BusinessTypeDetails(page)

    btp.cf.select_tenant(data["child_tenant"]) 
    btp.gf.secuential_navigation(btp.cf.menu_system, btp.cf.menu_client_setup, btp.cf.menu_business_types)

    btp.gf.search(btp.cf.input_search, data["business_type_code"])
    result = btp.gf.validateText(btp.element_business_type_table, data["business_type_code"])

    if not result:
        btp.click_new_business_type_button()
        btdp.input_business_type_code(data["business_type_code"])
        btdp.input_business_type_description(data["business_type_code"])
        btdp.select_maitain_inventory(data["maitain_inventory"])
        btdp.select_billing_type(data["billing_type"])
        btdp.input_inventory_priority(data["inventory_priority"])
        btdp.button_save()
        #btp.gf.validateToast(tp.element_toastr_save_success)
        btp.gf.search(btp.cf.input_search, data["business_type_code"])
        result = btp.gf.validateText(btp.element_business_type_table, data["business_type_code"])
        if result:
            print(f'Business Type {data["business_type_code"]} created')
    else:
        print(f'Business Type {data["business_type_code"]} already exists')


@then('adds default allocation rules')
def adds_allocation_rules(set_up,data_load):
    page=set_up
    data=data_load

    ap = AllocationRulesPage(page)

    ap.cf.select_tenant(data["child_tenant"]) 
    ap.gf.secuential_navigation(ap.cf.menu_system, ap.cf.menu_client_setup, ap.cf.menu_allocation)

    result = ap.gf.validateText(ap.assigned_allocation_rules, data["allocation_rule"])
    
    if not result:
        drag_element = ap.allocation_rule1 + data["allocation_rule"] + ap.allocation_rule2
        ap.gf.dragAndDrop(drag_element, ap.assigned_allocation_rules, 2 )   
    else:
        print(f'allocation Rule {data["allocation_rule"]} already assigned to tenant')


@then('creates offers')
def create_offers(set_up, data_load) :
    page=set_up
    data=data_load
    
    op = OffersPage(page)
    odp = OffersDetails(page)

    op.cf.select_tenant(data["child_tenant"]) 
    op.gf.secuential_navigation(op.cf.menu_system, op.cf.menu_client_setup, op.cf.menu_offers)

    op.gf.search(op.cf.input_search, data["offer_code"])
    result = op.gf.validateText(op.cf.data_table, data["offer_code"] )

    if not result:
        op.click_new_offer_button()
        odp.input_offer_code(data["offer_code"])
        odp.input_offer_description(data["offer_code"])
        odp.select_offer_business_type(data["business_type_code"])
        odp.select_calendar_end_date("2024")
        odp.select_input_offer_year("2024")
        odp.button_save()

        op.gf.search(op.cf.input_search, data["offer_code"])
        result2 = op.gf.validateText(op.cf.data_table, data["offer_code"] )
        if result2:
            print(f'Offer {data["offer_code"]} created')
    else:
        print(f'Offer {data["offer_code"]} was already created')

    
@then('creates sources')
def create_sources(set_up,data_load):
    page=set_up
    data=data_load

    sop = SourcesPage(page)
    sodp = SourcesDetails(page)

    sop.cf.select_tenant(data["child_tenant"]) 
    sop.gf.secuential_navigation(sop.cf.menu_system, sop.cf.menu_client_setup, sop.cf.menu_sources)

    sop.gf.search(sop.cf.input_search, data["source_code"])
    result = sop.gf.validateText(sop.cf.data_table, data["source_code"])

    if not result:
        sop.click_new_source_button()
        sodp.input_source_code(data["source_code"])
        sodp.input_source_description(data["source_code"])
        sodp.select_offer(data["offer_code"])
        sodp.select_is_active("Yes")
        sodp.select_start_promotion("2024-03-01")
        sodp.select_end_promotion("2099-12-31")
        sodp.input_promotion_price("0.05")
        sodp.select_billing_type(data["billing_type"])
        sodp.select_allocation_facility(data["allocation_facility"])
        sodp.click_button_save()

        
    else:
        print("Source already created")
    

@then('creates carriers')
def creates_carriers(set_up,data_load) :
    page=set_up
    data=data_load
     
    cp = CarriersPage(page)
    cdp = CarriersDetails(page)

    cp.cf.select_tenant(data["child_tenant"]) 
    #gf.selectValue('#view-as-tenant-select',data["child_tenant"], delay)

    cp.gf.secuential_navigation(cp.cf.menu_system, cp.cf.menu_shipping, 
                                cp.cf.menu_carriers)

    cp.gf.search(cp.cf.input_search, data["carrier_code"])
    result = cp.gf.validateText(cp.element_carrier_table, data["source_code"])

    if not result:
        cp.click_new_carrier_button()
        cdp.select_carrier(data["carrier_code"])
        cdp.input_carrier_name(data["carrier_code"])
        cdp.select_carrier_status("Enabled")
        cdp.click_button_save()
        print(f'carrier {data["carrier_code"]} created.')
    else:
        print(f'carrier {data["carrier_code"]} already exists.')


@then('creates ship codes')
def creates_ship_codes(set_up,data_load):
    page=set_up
    data=data_load

    scp = ShipCodesPage(page)
    scdp = ShipCodesDetails(page)

    scp.cf.select_tenant(data["child_tenant"])
    scp.gf.secuential_navigation(scp.cf.menu_system, scp.cf.menu_shipping, scp.cf.menu_shipcodes)

    for s in data["ship_code"]:
        scp.gf.search(scp.cf.input_search, s)
        index = data["ship_code"].index(s)
        result = scp.gf.validateText(scp.cf.data_table, s)

        if not result:
            scp.click_new_ship_code_button()
            #scdp.page.pause()
            scdp.input_ship_code(s)
            scdp.input_ship_code_description(data["ship_code_description"][index])
            scdp.input_fulfillment_ship_code(s)
            scdp.input_custom_carrier_code(s)
            scdp.select_is_rush("No")
            scdp.select_is_pack_and_hold("No")
            scdp.select_exclude_return_labels("No")
            scdp.input_dimensional_weight_factor("0")
            scdp.input_dimensional_wf_minimum_volume("0")
            scdp.input_nqd("0")
            scdp.select_block_translations_base_on_nqd_trigger("No")
            scdp.select_requires_lot_container("No")
            scdp.select_uses_combined_label_packing("No")
            scdp.click_button_save()
        else:
            continue


@then('adds shipping method and cartons to facility')
def adds_shipping_methods_and_cartons_to_facility(set_up, data_load):
    page=set_up
    data = data_load

    fp = FacilityPage(page)
    fdp = FacilityDetails(page)

    fp.cf.select_tenant(data["child_tenant"])
    fp.gf.secuential_navigation(fp.cf.menu_system, fp.cf.menu_facilities)
    fp.gf.search(fp.cf.input_search, data["facility_code"])
    result = fp.gf.validateText(fp.cf.data_table, data["facility_code"])

    if result:
        fp.click_faciliy_link(data["facility_code"])
        fdp.select_shipcode_status("Enabled")
        fdp.select_carton_status("Enabled")
        fdp.click_edit_facility()
        
        #expect(page.get_by_text("Saving...").first).to_be_visible()
        #expect(page.get_by_text("Saved Successfully!")).to_be_visible()
    

@then('adds inventory transaction reasons')
def adds_inventory_transaction_reasons(set_up, data_load) :
    page=set_up
    data=data_load

    itrp = InventoryTransactionsPage(page)
    itrdp = InventoryTransactionsDetails(page)
    
    itrp.cf.select_tenant(data["child_tenant"])
    itrp.gf.secuential_navigation(itrp.cf.menu_system, itrp.cf.menu_client_setup, 
                                  itrp.cf.menu_inventory_transaction_reasons)
    
    for r in data["transaction_reasons"]:
        itrp.gf.search(itrp.cf.input_search, r)
        result = itrp.gf.validateText(itrp.cf.data_table, r)
        
        if not result:
            itrp.click_new_button()
            itrdp.input_transaction_reason_code(r)
            itrdp.input_transaction_reason_desc(r)
            itrdp.select_transaction_type(r)
            itrdp.select_status("Enabled")
            itrdp.click_button_save()
        else:
            continue


@then('creates exception reasons')
def step_the(set_up, data_load):
    page=set_up
    data=data_load

    erp = ExceptionReasonsPage(page)
    erdp = ExceptionReasonsDetails(page)

    erp.cf.select_tenant(data["child_tenant"]) 
    erp.gf.secuential_navigation(erp.cf.menu_system, erp.cf.menu_client_setup, erp.cf.menu_exception_reasons)

    for e in data["exception_reasons"]:
        erp.gf.search(erp.cf.input_search, e)
        index = data["exception_reasons"].index(e)
        result = erp.gf.validateText(erp.cf.data_table, e)

        if not result:
            erp.click_new_button()
            erdp.input_exception_reason_code(e)
            erdp.input_exception_reason_description(data["exception_reason_desc"][index])
            erdp.click_button_save()
            print(f"exception reason {e} created")
        else:
            print(f"exception reason {e}  already exists")

        #page.wait_for_load_satate()

@then('creates cancelation reasons')
def step_then(set_up, data_load):
    page=set_up
    data=data_load

    crp = CancelReasonsPage(page)
    crdp = CancelReasonsDetails(page)

    crp.cf.select_tenant(data["child_tenant"]) 
    crp.gf.secuential_navigation(crp.cf.menu_system, crp.cf.menu_client_setup, 
                                 crp.cf.menu_cancel_reasons)



    for c in data["cancelation_reasons_code"]:
        crp.gf.search(crp.cf.input_search, c)
        index = data["cancelation_reasons_code"].index(c)
        result = crp.gf.validateText(crp.cf.data_table, c)
        if not result:
            crp.click_new_button()
            crdp.input_cancel_reason_code(c)
            crdp.input_cancel_reason_description(data["cancelation_reasons_desc"][index])
            #crdp.input_warehouse_service_failure("False")
            crdp.click_button_save()


@then('creates exception resolution reasons')
def step_then(set_up, data_load):
    page=set_up
    data=data_load

    errp = ExceptionResolutionReasonsPage(page)
    errdp = ExceptionResolutionReasonsDetails(page)


    errp.cf.select_tenant(data["child_tenant"]) 
    errp.gf.secuential_navigation(errp.cf.menu_system, errp.cf.menu_client_setup, 
                                  errp.cf.menu_exception_resolution_reasons)

    for r in data["resoulution_reasons_code"]:
        errp.gf.search(errp.cf.input_search, r)
        index = data["resoulution_reasons_code"].index(r)
        result = errp.gf.validateText(errp.cf.data_table, r)
    
        if not result:
            errp.click_new_button()
            errdp.input_exception_reason_code(r)
            errdp.input_exception_reason_description(data["resolution_reasons_desc"][index])
            #errdp.select_exception_resoulution_reason_status("Enabled")
            errdp.click_button_save()

            print(f'Exception resolution reason code {r} created')
        else:
            print(f'Exception resolution reason code {r} already exisits')


@then('creates Appeasement types')
def then_step(set_up, data_load):
    page=set_up
    data=data_load

    ap = AppeasementPage(page)
    adp = AppeasementDetails(page)

    ap.cf.select_tenant(data["child_tenant"]) 
    ap.gf.secuential_navigation(ap.cf.menu_system, ap.cf. menu_client_setup,
                                ap.cf.menu_appeasements)

    for a in data["appeasement_type_code"]:
        ap.gf.search(ap.cf.input_search, a)
        result = ap.gf.validateText(ap.cf.data_table, a)
        index = data["appeasement_type_code"].index(a)
        if not result: 
            ap.click_new_appeasement_button()
            adp.input_appeasement_type_code(a)
            adp.input_appeasement_description(data["appeasement_type_desc"][index])
            adp.select_credit_or_debit(data["appeasement_type"][index])
            adp.select_is_active("Yes")
            adp.select_is_actionable("No")
            adp.click_button_save()

            expect(page.get_by_text("Saved Successfully!").first).to_be_visible()
            print(f'Exception reason code {a} created')
        else:
            print(f'Exception reason code {a} already exisits')


@then('creates hold reasons')
def then_step(set_up, data_load):
    page=set_up
    data=data_load

    hrp = HoldReasonPage(page)
    hrdp = HoldReasonDetails(page)

    hrp.cf.select_tenant(data["child_tenant"]) 
    hrp.gf.secuential_navigation(hrp.cf.menu_system, hrp.cf.menu_client_setup, 
                                 hrp.cf.menu_hold_reasons)

    for h in data["hold_reasons_code"]:
        hrp.gf.search(hrp.cf.input_search, h)
        index = data["hold_reasons_code"].index(h)
        result = hrp.gf.validateText(hrp.element_table_hold_reasons, h)
        if not result:
            hrp.click_new_hold_button()
            hrdp.input_hold_reason_code(h)
            hrdp.input_hold_reason_description(data["hold_reasons_desc"][index])
            hrdp.click_button_save()
            print(f"hold reason {h} created")
        else:
            print(f"hold reason {h} already exists")


@then('creates disposition codes')
def then_step(set_up, data_load):
    page=set_up
    data=data_load
    
    dcp = DispositionCodesPage(page)
    dcdp = DispositionCodesDetails(page)

    dcp.cf.select_tenant(data["child_tenant"]) 
    dcp.gf.secuential_navigation(dcp.cf.menu_system, dcp.cf.menu_shipping, 
                                 dcp.cf.menu_disposition_codes)

    for d in data["disposition_codes"]:
        dcp.gf.search(dcp.cf.input_search, d)
        index = data["disposition_codes"].index(d)
        result = dcp.gf.validateText(dcp.cf.data_table, d)
        
        if not result:
            dcp.click_new_button()
            dcdp.input_disposition_code(d)
            dcdp.input_disposition_description(data["disposition_codes_desc"][index])
            dcdp.click_button_save()
            print(f'Hold reason code {d} created')
        else:
            print(f'Hold reason code {d} already exisits')


@then('creates override reasons')
def then_step(set_up, data_load):
    page=set_up
    data=data_load

    orp = OverrideReasonsPage(page)
    ordp = OverrideReasonsDetails(page)

    orp.cf.select_tenant(data["child_tenant"]) 
    orp.gf.secuential_navigation(orp.cf.menu_system, orp.cf.menu_client_setup, 
                                 orp.cf.menu_override_reasons)

    for o in data["override_reason_code"]:
        orp.gf.search(orp.cf.input_search, o)
        index = data["override_reason_code"].index(o)
        result = orp.gf.validateText(orp.cf.data_table, o)
        
        if not result: 
            orp.click_new_override_button()
            ordp.input_override_type_code(o)
            ordp.input_override_description(data["override_reason_desc"][index])
            ordp.click_button_save()
            print(f'Hold reason code {o} created')
        else:
            print(f'Hold reason code {o} already exisits')


@then('adds flat rates')
def step_then(set_up,data_load ) :
    page=set_up
    data=data_load

    frp = FlatRatesPage(page)
    frdp = FlatRatesDetails(page)

    frp.cf.select_tenant(data["child_tenant"]) 
    frp.gf.secuential_navigation(frp.cf.menu_system, frp.cf.menu_shipping, 
                                 frp.cf.menu_flat_rate_shipping)

    for f in data["ship_code"]:
        frp.gf.search(frp.cf.input_search, f)
        index = data["ship_code"].index(f)
        result = frp.gf.validateText(frp.element_table_flat_rate, f)
        
        if not result:
            frp.click_new_override_button()
            frdp.select_ship_code(f)
            frdp.input_minimum_amount(data["ship_code_flat_rate_min"][index])
            frdp.input_maximum_amount(data["ship_code_flat_rate_max"][index])
            frdp.input_shipping_amount(data["ship_code_flat_rate_cost"][index])
            time.sleep(1) 
            frdp.click_save_button()
            print(f'Flat rate for {f} created.')

        else:
            print(f'Flat rate for {f} already exisits.')


@then('adds card payments')
def step_then(set_up,data_load ) :
    page=set_up
    data=data_load

    cpp = CardPaymentsPage(page)
    cppdp = CardPaymentsDetails(page)

    cpp.cf.select_tenant(data["child_tenant"]) 
    cpp.gf.secuential_navigation(cpp.cf.menu_system, cpp.cf.menu_client_setup, 
                                 cpp.cf.menu_card_type_setup)

    cpp.enable_noc_cash_payment_setup()
    cppdp.click_ui_enabled()
    cppdp.click_save_button()


@then('creates workstations')
def step_then(set_up,data_load ) :
    page=set_up
    data=data_load
    
    wsp = WorkstationsPage(page)
    wsdp = WorkstationsDetails(page)

    wsp.cf.select_tenant(data["parent_tenant"]) 
    wsp.gf.secuential_navigation(wsp.cf.menu_system, wsp.cf.menu_workstations)
    
    for w in data["workstation_types"]:
        wsp.gf.search(wsp.cf.input_search, w)
        result = wsp.gf.validateText(wsp.element_table_workstations, w)
        
        if not result:
            wsp.click_new_workstation_button()

            wsdp.select_facility_code(data["workstation_facility"])
            wsdp.select_workstation_type(w)
            wsdp.input_ip_address(data["ip_address"])
            wsdp.input_label_ip_address(data["label_ip_address"])
            wsdp.input_label_port(data["label_port"])
            wsdp.input_customs_ip_address(data["custom_ip_address"])
            wsdp.input_customs_port(data["custom_port"])
            wsdp.input_reference(w)
            wsdp.select_is_active(data["workstation_active"])
            wsdp.input_attributes('{"qz_scale_enabled":false}')
            wsdp.input_paper_tray_tenants(data["paper_tray_tenants"])
            wsdp.input_paper_tray_media(data["paper_tray_media"])
            wsdp.click_button_save()
            print(f"Workstation {w} created.")
        else:
            print(f"Workstation {w} already exists")


@then('creates locations')
def step_then(set_up,data_load ) :
    page=set_up
    data=data_load

    lp = LocationsPage(page)
    ldp = LocationsDetails(page)

    lp.cf.select_tenant(data["parent_tenant"]) 
    lp.gf.secuential_navigation(lp.cf.menu_wms, lp.cf.menu_warehouse, lp.cf.menu_locations)
    
    i = 1
    for l in data["locations_barcode"]:
        lp.gf.search(lp.cf.input_search, l)
        result = lp.gf.validateText(lp.cf.data_table, l)

        if not result:
            lp.click_new_location_button()
            time.sleep(1) 
            ldp.select_facility_code(data["receiving_facility"])
 
            if l[0] == 'A':
                ldp.select_location_type("Active")
            elif l[0] == 'R':
                ldp.select_location_type("Reserve")
            elif l[0] == 'D':
                ldp.select_location_type("Drop Zone")
            elif l[0] == 'G':
                ldp.select_location_type("Damaged")
            elif l[0] == 'N':
                ldp.select_location_type("Nonsaleable")

            ldp.input_pick_path_order(str(i))
            ldp.check_is_enabled()
            ldp.input_barcode(l)
            ldp.input_location(l)
            ldp.input_building(l[0])
            ldp.input_aisle(l[1:2])
            ldp.input_rack(l[3:4])
            ldp.input_shelf(l[5:6])
            ldp.input_bin(l[7])
            ldp.input_width("10")
            ldp.input_height("10")
            ldp.input_depth("10")
            ldp.input_min_qty("1")
            ldp.input_max_qty("50")
            ldp.click_button_save()
            lp.gf.search(lp.cf.input_search, l)
            time.sleep(1) 
        else:
            continue

        i = i + 1
    

@then('creates shipping carts')
def step_then(set_up,data_load ) :
    page=set_up
    data=data_load

    cp = CartsPage(page)
    cdp = CartsDetails(page)

    cp.cf.select_tenant(data["parent_tenant"])
    cp.gf.secuential_navigation(cp.cf.menu_wms, cp.cf.menu_warehouse, cp.cf.menu_carts)

    for c in data["cart_code"]:
        index = data["cart_code"].index(c)
        cp.gf.search(cp.cf.input_search, c)
        result = cp.gf.validateText(cp.element_table_carts, c)
        logging.info(f"EL VALOR DE c es {c}::: con result {result}")

        if not result:
            cp.click_new_cart_button()
            #time.sleep(1)
            cdp.input_name(c)
            cdp.select_facility_code(data["facility_code"])
            cdp.input_description(data["cart_description"][index])
            if c== "Super":
                cdp.check_is_supertote()
            elif c == "EC":
                cdp.check_is_exception()
            elif c== "B2B":
                cdp.check_is_b2b()
            elif c== "LP":
                cdp.check_is_label_packing()
            elif c== "PM":
                cdp.check_is_pick_module()
            elif c== "JIT":
                cdp.check_is_jit()
            elif c == "RO":
                cdp.check_is_replenishment()
            elif c == "Prepack":
                cdp.check_is_prepack()
            elif c == "Conveyor-noLabel" or c == "Conveyor-asyncLabel":
                cdp.check_is_conveyor
            elif c == "locus":
                cdp.check_is_locus()

            if c != "locus":
                cdp.input_rows(data["rows"][index])
                cdp.input_cols(data["cols"][index])
                cdp.input_units_per_bin(data["units_per_bin"][index])
                
            #page.pause()
            cdp.click_button_save()
             
            
            print(f'Cart {c} created.')
        else:
            print(f'Cart {c} already exists.')
    

@then('creates items and skus')
def create_items_and_skus(set_up,data_load ) :
    page=set_up
    data=data_load

    ip = ItemsPage(page)
    idp = ItemsDetails(page)
    sdp = SkuDetails(page)

    ip.cf.select_tenant(data["child_tenant"])
    ip.gf.secuential_navigation(ip.cf.menu_inventory, ip.cf.menu_items)

    ip.gf.search(ip.cf.input_search, data["item"])
    result = ip.gf.validateText(ip.cf.data_table, data["item"])
    
    if not result:
        #page.pause()
        ip.click_new_cart_button()
        idp.input_item_code(data["item"])
        idp.input_item_desc(data["item"])
        idp.input_item_original_price("10")
        idp.input_item_cost("5")
        idp.click_item_button_save()
        print(f'Item {data["item"]} created.')

        sdp.click_tab_sku_details()
        sdp.click_sku_button_insert()
        
        for sku in data["skus"]:
            sdp.input_sku_code(sku)
            sdp.input_sku_description(sku)
            sdp.input_sku_barcode(sku)
            sdp.input_sku_original_price("10")
            sdp.input_sku_current_price("10")
            sdp.input_sku_cost("3")
            sdp.input_sku_inventory_threshold("0")
            sdp.input_sku_box_quantity("1")
            sdp.check_sku_backorderable()
            #sdp.check_sku_signature_label_required()
            sdp.click_sku_button_save()
            sdp.validate_sku_saved(sku)

        print(f'Item {data["item"]} created with {len(data["skus"])} skus.')
        

@then('creates virtual items')
def creates_virtual_items(set_up,data_load ) :
    page=set_up
    data=data_load
    pass

@then('creates items with kits')
def creates_items_with_kits(set_up,data_load ) :
    page=set_up
    data=data_load
    pass

@then('create Price Groups to items')
def create_price_groups__to_items(set_up,data_load ) :
    page=set_up
    data=data_load
    pass

@then('creates items with lots')
def creates_items_with_lots(set_up,data_load ) :
    page=set_up
    data=data_load
    pass


@then('putaway inventory')
def put_away_inventory(set_up,data_load ) :
    page=set_up
    data=data_load

    pap = PutawayActivePage(page)

    pap.cf.select_tenant(data["child_tenant"])
    pap.gf.secuential_navigation(pap.cf.menu_wms, pap.cf.menu_putaway,
                                 pap.cf.menu_putaway_active)
    
    pap.select_facility(data["facility_name"])
    
    for sku in data["skus"]:
        try:
            index = data["skus"].index(sku)
            #page.pause()
            pap.input_container_barcode(sku + data["container"])
            pap.click_add_container(sku + data["container"])
            pap.gf.validateText(pap.page.locator("#putaway-form-where"), 'Where do you want to move it to?')
            pap.input_location_barcode(data["locations_barcode"][index])
            pap.click_select_location()
            pap.click_complete_putaway()
        except:
            continue


@then('receive inventory')
def receive_inventory(set_up,data_load ) :
    page=set_up
    data=data_load

    rsp = ReceivingStandardPage(page)

    rsp.cf.select_tenant(data["child_tenant"])
    rsp.gf.secuential_navigation(rsp.cf.menu_wms, rsp.cf.menu_receiving,
                                 rsp.cf.menu_standard)

    expect(page.get_by_text("Current Container")).to_be_visible()
    page.wait_for_load_state()
    rsp.select_facility(data["facility_name"])
    rsp.select_business_type(data["business_type_code"])
    #page.pause()
    for sku in data["skus"]:
        rsp.input_quantity(data["quantity_to_receive"])
        rsp.input_sku_barcode(sku)
        rsp.click_button_close_container_F9()
        
        rsp.input_container_barcode(sku + data["container"])
        rsp.click_button_close_container_modal()

        rsp.click_button_complete_F10()
        time.sleep(2)
    
           
