#!/user/baojiong/projects/pycharmprojects/env/python

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestStudentUI:

    def setup(self):
        caps = {}
        caps["automationName"] = "XCUITest"
        caps["platformName"] = "iOS"
        caps["deviceName"] = "iPhone 8"
        caps["bundleId"] = "com.box-fairy.boxfairy"
        caps["platformVersion"] = "13.3"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

    def test_login(self):
        el1 = self.driver.find_element_by_ios_predicate("value == '请输入手机号码'")
        el1.click()
        el1.send_keys("13918255587")
        el2 = self.driver.find_element_by_ios_predicate("value == '请输入短信验证码'")
        el2.click()
        el2.send_keys("111222")
        el3 = self.driver.find_element_by_xpath("(//XCUIElementTypeButton[@name=\"登录\"])[1]")
        el3.click()
        self.driver.implicitly_wait(10)
        assert self.driver.find_element_by_ios_predicate("value CONTAINS '全部课时'")

    def test_home(self):
        assert self.driver.find_element_by_ios_predicate("value CONTAINS '全部课时'")

    def test_enter_a_course(self):
        el1 = self.driver.find_element_by_xpath(
            "//XCUIElementTypeApplication[@name=\"盒精灵\"]/XCUIElementTypeWindow["
            "1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
            "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
            "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[4]")
        el1.click()

    def teardown(self):
        self.driver.quit()