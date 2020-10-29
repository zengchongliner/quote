class OperationBrowser:

    def __init__(self,driver):
        self.driver=driver

    def open_url(self,url):
        try:
            self.driver.get(url)
        except Exception as e:
            print(e,'url可能会出现的错误')

    def send_keys(self,xpath,content):
        try:
            self.driver.find_element_by_xpath(xpath).send_keys(content)
        except Exception as e:
            print(e,'send_keys 可能会出现的错误')

    def click_element(self,xpath):
        try:
            self.driver.find_element_by_xpath(xpath).click()
        except Exception as e:
            print(e,'click_element 可能会出现的错误')

    def get_text(self,xpath):
        try:
            return self.driver.find_element_by_xpath(xpath).text
        except Exception as e:
            print(e,'get_text 可能会出现的错误')

    def change_frame(self,frame_name):
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.frame(frame_name)

    def change_window(self,window_name):
        for window_id in self.driver.window_handles:
            self.driver.switch_to.window(window_id)
            if self.driver.title==window_name:
                break
