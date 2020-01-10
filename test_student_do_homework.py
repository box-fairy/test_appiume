#!/user/baojiong/projects/pycharmprojects/env/python
from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestStudentDoHomework:

    def setup(self):
        caps = {}
        caps["automationName"] = "XCUITest"
        caps["platformName"] = "iOS"
        caps["deviceName"] = "iPhone 11"
        caps["bundleId"] = "com.box-fairy.boxfairy"
        caps["platformVersion"] = "13.3"
        caps["autoAcceptAlerts"] = "true"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

        self.help_login()

    def choose_a_homework_contain(self, name_contain):
        while 1:
            if len(self.driver.find_elements_by_ios_predicate(
                    "type == 'XCUIElementTypeStaticText' AND value CONTAINS '" + name_contain + "'")) >= 1:
                homework_name = self.driver.find_elements_by_ios_predicate(
                    "type == 'XCUIElementTypeStaticText' AND value CONTAINS '" + name_contain + "'")[0].text
                self.driver.find_elements_by_ios_predicate(
                    "type == 'XCUIElementTypeStaticText' AND value CONTAINS '" + name_contain + "'")[0].click()
                sleep(1)
                break
            else:
                self.driver.execute_script('mobile: swipe', {'direction': 'up'})

        if len(self.driver.find_elements_by_ios_predicate(
                "type == 'XCUIElementTypeStaticText' AND value CONTAINS '" + name_contain + "'")) >= 1:
            self.driver.find_elements_by_ios_predicate(
                "type == 'XCUIElementTypeStaticText' AND value CONTAINS '" + name_contain + "'")[0].click()

        return homework_name

    def read_pages_and_upload(self):
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
                return

    def read_pages_and_upload_duoju(self):
        while 1:
            rec_buttons = self.driver.find_elements_by_accessibility_id("record icon")
            if len(rec_buttons) == 0:
                break;
            else:
                for i in range(len(rec_buttons)):
                    self.driver.find_elements_by_accessibility_id("record icon")[i].click()
                    sleep(3)
                    self.driver.find_element_by_accessibility_id("endRecord icon").click()

                    if len(self.driver.find_elements_by_ios_predicate("value CONTAINS '下一题'")) == 1:
                        self.driver.find_element_by_accessibility_id("下一题").click()

                        if i == len(rec_buttons) - 1:
                            break;
                    else:
                        self.driver.find_element_by_accessibility_id("完成").click()
                        self.driver.find_element_by_accessibility_id("upload on").click()
                        return

    def help_login(self):
        if len(self.driver.find_elements_by_ios_predicate("value == '请输入手机号码'")) >= 1:
            el1 = self.driver.find_element_by_ios_predicate("value == '请输入手机号码'")
            el1.click()
            el1.send_keys("13918255587")
            el2 = self.driver.find_element_by_ios_predicate("value == '请输入短信验证码'")
            el2.send_keys("111222")
            el3 = self.driver.find_element_by_xpath("(//XCUIElementTypeButton[@name=\"登录\"])[1]")
            el3.click()

            sleep(10)
        else:
            return

    def test_failed(self):
        el1 = self.driver.find_element_by_ios_predicate("value == '自动失败'")
        el1.click()

    def test_student_DH_huiben(self):
        self.driver.find_element_by_accessibility_id("练习").click()

        homework_name = self.choose_a_homework_contain("huiben")

        assert self.driver.find_element_by_ios_predicate("value CONTAINS '排行榜'")

        self.driver.find_element_by_ios_predicate("value CONTAINS '完成'").click()

        assert homework_name in self.driver.find_element_by_ios_predicate("value CONTAINS 'huiben'").text

        self.read_pages_and_upload()

        sleep(5)
        TouchAction(self.driver).tap(x=322, y=67).perform()
        sleep(1)
        assert homework_name in self.driver.find_elements_by_ios_predicate("value CONTAINS 'huiben'")[0].text

    # def test_student_DH_gendu(self):
    #
    #     self.driver.find_element_by_accessibility_id("练习").click()
    #
    #     homework_name = self.choose_a_homework_contain("gendu")
    #
    #     assert self.driver.find_element_by_ios_predicate("value CONTAINS '排行榜'")
    #
    #     self.driver.find_element_by_ios_predicate("value CONTAINS '完成'").click()
    #
    #     assert homework_name in self.driver.find_element_by_ios_predicate("value CONTAINS 'gendu'").text
    #
    #     self.read_pages_and_upload()
    #
    #     sleep(5)
    #     TouchAction(self.driver).tap(x=322, y=67).perform()
    #     sleep(1)
    #     assert homework_name in self.driver.find_elements_by_ios_predicate("value CONTAINS 'gendu'")[0].text

    def test_student_DH_gendu_duoju(self):
        self.driver.find_element_by_accessibility_id("练习").click()

        homework_name = self.choose_a_homework_contain("duoju")

        assert self.driver.find_element_by_ios_predicate("value CONTAINS '排行榜'")

        self.driver.find_element_by_ios_predicate("value CONTAINS '完成'").click()

        assert homework_name in self.driver.find_element_by_ios_predicate("value CONTAINS 'duoju'").text

        self.read_pages_and_upload_duoju()

        sleep(5)
        TouchAction(self.driver).tap(x=322, y=67).perform()
        sleep(1)
        assert homework_name in self.driver.find_elements_by_ios_predicate("value CONTAINS 'duoju'")[0].text

    def test_student_DH_huiben_duoju(self):
        self.driver.find_element_by_accessibility_id("练习").click()

        homework_name = self.choose_a_homework_contain("hbdj")

        assert self.driver.find_element_by_ios_predicate("value CONTAINS '排行榜'")

        self.driver.find_element_by_ios_predicate("value CONTAINS '完成'").click()

        assert homework_name in self.driver.find_element_by_ios_predicate("value CONTAINS 'hbdj'").text

        self.read_pages_and_upload_duoju()

        sleep(5)
        TouchAction(self.driver).tap(x=322, y=67).perform()
        sleep(1)
        assert homework_name in self.driver.find_elements_by_ios_predicate("value CONTAINS 'hbdj'")[0].text

    def teardown(self):
        self.driver.quit()
