from selenium import webdriver
import unittest
import time

class Items(unittest.TestCase):
    def test_view_item_page(self):
        driver = webdriver.Chrome('chromedriver.exe')
        driver.get('http://www.missingchildren.org.ar/')
        driver.find_element_by_name('busqueda').send_keys('Luciano')
        driver.find_element_by_xpath('//*[@id="form1"]/div/table/tbody/tr/td[2]/input').click()
        time.sleep(2)
        driver.quit()







if __name__ == '__main__':
    unittest.main()