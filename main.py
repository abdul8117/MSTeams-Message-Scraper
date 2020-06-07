from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

# WebDriver location: 'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python37-32'
browser = webdriver.Firefox()

browser.get("https://teams.microsoft.com")
browser.implicitly_wait(10)

def wait(timeToWait):
  time.sleep(timeToWait)

# enters in your email
email_input = browser.find_element_by_css_selector("input[name='loginfmt']")
wait(3)
email_input.send_keys("<your email here>")
wait(3)
email_input.send_keys(Keys.ENTER)
print("\nEntered in email.")
wait(3)

# enters in your password
password_input = browser.find_element_by_css_selector("input[name='passwd']")
password_input.send_keys("<your password here>")
password_input.send_keys(Keys.ENTER)
print("Entered in password.")
wait(3)

stay_signed_in = browser.find_element_by_id("idSIButton9")
stay_signed_in.send_keys(Keys.ENTER)
print("Signed in.")

wait(50)

# click on the chat button
# its id = "app-bar-86fcd49b-61a2-4701-b771-54728cd291fb"
chat_button = browser.find_element_by_id("app-bar-86fcd49b-61a2-4701-b771-54728cd291fb")
chat_button.click()
print("Accessed private chats.")
wait(4)

# specific chat
element = browser.find_element_by_xpath("//body")
# use the lines below until the print statement to navigate to a specific chat by repeating 'element.send_keys(Keys.ALT, Keys.ARROW_UP)' or 'element.send_keys(Keys.ALT, Keys.ARROW_DOWN)' 
element.send_keys(Keys.ALT, Keys.ARROW_UP)
print("Accessed specific chat.\n\n")

wait(60)
print("Starting to scrape...")

# find, scrape all messages, and store them in messages.txt w/BeatifulSoup
# scrape msgs, PgUp, append to list

count = 0
messages = []

while count <= 1500:
  soup = BeautifulSoup(browser.page_source, features="html.parser")
  msgs = soup.findAll("div", class_="message-body-container")
  
  for msg in msgs:
    messages.append(msg.text)
    print(msg.text, "\n")
    
  # MANUALLY CLICK AWAY FROM THE MESSAGE INPUT BOX
  element.send_keys(Keys.PAGE_UP)
  
  count += 1
  print(count)

finalMsgs = set(messages)

def exportMessages():
  file = open("messages.txt", "w")
  for msg in finalMsgs:
    record = f"{msg}, \n"
    file.write(record)
  file.close()

exportMessages()

time.sleep(10) # stop for 10 seconds
browser.quit()
