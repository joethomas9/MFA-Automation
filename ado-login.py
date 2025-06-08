import pyotp, os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()

URL = os.getenv("ADO_URL")
USERNAME = os.getenv("ADO_USERNAME")
PASSWORD = os.getenv("ADO_PASSWORD")
TOTP_SECRET = os.getenv("ADO_TOTP_SECRET")

def generate_totp(secret):
    totp = pyotp.TOTP(secret)
    return totp.now()

def login_ado():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(record_video_dir="./videos/", 
                                      record_video_size={"width": 1280, "height": 720})
        page = context.new_page()

        # Navigate to Azure DevOps login page and enter email
        page.goto(URL)
        page.locator('#i0116').fill(USERNAME)
        page.locator("#idSIButton9").click()

        # Wait to be taken to org sign-in, then enter password
        # This _might_ be different for your org, if so use the 
        # ID of the password input field and submit button
        page.locator("#passwordInput").fill(PASSWORD)
        page.locator("#submitButton").click()

        # On the authenticator screen, instead of using the app, we will use TOTP
        page.locator("#signInAnotherWay").click()
        page.locator("text=Use a verification code").click()

        # Generate TOTP code and fill it in
        code = generate_totp(TOTP_SECRET)
        print(f"TOTP code generated: {code}", flush=True)
        page.locator("#idTxtBx_SAOTCC_OTC").fill(code)
        page.locator("#idSubmit_SAOTCC_Continue").click()

        # Verify stay signed in
        page.locator("#idSIButton9").click()

        # You are now logged in
        print("Login successful!", flush=True)
        context.close()

login_ado()

