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
        caps["deviceName"] = "iPhone 8"
        caps["bundleId"] = "com.box-fairy.boxfairyteacher"
        caps["platformVersion"] = "13.2"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

    def test_customer_version(self):
        el1 = self.driver.find_element_by_ios_predicate("value == '申请制作'")
        el1.click()
        assert self.driver.find_element_by_ios_predicate("value CONTAINS '申请制作'")

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

    def test_home(self):
        assert self.driver.find_element_by_ios_predicate("value CONTAINS '全部课时'")

    def test_enter_a_course(self):
        el1 = self.driver.find_element_by_xpath(
            "//XCUIElementTypeApplication[@name=\"盒精灵\"]/XCUIElementTypeWindow["
            "1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
            "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
            "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[4]")
        el1.click()

    def test_enter_a_homework_gendu(self):
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
        el5 = self.driver.find_element_by_ios_predicate("value == '请输入作业标题'")
        el5.click()
        el5.send_keys("gendu")
        el6 = self.driver.find_element_by_ios_predicate("value == '请输入作业要求（可选）'")
        el6.click()
        el6.send_keys("genduzuoyeyaoqiu")
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
        el11 = self.driver.find_element_by_ios_predicate("value CONTAINS '缎蜕测试班'")
        el11.click()
        el12 = self.driver.find_element_by_ios_predicate("value == '发布作业'")
        el12.click()

    def test_enter_a_homework_student(self):
        TouchAction(self.driver).tap(x=113, y=638).perform()
        self.driver.implicitly_wait(5)
        assert self.driver.find_element_by_ios_predicate("value CONTAINS '111'")
        el1 = self.driver.find_element_by_xpath(
            "//XCUIElementTypeApplication[@name=\"盒精灵\"]/XCUIElementTypeWindow["
            "1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
            "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
            "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView"
            "/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]")
        el1.click()
        el2 = self.driver.find_element_by_ios_predicate("value CONTAINS '开始完成'")
        el2.click()

        assert self.driver.find_element_by_ios_predicate("value CONTAINS '对句'")

    def teardown(self):
        self.driver.quit()
