# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["platformName"] = "android"
caps["deviceName"] = "MuMu"
caps["appPackage"] = "com.soft.blued"
caps["appActivity"] = ".ui.login_register.SignInActivity"
caps["noReset"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(5)

# el1 = driver.find_element_by_id("com.soft.blued:id/tv_positive_detailed")
# el1.click()
# el2 = driver.find_element_by_id("com.soft.blued:id/tv_positive_detailed")
# el2.click()
# el3 = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
# el3.click()
# el4 = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
# el4.click()
el5 = driver.find_element_by_id("com.soft.blued:id/ctt_left")
el5.click()
el6 = driver.find_element_by_id("com.soft.blued:id/rd_debug")
el6.click()
el7 = driver.find_element_by_id("com.soft.blued:id/btn_ok")
el7.click()
el8 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.EditText")
el8.send_keys("13366470799")
el9 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText")
el9.send_keys("123123")
el9.click()

driver.quit()