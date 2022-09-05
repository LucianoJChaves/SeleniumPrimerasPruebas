from selenium import webdriver
import unittest
import time

class Items(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get('http://automationpractice.com/index.php')

    def test_do_nothing(self):
        pass

    def test_view_item_page(self):
        #BUSQUEDA_ARTICULO
        self.driver.find_element_by_id('search_query_top').send_keys('dress')
        self.driver.find_element_by_name('submit_search').click()
        self.driver.implicitly_wait(5)
        #ELEGIR_ARTICULO_Printed_Summer_Dress
        self.driver.find_element_by_xpath('//*[@id="center_column"]/ul/li[1]/div/div[1]/div/a[1]/img').click()
        title = self.driver.find_element_by_xpath('//h1[@itemprop="name"]').text
        self.assertEqual(title, 'Printed Summer Dress')
        #ADD_TO_CART
        self.driver.find_element_by_name('Submit').click()
        self.driver.implicitly_wait(2)
        #PROCEDED_TO_CHECKOUT
        self.driver.find_element_by_xpath('//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a').click()
        self.driver.implicitly_wait(2)
        #PROCEDED_TO_CHECKOUT_2
        self.driver.find_element_by_xpath('//*[@id="center_column"]/p[2]/a[1]').click()
        self.driver.implicitly_wait(2)
        #LOGIN
        self.driver.find_element_by_name('email').send_keys('lucianojulianchaves@gmail.com')
        self.driver.find_element_by_name('passwd').send_keys('Automation2022')
        self.driver.find_element_by_name('SubmitLogin').click()
        time.sleep(1)
        # PROCEDED_TO_CHECKOUT_3
        self.driver.find_element_by_name('processAddress').click()
        #CLICK_CHECKBOX
        self.driver.find_element_by_name('cgv').click()
        time.sleep(1)
        self.driver.find_element_by_name('processCarrier').click()
        self.driver.implicitly_wait(2)



    def tearDown(self):
        self.driver.quit()

#time.sleep(1)

if __name__ == '__main__':
    unittest.main()
