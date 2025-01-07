from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import winsound

# Test mode flag - set to True to simulate finding a slot
TEST_MODE = False

def check_availability():
    try:
        if TEST_MODE:
            print("TEST MODE: Simulating found slot!")
            return True
            
        # Regular check logic continues below...
        driver = webdriver.Chrome()
        driver.get("https://www.ockovacicentrum.cz/cz/objednavka/nemoc")
        
        # Rest of your normal checking code here...
        
    except Exception as e:
        print(f"Error occurred: {e}")
        return False
        
    finally:
        if not TEST_MODE and 'driver' in locals():
            driver.quit()

def main():
    print("Starting availability checker...")
    while True:
        try:
            current_time = time.strftime("%H:%M:%S")
            print(f"\nChecking availability at {current_time}")
            
            if check_availability():
                print("Slot found! Check the website!")
                # Keep beeping until user acknowledges
                while True:
                    winsound.Beep(1000, 1000)
                    response = input("Press 'q' to quit or any other key to check again: ")
                    if response.lower() == 'q':
                        return
                    break
            
            print("Waiting 10 minutes before next check...")
            time.sleep(600)  # 10 minutes
            
        except KeyboardInterrupt:
            print("\nStopping the checker...")
            break
        except Exception as e:
            print(f"Error in main loop: {e}")
            time.sleep(600)

if __name__ == "__main__":
    main()