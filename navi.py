from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Specify the path to the NEW ChromeDriver executable you downloaded
webdriver_path = 'path_to_new_chromedriver_executable'

# Rest of your script remains the same

# URL of the login page
login_url = 'https://www.flippa.com/login'

# Your login credentials
username = 'mamusstaffali@gmail.com'
password = 'Elkshoals1!'

# Create a WebDriver instance
driver = webdriver.Chrome(executable_path=webdriver_path)

try:
    # Navigate to the login page
    driver.get(login_url)
    
    # Find and fill in the username/email field
    username_field = driver.find_element(By.ID, 'username')  # You need to inspect the HTML to find the correct ID
    username_field.send_keys(username)
    
    # Find and fill in the password field
    password_field = driver.find_element(By.ID, 'password')  # You need to inspect the HTML to find the correct ID
    password_field.send_keys(password)
    
    # Find and click the login/submit button
    login_button = driver.find_element(By.XPATH, '//button[contains(text(), "Login")]')  # Adjust the XPath as needed
    login_button.click()

    # Wait for the next page to load (you might need to adjust the wait time)
    driver.implicitly_wait(10)

    # Here you can add code for additional actions after logging in
    
finally:
    # Close the browser window
    driver.quit()
