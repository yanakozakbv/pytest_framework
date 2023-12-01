https://rahulshettyacademy.com/dropdownsPractise/

XPath:

1.loc_select_header_input: "//input[@id='autosuggest']"
2.loc_select_flights: "//a[contains(@title,"Flights")]/span[contains(@class,"text-label")]"
3.loc_select_hotels: "//a[contains(@title,"Hotels")]/span[contains(@class,"text-label")]"
4.loc_select_Holiday: "//a[contains(@title,"Holiday Packages")]/span[contains(@class,"text-label")]"
5.loc_select_round_trip:"//table[@class="tblTrip"]/tbody/tr/td/input[@value="RoundTrip"]"
6.loc_select_one_way_trip:"//table[@class="tblTrip"]/tbody/tr/td/input[@value="OneWay"]"
7.loc_select_from_arrow: "//div[@class="left1"]/span[@class="red-arrow-btn"]"
8.loc_select_to_arrow: "//div[@class="right1"]/span[@class="red-arrow-btn"]"
9.loc_select_from_city: "//select[@id='ctl00_mainContent_ddl_originStation1']//option[@value='BKK']" #after openning the drop-down
10.loc_depart_to_city: "//button[@class="ui-datepicker-trigger"][1]"
11.loc_return_date: "//div[@id='Div1']//button[@type='button']" #should be Round Trip option selected
12.loc_close_return_date: "//span[@id='spclearDate']" #should be Round Trip option selected
13.loc_select_passengers: "//*[@id="divpaxinfo"]"
14.loc_select_currency: "//*[@id="ctl00_mainContent_DropDownListCurrency"]"
15.loc_select_family_checkbox: "//label[text()[contains(.,'Family and Friends')]]"
16.loc_search_button: "//input[@value="Search"][1]"
17.loc_add_more_button: "///*[@value="+AddMore"]" #should be Multicity option selected
18.loc_special_assistant_open: "//*[@onclick][2]"
19.loc_special_assistant_close: "//*[@class='popup-close2']" # special assistant shoudl be open
20.loc_select_third_picture: "//*[@data-ikslider-control="2"]"
21.loc_select_senior_checkbox: "//input[@id='ctl00_mainContent_chk_SeniorCitizenDiscount']"
22.loc_special_assistant_download_first_doc: "//tbody/tr[2]/td[3]/a[1]"
22.loc_special_assistant_download_second_doc: "(//a[@class='pdf-download-icon'])[2]"
23.loc_depart_date_select_current:"//a[@class='ui-state-default ui-state-highlight ui-state-active']" #should be calendar
24.loc_select_blinking_banner:"//*[@class="blinkingText"]"
25.loc_select_aed_currency:"//option[@value='AED']" #should be drop-down open
26.loc_select_ok_multicity_alert:"//a[@id='MultiCityModelAlert']" #appears after selecting Multicity
27.loc_select_multicity_second_depart_calendar:"//div[@id='Div2']//button[@type='button']" #appears after selecting Multicity
28.loc_select_footer_flights_text:"//span[@class='group-heading'][normalize-space()='Flights']"
29.loc_select_footer_tax_arrow:"//a[@id='GST']//span[@class='right-arrow']"
30. loc_select_footer_changes_arrow:"//a[@title='Change Flight or Refund']//span[@class='right-arrow']"

CSS:
1.loc_select_flights: "a[title='Flights'] span[class='text-label']"
2.loc_select_from_arrow: "#ctl00_mainContent_ddl_originStation1_CTXTaction"
3.loc_special_assistant_open:"a[onclick="return ShowModal('SpecialAssistancePopup');"]"
4.loc_special_assistant_close: "#SpecialAssistanceWindow" # special assistant shoudl be open
5.loc_select_round_trip:"#ctl00_mainContent_rbtnl_Trip_1"
6.loc_select_hotels:"li[class='myspice_trip'] span:nth-child(1)"
7.loc_select_depart_date:"#ctl00_mainContent_view_date1"
8.loc_select_currency:"#ctl00_mainContent_DropDownListCurrency"
9.loc_select_ok_multicity_alert:"#MultiCityModelAlert"
10.loc_select_footer_changes_arrow:"a[title='Change Flight or Refund'] span[class='right-arrow']"