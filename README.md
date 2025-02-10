<div style="display: flex; justify-content: space-between;">
    <img src="https://github.com/d4v1-sudo/wifi-sploit/raw/beta/assets/wifi-sploit.png" style="text-align: left ; height:20%; width:20%" />
    <!--
    <img src="https://github.com/d4v1-sudo/wifi-sploit/raw/master/assets/router.jpg" style="text-align: left ; height:20%; width:20%" />
    <img src="https://github.com/d4v1-sudo/wifi-sploit/raw/master/assets/slash.png" style="text-align: center ; height:20%; width:20%" />
    <img src="https://github.com/d4v1-sudo/wifi-sploit/raw/master/assets/www.jpg" style="text-align: right ; height:20%; width:20%" />
    -->
</div>
<h3 style="text-align:center;">WiFi-Sploit</h3>
<p style="text-align:center;">
   🔒 Complete scripts to brute-force any login page
</p>

# **Beta** branch: 
 - Just uses browsers, some things fixed and new script to use google chrome.
 - Removed wfs.py because as it didn't click any button, so you couldn't be sure about the login status.

## About
 - Originally made for `python2` but now just works using `python3`.
 - Originally it was made for router's login pages but it works fine in any login page site, even on internet.

## Prerequisites

1. Your laptop/computer must be **connected to the Wi-Fi** network whose router or site login page will be pentested.
2. A laptop/computer that has `Python 3.x` installed.

### How to install Python/Python3

- [Windows](https://www.python.org/downloads/windows/)
- [MacOS](https://www.python.org/downloads/macos/)
- Linux/Unix (Well.. python comes preinstalled on most Linux distributions. Otherwise, you can download it [here](https://www.python.org/downloads/source/))

<br />

## About the Scripts

Wifi-Sploit provides two scripts:

### wfs-browser.py

- Utilizes Selenium-based script with customizable HTML element names.
- Uses firefox webdriver
- Offers more flexibility in specifying HTML element names for username, password, and submit button.
- Useful when the default element names don't match the target webpage's structure.
- Requires Python 3.x and Selenium WebDriver.
- Usage: `python3 wfs-browser.py`.
- Allows users to specify HTML element names for username, password, and submit button.

### wfs-chrome.py

- Basically the ```wfs-browser-input.py``` but using google chrome instead of firefox (that I recommend the most)
- Usage*: `python3 wfs-chrome.py`
  *Verify instructions below before run

<br />

## Before Running the scripts:

- On linux:
```bash
chmod +x /PATH-TO/selenium/webdriver/common/linux/selenium-manager
```
- On windows: just to be sure, run the scripts as administrator

## Before Running `wfs-chrome.py`:

- On linux:
Download chromedriver for linux 64-bits: [https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip](https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip)

And then:
```bash
unzip chromedriver_linux64.zip
sudo cp chromedriver /usr/local/bin
```
And install chrome version 114 from [https://bestim.org/chrome-114.html](https://bestim.org/chrome-114.html) (dependencies: ```fonts-liberation```, ```libu2f-udev``` and ```libvulkan1``` → ```sudo apt install fonts-liberation libu2f-udev libvulkan1 -y```)

- On windows:
  
  Install chrome version 114 from [https://bestim.org/chrome-114.html](https://bestim.org/chrome-114.html)
  
  Install chromedriver from [https://storage.googleapis.com/chrome-for-testing-public/127.0.6533.88/win64/chrome-win64.zip](https://storage.googleapis.com/chrome-for-testing-public/127.0.6533.88/win64/chrome-win64.zip)
  
  Change wfs-chrome.py line 81 to:
  ```
  service = Service('C:/<PATH/TO>/chromedriver.exe')
  ```

For more chromedriver options acess: [https://getwebdriver.com/chromedriver](https://getwebdriver.com/chromedriver)

## Running the Scripts

1. Clone this repository:
```bash
git clone https://github.com/kevinadhiguna/wifi-sploit.git
```

2. Change directory to `wifi-sploit`:
```bash
cd wifi-sploit
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the desired script:
   - For `wfs-browser.py`: `python3 wfs-browser.py`
   - For `wfs-chrome.py`: `python3 wfs-chrome.py`

<br />

## Additional Notes

- It is recommended to check out the `address.md` file for the Wi-Fi router's IP address before running the scripts.
- Default usernames and passwords for Wi-Fi routers can be found in the `username.txt` and `password.txt` files, respectively.
- Don't want the browser screen? No problem! Find ```options.headless = True``` and change it to ```False```
- Remember, these tools are for educational purposes only. Misuse is not condoned.

<br />
<hr />

## Disclaimer

<b>I am not responsible for any misuse. These tools are only for educational purposes.</b>

<br />

![Hello !](https://api.visitorbadge.io/api/VisitorHit?user=kevinadhiguna&repo=wifi-sploit&label=thanks%20for%20dropping%20in%20!&labelColor=%23000000&countColor=%23FFFFFF)
