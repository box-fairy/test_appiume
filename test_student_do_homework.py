#!/user/baojiong/projects/pycharmprojects/env/python
from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestStudentDoHomework:

    def setup(self):
        caps = {}
        caps["automationName"] = "XCUITest"
        caps["platformName"] = "iOS"
        caps["deviceName"] = "iPhone 8"
        caps["bundleId"] = "com.box-fairy.boxfairy"
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
        assert self.driver.find_element_by_ios_predicate("value CONTAINS '全部课时'")

    def test_student_do_homework_gendu(self):
        el0 = self.driver.find_element_by_accessibility_id("练习")
        el0.click()

        homework_name = self.driver.find_elements_by_ios_predicate("value CONTAINS 'gendu'")[0].text

        el1 = self.driver.find_element_by_xpath(
            "//XCUIElementTypeApplication[@name=\"盒精灵\"]/XCUIElementTypeWindow["
            "1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
            "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
            "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView"
            "/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]")
        el1.click()

        assert self.driver.find_element_by_ios_predicate("value CONTAINS '排行榜'")

        el2 = self.driver.find_element_by_ios_predicate("value CONTAINS '完成'")
        el2.click()

        assert homework_name in self.driver.find_element_by_ios_predicate("value CONTAINS 'gendu'").text

        while 1:
            el3 = self.driver.find_element_by_xpath(
                "//XCUIElementTypeApplication[@name=\"盒精灵\"]/XCUIElementTypeWindow["
                "1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
                "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
                "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeImage")
            el3.click()
            sleep(3)
            el3.click()

            if len(self.driver.find_elements_by_ios_predicate("value CONTAINS '下一题'")) == 1:
                el4 = self.driver.find_element_by_accessibility_id("下一题")
                el4.click()
            else:
                el4 = self.driver.find_element_by_accessibility_id("完成")
                el4.click()

                el5 = self.driver.find_element_by_xpath(
                    "//XCUIElementTypeApplication[@name=\"盒精灵\"]/XCUIElementTypeWindow["
                    "1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
                    "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
                    "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage[2]")
                el5.click()
                break

        sleep(5)
        TouchAction(self.driver).tap(x=295, y=43).perform()
        sleep(1)
        assert homework_name in self.driver.find_elements_by_ios_predicate("value CONTAINS 'gendu'")[0].text

    def teardown(self):
        self.driver.quit()
