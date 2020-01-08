import time
from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


def now_to_date(format_string="%Y-%m-%d %H:%M:%S"):
    time_stamp = int(time.time())
    time_array = time.localtime(time_stamp)
    str_date = time.strftime(format_string, time_array)
    return str_date


class TestTeacherSendHomework:

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

    def test_send_homework_gendu(self):

        homework_name = "gendu" + now_to_date()
        self.driver.implicitly_wait(5)
        TouchAction(self.driver).tap(x=347, y=42).perform()
        el13 = self.driver.find_element_by_ios_predicate("value == '课件跟读'")
        el13.click()
        sleep(2)
        TouchAction(self.driver).tap(x=187, y=109).perform()

        el14 = self.driver.find_element_by_ios_predicate("value == 'K1-1'")
        el14.click()

        el1 = self.driver.find_element_by_xpath("(//XCUIElementTypeButton[@name=\"task chapter checkbox\"])[3]")
        el1.click()
        el2 = self.driver.find_element_by_xpath("(//XCUIElementTypeButton[@name=\"task chapter checkbox\"])[7]")
        el2.click()
        el3 = self.driver.find_element_by_xpath("(//XCUIElementTypeButton[@name=\"task chapter checkbox\"])[2]")
        el3.click()
        el4 = self.driver.find_element_by_ios_predicate("value == '确定'")
        el4.click()

        # el15 = self.driver.find_element_by_accessibility_id("task record button")
        # # TouchAction(self.driver).long_press(el15).perform()
        # el15.click()
        # TouchAction(self.driver).long_press(el15, None, None, 2000).perform()
        # time.sleep(3)

        el5 = self.driver.find_element_by_ios_predicate("value == '请输入作业标题'")
        el5.click()
        el5.send_keys(homework_name)
        el6 = self.driver.find_element_by_ios_predicate("value == '请输入作业要求（可选）'")
        el6.click()
        el6.send_keys("zuoyeyaoqiu")


        el7 = self.driver.find_element_by_xpath(
            "//XCUIElementTypeApplication[@name=\"盒精灵教师\"]/XCUIElementTypeWindow["
            "1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
            "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
            "/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[5]/XCUIElementTypeTextField")
        el7.click()
        el8 = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"确定\"]")
        el8.click()
        el9 = self.driver.find_element_by_xpath(
            "//XCUIElementTypeApplication[@name=\"盒精灵教师\"]/XCUIElementTypeWindow["
            "1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
            "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
            "/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[6]/XCUIElementTypeTextField")
        el9.click()
        el10 = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"确定\"]")
        el10.click()

        el11 = self.driver.find_element_by_ios_predicate("value BEGINSWITH '缎蜕测试班'")
        el11.click()
        el11.click()

        sleep(2)

        el12 = self.driver.find_element_by_ios_predicate("value == '发布作业'")
        el12.click()

        assert self.driver.find_element_by_ios_predicate("value == '发布作业成功'")

        sleep(3)
        assert self.driver.find_element_by_ios_predicate("value CONTAINS '" + homework_name + "'")

    def test_send_homework_gendu_duoju(self):
        homework_name = "duoju" + now_to_date()
        self.driver.implicitly_wait(5)
        TouchAction(self.driver).tap(x=347, y=42).perform()
        el13 = self.driver.find_element_by_ios_predicate("value == '课件跟读'")
        el13.click()
        sleep(2)
        TouchAction(self.driver).tap(x=187, y=109).perform()
        self.driver.execute_script('mobile: swipe', {'direction': 'up'})
        self.driver.execute_script('mobile: swipe', {'direction': 'up'})
        el14 = self.driver.find_element_by_ios_predicate("value == 'Big English 1'")
        el14.click()

        el1 = self.driver.find_element_by_xpath("(//XCUIElementTypeButton[@name=\"task chapter checkbox\"])[3]")
        el1.click()
        el2 = self.driver.find_element_by_xpath("(//XCUIElementTypeButton[@name=\"task chapter checkbox\"])[7]")
        el2.click()
        el3 = self.driver.find_element_by_xpath("(//XCUIElementTypeButton[@name=\"task chapter checkbox\"])[2]")
        el3.click()
        el4 = self.driver.find_element_by_ios_predicate("value == '确定'")
        el4.click()
        el5 = self.driver.find_element_by_ios_predicate("value == '请输入作业标题'")
        el5.click()
        el5.send_keys(homework_name)
        el6 = self.driver.find_element_by_ios_predicate("value == '请输入作业要求（可选）'")
        el6.click()
        el6.send_keys("zuoyeyaoqiu")
        el7 = self.driver.find_element_by_xpath(
            "//XCUIElementTypeApplication[@name=\"盒精灵教师\"]/XCUIElementTypeWindow["
            "1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
            "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
            "/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[5]/XCUIElementTypeTextField")
        el7.click()
        el8 = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"确定\"]")
        el8.click()
        el9 = self.driver.find_element_by_xpath(
            "//XCUIElementTypeApplication[@name=\"盒精灵教师\"]/XCUIElementTypeWindow["
            "1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
            "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
            "/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[6]/XCUIElementTypeTextField")
        el9.click()
        el10 = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"确定\"]")
        el10.click()

        el11 = self.driver.find_element_by_ios_predicate("value BEGINSWITH '缎蜕测试班'")
        el11.click()
        el11.click()

        sleep(2)

        el12 = self.driver.find_element_by_ios_predicate("value == '发布作业'")
        el12.click()

        assert self.driver.find_element_by_ios_predicate("value == '发布作业成功'")

        sleep(3)
        assert self.driver.find_element_by_ios_predicate("value CONTAINS '" + homework_name + "'")

    def test_send_homework_

    def teardown(self):
        self.driver.quit()
