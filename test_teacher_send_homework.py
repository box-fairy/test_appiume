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

        self.help_login()

    def click_add_button(self):
        TouchAction(self.driver).tap(x=347, y=42).perform()

    def finish_and_send_homework(self, homework_name):

        # el15 = self.driver.find_element_by_accessibility_id("task record button")
        # # TouchAction(self.driver).long_press(el15).perform()
        # el15.click()
        # TouchAction(self.driver).long_press(el15, None, None, 2000).perform()
        # time.sleep(3)

        el15 = self.driver.find_element_by_ios_predicate("value == '请输入作业标题'")
        el15.click()
        el15.send_keys(homework_name)
        el16 = self.driver.find_element_by_ios_predicate("value == '请输入作业要求（可选）'")
        el16.click()
        el16.send_keys("zuoyeyaoqiu")

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

        el12 = self.driver.find_element_by_ios_predicate("value == '发布作业'")
        el12.click()

    def check_gendu_pages(self, page_arr):
        for i in page_arr:
            el1 = self.driver.find_element_by_xpath(
                "(//XCUIElementTypeButton[@name=\"task chapter checkbox\"])[" + str(i) + "]")
            el1.click()
        el2 = self.driver.find_element_by_ios_predicate("value == '确定'")
        el2.click()

    def assert_homework(self, homework_name):
        assert self.driver.find_element_by_ios_predicate("value == '发布作业成功'")

        sleep(3)
        assert self.driver.find_element_by_ios_predicate("value CONTAINS '" + homework_name + "'")

    def choose_a_type(self, type_name):
        el13 = self.driver.find_element_by_ios_predicate("value == '" + type_name + "'")
        el13.click()
        sleep(2)

    def choose_a_book(self, book_name):
        while 1:
            try:
                el14 = self.driver.find_element_by_ios_predicate("value == '" + book_name + "'")
                break
            except:
                self.driver.execute_script('mobile: swipe', {'direction': 'up'})

        el14.click()

    def help_login(self):
        try:
            el1 = self.driver.find_element_by_ios_predicate("value == '请输入手机号码'")
            el1.click()
            el1.send_keys("13918255587")
            el2 = self.driver.find_element_by_ios_predicate("value == '请输入短信验证码'")
            el2.click()
            el2.send_keys("111222")
            el3 = self.driver.find_element_by_xpath("(//XCUIElementTypeButton[@name=\"登录\"])[1]")
            el3.click()

            sleep(10)
        except:
            print("已经登录")

    def test_SH_gendu(self):

        homework_name = "gendu" + now_to_date()

        self.click_add_button()

        self.choose_a_type("课件跟读")

        TouchAction(self.driver).tap(x=187, y=109).perform()

        self.choose_a_book("K1-1")

        self.check_gendu_pages([3, 7, 2])

        self.finish_and_send_homework(homework_name)

        self.assert_homework(homework_name)

    def test_SH_gendu_duoju(self):

        homework_name = "duoju" + now_to_date()

        self.click_add_button()

        self.choose_a_type("课件跟读")

        TouchAction(self.driver).tap(x=187, y=109).perform()

        self.choose_a_book("Big English 1")

        self.check_gendu_pages([3, 7, 2])

        self.finish_and_send_homework(homework_name)

        self.assert_homework(homework_name)

    def test_SH_huiben(self):

        homework_name = "huiben" + now_to_date()

        self.click_add_button()

        self.choose_a_type("课外练习")

        # 按选择类型与内容按钮
        TouchAction(self.driver).tap(x=187, y=109).perform()

        # 选择【绘本跟读】类型
        el2 = self.driver.find_element_by_accessibility_id("   绘本跟读")
        el2.click()

        self.choose_a_book("First Little Readers C")

        self.check_gendu_pages([5, 2])

        self.finish_and_send_homework(homework_name)

        self.assert_homework(homework_name)

    def test_SH_huiben_duoju(self):
        homework_name = "hbdj" + now_to_date()

        self.click_add_button()

        self.choose_a_type("课外练习")

        # 按选择类型与内容按钮
        TouchAction(self.driver).tap(x=187, y=109).perform()

        # 选择【绘本跟读】类型
        el2 = self.driver.find_element_by_accessibility_id("   绘本跟读")
        el2.click()

        self.choose_a_book("牛津阅读树5")

        self.check_gendu_pages([5, 2])

        self.finish_and_send_homework(homework_name)

        self.assert_homework(homework_name)
        return

    #
    # def test_SH_peiyin(self):
    #     return

    def teardown(self):
        self.driver.quit()
