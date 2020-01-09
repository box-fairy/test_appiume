#!/user/baojiong/projects/pycharmprojects/env/python
from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait


class TestStudentUI:

    def setup(self):
        caps = {}
        caps["automationName"] = "XCUITest"
        caps["platformName"] = "iOS"
        # caps["deviceName"] = "Ding's iPhone"
        # caps["udid"] = "66ed8a83002310937d0999dea7496cc505b42fb2"
        caps["deviceName"] = "包炯's iPhoneX"
        caps["udid"] = "dc254a6433fee58bb8ebd0bc4bb69cca578e8ff2"
        caps["app"] = "/Users/baojiong/Library/Developer/Xcode/DerivedData/boxfairyteacher-elbueuqihgcsbyamlopvtjtwylpp/Build/Products/Debug-iphoneos/boxfairyteacher.app"

        caps["xcodeOrgId"] = "8HXUNCJ8HX"
        caps["xcodeSigningId"] = "iPhone Developer"
        caps["autoAcceptAlerts"] = "true"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def test_customer_version(self):
        el1 = self.driver.find_element_by_ios_predicate("value == '申请制作'")
        el1.click()
        assert self.driver.find_element_by_ios_predicate("value CONTAINS '申请制作'")

    def test_login(self):

        el1 = self.driver.find_element_by_xpath("//XCUIElementTypeOther[@name=\"欢迎来到盒精灵教师端\"]/XCUIElementTypeTextField[1]")
        el1.click()
        el1.send_keys("13918255587")
        el2 = self.driver.find_element_by_xpath("//XCUIElementTypeOther[@name=\"欢迎来到盒精灵教师端\"]/XCUIElementTypeTextField[2]")
        el2.send_keys("111222")
        el3 = self.driver.find_element_by_accessibility_id("登录")
        el3.click()

        # assert self.driver.find_element_by_ios_predicate("value CONTAINS '练习'")


    def teardown(self):
        self.driver.quit()
