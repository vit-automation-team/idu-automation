import datetime
import subprocess
import time

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import input
import locaters
from logger import setup_logger


# Initialize logger
logger = setup_logger(__name__)


class Utils:
    def __init__(self, driver):
        self.driver = driver

    # Find the element in return
    def find_element(self, xpath=None, css_selector=None, id=None, timeout=10):
        time.sleep(1)
        if not any([xpath, css_selector, id]):
            raise ValueError("At least one locator (xpath, css_selector, or ID) must be provided.")

        try:
            if xpath:
                return WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located((By.XPATH, xpath))
                )
            elif css_selector:
                return WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
                )
            elif id:
                return WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located((By.ID, id))
                )
        except TimeoutException:
            raise NoSuchElementException("Element not found within the specified timeout")

    # Check if element is visible or nor
    def is_element_visible(self, xpath, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    # Find input field and send keys
    def clear_and_send_keys(self, keys, xpath=None, css_selector=None, id=None, timeout=30):
        try:
            input_field = self.find_element(xpath, css_selector, id)
            input_field.clear()
            input_field.send_keys(keys)
        except (TimeoutException, NoSuchElementException, timeout):
            raise NoSuchElementException("Element not found within the specified timeout")

    # Searching the keyword in Web GUI search bar
    def search_WebGUI(self, value):
        time.sleep(5)
        logger.debug(f"Searching for the keyword: '{value}'")
        try:
            search_bar = self.find_element(*locaters.Search_Bar)
            search_bar.clear()
            search_bar.send_keys(value)

            for i in range(1, 49):
                path1 = f'//*[@id="root"]/div[1]/div[2]/div[1]/div[1]/div[3]/a[{i}]'
                path2 = f'root > div.jioMainGrid > div.jioGridRight > div.jioGridRightTop > div.jioSearchBar > div.jioSearchResults > a:nth-child({i})'

                lists = self.find_element(path1, path2).text

                if value in lists:
                    self.find_element(path1, path2).click()
                    return
            time.sleep(5)
            logger.warning(f"No search result found for keyword: '{value}'")
        except Exception as e:
            logger.error(f"Error occurred while searching for the keyword: '{value}': {str(e)}")

    # Ping check
    def check_ping(self, target, protocol):
        try:
            logger.debug(f"Checking Ping {str(protocol).upper()} to {target}")
            loss_packet_count = 20
            command = f'ping -{protocol} -n 20 {target}'
            p = subprocess.run(command, shell=True, stdin=subprocess.PIPE, capture_output=True, text=True)

            ping_status = ""
            for line in p.stdout.splitlines():
                if 'Packets: Sent' in line:
                    ping_status = line
                    loss_packet_count = int(line.split('Lost = ')[1].split(' (')[0])
                    break

            logger.debug(ping_status)

            if loss_packet_count < 10:
                logger.info(f'Ping {str(protocol).upper()} Passed')
                return True
            else:
                logger.error(f'Ping {str(protocol).upper()} Failed')
                return False

        except Exception as e:
            logger.error(f'An error occurred during {str(protocol).upper()} ping: {e}')
            return False

    # Checking IPv6 status
    def get_ipv6_info(self):
        logger.debug("Getting WAN IPv6 Information")
        result = {"status": False, "value": ""}

        try:
            self.search_WebGUI("WAN Information")

            ipv6_address_element = self.find_element(*locaters.WanInfo_IPv6)
            ipv6_address = ipv6_address_element.text
            result["value"] = ipv6_address

            if ipv6_address and ipv6_address != "0::0":
                result["status"] = True
                logger.info(f"Successfully retrieved WAN IPv6 address: {ipv6_address}")
            else:
                logger.error(f"Device is NOT Getting WAN IPv6 Address: {ipv6_address}")

        except NoSuchElementException:
            logger.error("WAN IPv6 address element not found on the page")
        except Exception as e:
            logger.error(f"An error occurred while fetching WAN IPv6 info: {e}")

        return result

    # Checking Firmware Version
    def get_firmware_version(self):
        logger.debug("Retrieving Firmware Version.....")
        try:
            self.search_WebGUI("WAN Information")
            firmware_version = self.find_element(*locaters.SysInfo_FirmwareVersion).text
            logger.info(f"Current firmware version: {firmware_version}")
            return firmware_version
        except Exception as e:
            logger.error(f"An error occurred while fetching Firmware Version: {e}")

    # Check internet connectivity
    def check_website_connectivity(self, urls):
        logger.info("Checking website connectivity")
        from selenium import webdriver
        for url in urls:
            try:
                driver = webdriver.Chrome()
                driver.get(url)
            except Exception as e:
                logger.error(f"Error accessing {url}")
                return False
            finally:
                driver.quit()

        logger.info('URL access is successful')
        return True

    # Taking DBG logs
    def get_DBGLogs(self):
        try:
            logger.warning('Initiating DBG log collection after encountering an issue')
            # Assuming `input.URL` contains the base URL
            self.driver.get(f'{input.URL}/WCGI/?dbglogs')
            logger.warning('DBG log collected at: {}'.format(datetime.datetime.now()))
            time.sleep(30)
        except Exception as e:
            logger.error(f'Error occurred while collecting DBG logs: {e}')

    # Navigate to page
    def navigate(self, page_name):
        try:
            time.sleep(5)
            excepted_url = f'{input.URL}/#/{page_name}'

            self.driver.get(excepted_url)
            time.sleep(3)
            current_url = self.driver.current_url
            if current_url == excepted_url:
                logger.debug(f'Navigating to {page_name} Page ')
            else:
                logger.error(f'Unable Navigate to {excepted_url}')

        except Exception as e:
            logger.error(f"Error occurred while navigating to {page_name} page: {e}")
        finally:
            time.sleep(5)

    # Getting System Information
    # def get_system_info(self):
    #     logger.info( "Getting System Information" )
    #     result = {"Firmware Version": "" , "Serial Number": "" , "Model Name": ""}
    #
    #     try:
    #         self.search_WebGUI( "System Information" )
    #         self.find_element( '//div[@class="iconRefresh"]//*[name()="svg"]' ).click()
    #         result["Firmware Version"] = self.find_element( *locaters.SysInfo_FirmwareVersion ).text
    #         result["Serial Number"] = self.find_element( *locaters.SysInfo_SerialNumber ).text
    #         result["Model Name"] = self.find_element( *locaters.SysInfo_ModelName ).text
    #
    #         logger.info( "Successfully retrieved System Information" )
    #
    #     except NoSuchElementException as e:
    #         logger.error( f"Element not found while fetching System Information: {e}" )
    #     except Exception as e:
    #         logger.error( f"An error occurred while fetching System Information: {e}" )
    #
    #     return result
    #
    # #Getting System Information
    # def get_LAN_info(self):
    #     logger.info( "Fetching LAN Information..." )
    #
    #     result = {"MAC Address": "" , "IPv4 IP Address": "" , "IPv6 IP Address": "" , "IPv4 DHCP Server": ""}
    #
    #     try:
    #         self.search_WebGUI( "LAN Information" )
    #         self.find_element( '//div[@class="iconRefresh"]//*[name()="svg"]' ).click()
    #
    #         result["MAC Address"] = self.find_element( *locaters.LANInfo_MACAddress ).text
    #         result["IPv4 IP Address"] = self.find_element( *locaters.LANInfo_IPv4Address ).text
    #         result["IPv6 IP Address"] = self.find_element( *locaters.LANInfo_IPv6Address ).text
    #         result["IPv4 DHCP Server"] = self.find_element( *locaters.LANInfo_IPv4DHCPServer ).text
    #
    #         logger.info( "LAN Information successfully retrieved." )
    #
    #     except NoSuchElementException as e:
    #         logger.error( f"Element not found while fetching LAN Information: {e}" )
    #     except Exception as e:
    #         logger.error( f"An error occurred while fetching LAN Information: {e}" )
    #     finally:
    #         logger.debug( result )
    #         return result
