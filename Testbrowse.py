from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\saad\\AppData\\Local\\Google\\Chrome\\User Data") #Path to your chrome profile
driver = webdriver.Chrome(executable_path="C:\Program Files\Drivers\chromedriver", options=options)
#driver = webdriver.Chrome(executable_path='C:\Program Files\Drivers\chromedriver')
driver.get("https://my.ryerson.ca/uPortal/f/u21l1s1000/normal/render.uP")




driver.find_element_by_xpath("//*[@id='my-ryerson-login']/div/a/span").click()
time.sleep(2)
#driver.find_element_by_xpath("//*[@id='username']").send_keys("Swazir") #this is my ryerson ID that I would have to enter, but I do not need to since I have autofill enabled on my browser
#driver.find_element_by_xpath("//*[@id='password']").send_keys("jigglypuff12345")$this is not my actual password
driver.find_element_by_xpath("//*[@id='fm1']/section/input[3]").click() #select ramms
time.sleep(3)
driver.get_cookies() #this command takes cookies from your actual chrome browser and inserts them into the automated chrome browser which allows you to bypass 2 factor authentication
window_before = driver.window_handles[0]


driver.find_element_by_xpath("//*[@id='tabLink_u25l1s1000']/span").click()
time.sleep(8);

window_after = driver.window_handles[1];
time.sleep(8);

driver.switch_to.window(window_after)
driver.find_element_by_id('win0groupletPTNUI_LAND_REC_GROUPLET$2').click()#navigating to manage classes on RAMMS
driver.maximize_window()
time.sleep(5);
driver.find_element_by_id('wSCC_LO_FL_WRK_SCC_VIEW_BTN$6').click() #selects enrollment shopping cart
time.sleep(5);
driver.find_element_by_xpath("//*[@id='SSR_DUMMY_RECV1$sels$1$$0']").click()
time.sleep(5);
driver.find_element_by_id('DERIVED_SSS_SCT_SSR_PB_GO').click() #selects continue
time.sleep(5);
driver.find_element_by_id('DERIVED_REGFRM1_SSS_SCHED_PLANNER').click() #selects continue
time.sleep(5);
driver.find_element_by_id('DERIVED_REGFRM1_LINK_ADD_ENRL$291$').click() #selects enrolll, Done!
