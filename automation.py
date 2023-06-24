from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pytest

# Login Page tests
def test_login():
    driver = webdriver.Chrome()  # or webdriver.Firefox() for Firefox browser
    driver.get("https://sakshingp.github.io/assignment/login.html")

    # Enter username and password
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    username_input.send_keys("your_username")
    password_input.send_keys("your_password")

    # Click on the submit button to login
    submit_button.click()

    # Wait for the home page to load after successful login
    WebDriverWait(driver, 10).until(EC.title_contains("Home Page"))

    # Assertion for successful login
    assert "Home Page" in driver.title

    # Close the browser
    driver.quit()


# Home Page tests
def test_home_page():
    driver = webdriver.Chrome()  # or webdriver.Firefox() for Firefox browser

    # Assuming you are already logged in and on the Home Page

    # Find the AMOUNT header element
    amount_header = driver.find_element(By.XPATH, "//th[text()='AMOUNT']")

    # Click on the AMOUNT header to sort the values
    amount_header.click()

    # Retrieve all the values in the AMOUNT column
    amount_column_values = driver.find_elements(By.XPATH, "//table/tbody/tr/td[5]")

    # Extract the numerical values from the web elements
    extracted_values = [float(value.text) for value in amount_column_values]

    # Check if the values are sorted in ascending order
    assert extracted_values == sorted(extracted_values)

    # Close the browser
    driver.quit()


# Run the tests and generate an HTML report
pytest.main(['-v', '--html=report.html'])
