# Selenium
Tutorial on selenium usage

### Lec1.py

* Contains a boilerplate for a selenium script
* Works for firefox on a barebones pop-os system , which means that it should presumably work on most ubuntu distros
* Using Webdriver-Manager is a best practice which simplified a lot of the prerequesites (Externally downloading and linking the geckodriver, reinstalling firefox dependent on compatibility, etc.)
* driver.get opens the required site
* driver.quit ends the application and is preferred over driver.close
