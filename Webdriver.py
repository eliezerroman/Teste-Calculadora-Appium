from appium import webdriver


class Driver:
    def __init__(self):
        desired_cap = {
            'platformName': 'Android',
            'deviceName': 'emulator-5554',
            # 'avd': 'Pixel_2_API_30',
            'appPackage': 'com.google.android.calculator',
            'appActivity': 'com.android.calculator2.Calculator'
        }
        self.instance = webdriver.Remote(
            "http://127.0.0.1:4723/wd/hub", desired_cap)
