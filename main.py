import time
from pathlib import Path
import undetected_chromedriver.v2 as uc

options = uc.ChromeOptions()
options.user_data_dir = str(Path("profile").absolute())
options.add_argument("--no-first-run --no-service-autorun --password-store=basic")

driver = uc.Chrome(options=options)
driver.get("https://www.youtube.com/")

driver.save_screenshot("datadome_undetected_webddriver.png")

input("press any key to exit...")
