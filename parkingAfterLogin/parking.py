from sikuli import *
import datetime
import logging
import shutil

# Configure logging
logging.basicConfig(
    filename='sikulix_log.txt',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logging.info('Script started')

tomorrow=datetime.date.today()+datetime.timedelta(days=1)
print("tomorrow is: ", str(tomorrow.day))
tomorrowImage=str(tomorrow.day)+".png"
tomorrowImageSelected=str(tomorrow.day)+"_s.png"

try:
    # Path to Chrome executable
    chrome = App(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
    if chrome.isRunning():
        # Close Chrome
        chrome.close()
        wait(1)  # Wait for Chrome to close
    # Check if Chrome is running, if not, open it
    if not chrome.isRunning():
        chrome.open()
        wait(1)  # Wait for Chrome to open
    # Open a new tab and go to the URL
    wait("1739304190822.png",15)
    click("1739304190822.png")
       
    # Wait for Calculator to open
    wait("yer.png", 15)
    wait(5)
    click("yer.png")
    wait("1739260922583.png",15)
    wheel(WHEEL_DOWN, 20)
    wait("Booknow.png", 5)
    click("Booknow.png")
    wait("1739141642286.png", 15)
    click("1739141642286.png")

    wait(2)

    # Check if image1 exists
    pattern1 = Pattern(tomorrowImage).similar(0.9)
    pattern2 = Pattern(tomorrowImageSelected).similar(0.9)
    
    if exists(pattern1):
        click(pattern1)
        print("Clicked on tomorrowImage")
    # If image1 is not found, check for image2
    elif exists(pattern2):
        click(pattern2)
        print("Clicked on tomorrowImageSelected")
    else:
        print("Neither image was found")
        click(tomorrowImage)
    
    click("1739026654651.png")
    
    wait("1739026732631.png", 15)
    
    # Scroll down the page
    wheel(WHEEL_DOWN, 8)
    wait(2)
    if exists("1739141113776.png"):
        print("Standard parking sold out")
        logging.info("Standard parking sold out")
        exit()
    
    click("1739027588496.png")
    
    # Scroll down the page
    
    wait("1739026826761.png", 15)
    click("1739026826761.png")
    
    wheel(WHEEL_DOWN, 5)
    
    wait("1739026958480.png", 5)
    click("1739026958480.png")
    wait(2)

except Exception as e:
    print("exception occurred",e)
    logging.error('An error occurred', exc_info=True)
    # Capture a screenshot of the entire screen
    screenshot = capture(SCREEN)
    print(screenshot)
   








