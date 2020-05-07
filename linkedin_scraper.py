from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv


driver = webdriver.Chrome("./chromedriver")
login_email=input("Enter Login Email\n")
login_password=input("Enter Password\n")
post_url = input("Enter Link To Post\n")


#########################################
driver.get('https://linkedin.com')
login = driver.find_element_by_xpath('/html/body/nav/a[3]')
login.click()

time.sleep(0.5)

email = driver.find_element_by_id('username')
email.click()
time.sleep(0.5)
email.send_keys(login_email)

password = driver.find_element_by_id('password')
password.click()
password.send_keys(login_password)

signin = driver.find_element_by_css_selector('.btn__primary--large.from__button--floating')
signin.click()
time.sleep(2)
driver.get(post_url)

#########################################




#######Get likes##########
time.sleep(2)
number_likes = driver.find_element_by_css_selector('.v-align-middle.social-details-social-counts__reactions-count').text
likes_button = driver.find_element_by_xpath('/html/body/div[8]/div[3]/div/div/div/div/section/div/div[5]/div/ul/li[1]/button/span')
likes_button.click()

time.sleep(3)


while True:
	driver.execute_script('document.querySelector(".artdeco-modal__content.social-details-reactors-modal__content.ember-view").scrollTop+=10')
	links = driver.find_elements_by_css_selector('.actor-item a')
	if(len(links)>=int(number_likes)-5):
		break

likes=[]
links = driver.find_elements_by_css_selector('.actor-item a')
names = driver.find_elements_by_css_selector('.actor-item a .profile-link .name span[dir="ltr"]')
for link,name in zip(links,names):
	likes.append((link.get_attribute("href"),name.text))

#########################################







#######Get comments##########
driver.get(post_url)

while True:
	try:
		load_more_comments_button = driver.find_element_by_css_selector('.comments-comments-list__load-more-comments-button.artdeco-button.artdeco-button--muted.artdeco-button--1.artdeco-button--tertiary.ember-view')
		load_more_comments_button.click()
	except:
		print("waiting.....")
		time.sleep(3.5)
		try:
			load_more_comments_button = driver.find_element_by_css_selector('.comments-comments-list__load-more-comments-button.artdeco-button.artdeco-button--muted.artdeco-button--1.artdeco-button--tertiary.ember-view')
		except:
			break

comments=[]
links = driver.find_elements_by_css_selector('.comments-post-meta__profile-link.t-16.t-black.t-bold.tap-target.ember-view')
for link in links:
	comments.append(link.get_attribute("href"))

print(len(comments))
#########################################



ids = set(likes+comments)


#######Write to file##########
with open('linkedin.csv','w') as f:
	writer = csv.writer(f)
	writer.writerow(['S.No','LinkedIn ID','Liked?','Commented?'])
	for sno,i in enumerate(ids,1):
		l="No"
		c="No"
		if i in likes:
			l="Yes"
		if i in comments:
			c="Yes"
		writer.writerow([sno,i,l,c])
print("Written to File\n")
#########################################

