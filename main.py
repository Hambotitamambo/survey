from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time

# إعدادات المتصفح للسيرفر
options = Options()
options.add_argument("--headless")  # التشغيل في الخلفية
options.add_argument("--no-sandbox")

# بيانات الدخول من GitHub Secrets
EMAIL = os.getenv("MOBROG_EMAIL")
PASSWORD = os.getenv("MOBROG_PASSWORD")

def run_bot():
    driver = webdriver.Chrome(options=options)
    try:
        driver.get("https://www.mobrog.com/login")
        driver.find_element("id", "email").send_keys(EMAIL)
        driver.find_element("id", "password").send_keys(PASSWORD)
        driver.find_element("xpath", "//button[@type='submit']").click()
        time.sleep(5)
        print("تم تسجيل الدخول بنجاح!")
    finally:
        driver.quit()

if __name__ == "__main__":
    run_bot()
