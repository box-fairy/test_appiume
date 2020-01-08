import time
from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


def now_to_date(format_string="%Y-%m-%d %H:%M:%S"):
    time_stamp = int(time.time())
    time_array = time.localtime(time_stamp)
    str_date = time.strftime(format_string, time_array)
    return str_date


class TestTeacherLookHomework:

    def setup(self):
        caps = {}
        caps["automationName"] = "XCUITest"
        caps["platformName"] = "iOS"
        caps["deviceName"] = "iPhone 8"
        caps["bundleId"] = "com.box-fairy.boxfairyteacher"
        caps["platformVersion"] = "13.2"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

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
        assert self.driver.find_element_by_ios_predicate("value CONTAINS '练习'")

    def test_look_homework_1(self):
        # homework_name = "gendu" + now_to_date()

        el1 = self.driver.find_element_by_xpath(
            "//XCUIElementTypeApplication[@name=\"盒精灵教师\"]/XCUIElementTypeWindow["
            "1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
            "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
            "/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]")
        el1.click()

        # nWaitToLook = len(self.driver.find_elements_by_ios_predicate("value = '待提交'"))
        # el2 = self.driver.find_element_by_xpath(
        #     "//XCUIElementTypeApplication[@name=\"盒精灵教师\"]/XCUIElementTypeWindow["
        #     "1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
        #     "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
        #     "/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[" + '%d' % (nWaitToLook + 1) + "]")
        # el2.click()

        el2 = self.driver.find_element_by_xpath(
            "//XCUIElementTypeApplication[@name=\"盒精灵教师\"]/XCUIElementTypeWindow["
            "1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
            "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
            "/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[2]")
        el2.click()

        el3 = self.driver.find_element_by_xpath(
            "//XCUIElementTypeApplication[@name=\"盒精灵教师\"]/XCUIElementTypeWindow["
            "1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
            "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
            "/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[3]")
        el3.click()

        # el5 = self.driver.find_elements_by_ios_predicate("type == 'XCUIElementTypeStaticText'")[3]
        # name = el5.text
        # print(name)
        # sleep(5)

        # el4 = self.driver.find_element_by_xpath(
        #     "//XCUIElementTypeApplication[@name=\"盒精灵教师\"]/XCUIElementTypeWindow["
        #     "1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
        #     "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
        #     "/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[3]/XCUIElementTypeTextView")
        # el4 = self.driver.find_elements_by_ios_predicate("type == 'XCUIElementTypeTextView'")[1]
        # el4.click()
        # el4.send_keys("very good")

        el5 = self.driver.find_element_by_ios_predicate("type == 'XCUIElementTypeTextView' AND value == "
                                                        "'发音很纯正，作业完成非常认真，再接再厉！'")
        el5.click()
        # el5.click()
        # el5.send_keys("Good")
        #
        el6 = self.driver.find_element_by_ios_predicate("value == '提交'")
        el6.click()

        # sleep(5)
        # assert "Westbrook" in self.driver.find_element_by_ios_predicate("value == '" + "Westbrook" + "'")
        assert self.driver.find_element_by_ios_predicate("value == '批改完成'")

    def teardown(self):
        self.driver.quit()
