from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class WebDriverFactory:

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument('--enable-benchmarking')
    # chrome_options.add_argument('--enable-net-benchmarking')
    # chrome_options.add_argument('--remote-debugging-port=9222')
    chrome_options.add_experimental_option('w3c', False)

    @classmethod
    def get_browser(cls):
        try:
            return webdriver.Chrome(ChromeDriverManager().install(), options=cls.chrome_options)
        except Exception as e:
            raise e
