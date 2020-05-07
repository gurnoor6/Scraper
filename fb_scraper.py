from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome("./chromedriver")
login_email=input("enter your email address\n")
login_password=input("enter password \n")

post_url = input("enter post url\n")


#########################################
driver.get('https://www.facebook.com')

time.sleep(0.5)

email = driver.find_element_by_id('email')
email.click()
time.sleep(0.5)
email.send_keys(login_email)

password = driver.find_element_by_id('pass')
password.click()
password.send_keys(login_password)

signin = driver.find_element_by_id('u_0_b')
signin.click()
time.sleep(2)
driver.get(post_url)

#########################################




#######Get likes##########
time.sleep(2)
likes_button = driver.find_element_by_class_name('_3dlf')
likes_button.click()

time.sleep(3)

while True:
	try:
		button = driver.find_element_by_css_selector('a[rel="async"][class="pam uiBoxLightblue uiMorePagerPrimary"]')
		button.click()
	except:
		time.sleep(3)
		try: 
			button = driver.find_element_by_css_selector('a[rel="async"][class="pam uiBoxLightblue uiMorePagerPrimary"]')
		except:
			break

likes=[]
links = driver.find_elements_by_css_selector('#reaction_profile_browser li a[data-gt]')
for link in links:
	likes.append(link.get_attribute("href"))


#######Write to file##########
filename='fblikes.txt'
with open(filename,'w') as f:
	for item in likes:
		f.write(item)
		f.write('\n')
	f.write(str(len(likes)))
	f.write('\n')

print("written in file {}".format(filename))
#########################################

