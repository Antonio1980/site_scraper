import os
import argparse
from bs4 import BeautifulSoup
from web_driver_factory import WebDriverFactory


def log_in_to_otus():
    browser = WebDriverFactory().get_browser()
    browser.get("https://otus.ru/")
    browser.maximize_window()
    log_in = browser.find_element_by_xpath("//button[@data-modal-id='new-log-reg']")
    log_in.click()
    browser.implicitly_wait(5.0)
    email_input = browser.find_element_by_xpath("//*[@class='new-log-reg__form js-login']//input[@type='text']")
    email_input.send_keys("antishipul@yandex.ru")
    password_input = browser.find_element_by_xpath("//input[@type='password']")
    password_input.send_keys("As890890")
    login_button = browser.find_element_by_xpath("//*[@class='new-input-line new-input-line_last new-input-line_relative']/button[@type='submit']")
    login_button.click()
    return browser


def get_otus_html(browser):
    return browser.page_source


def pars_html(inner_html):
    return BeautifulSoup(inner_html, 'html5lib')


def sort_all_ref(parsed_html):
    # return [i["href"] for i in parsed_html.div.find_all("a") if i["href"] != "/"]
    for i in parsed_html.div.find_all("a"):
        if i["href"] != "/" and "https" in i["href"]:
            yield i["href"]


my_parser = argparse.ArgumentParser(prog='my_parser', usage='%(prog)s [path] ', argument_default=argparse.SUPPRESS,
                                    description='HTML Parser (for OTUS courses)', epilog='Enjoy the HTML parser! :)')

my_parser.add_argument('-p', '--path', metavar='P', type=str, help='the path to output file.')

args = my_parser.parse_args()

if hasattr(args, "path"):

    input_path = args.path

else:
    input_path = "output"

browser = log_in_to_otus()
requiredHtml = get_otus_html(browser)
soap_html = pars_html(requiredHtml)

if not os.path.isdir(input_path):
    os.makedirs(input_path)
output_file = input_path + "/courses.csv"

with open(output_file, "w") as csv_file:

    for url in sort_all_ref(soap_html):
        csv_file.write(url + "\n")
