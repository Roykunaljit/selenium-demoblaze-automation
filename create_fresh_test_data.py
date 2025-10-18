import pandas as pd
import os
from datetime import datetime
import random

# Ensure we're in the right directory
data_dir = "selenium_demoblaze_framework/data"
os.makedirs(data_dir, exist_ok=True)

# Generate a COMPLETELY unique username
timestamp = datetime.now().strftime("%H%M%S")  # Just time for shorter username
random_num = random.randint(1000, 9999)
unique_username = f"user{timestamp}{random_num}"  # Shorter, unique username
password = "Test@123"

print(f"[INFO] Creating test with NEW username: {unique_username}")
print(f"       This username has NEVER been used before!")

# Create test data with ONLY 16 steps (NO LOGOUT)
test_data = {
    'Test_Step_ID': list(range(1, 17)),  # Only 16 steps
    'Action': [
        'navigate_to_url',
        'wait',  # Initial wait for page load
        'click_element',  # Click Sign up
        'wait_for_element',  # Wait for signup modal
        'enter_text',  # Enter username
        'enter_text',  # Enter password
        'click_element',  # Click Sign up button
        'handle_alert',  # Handle signup success alert
        'wait',  # Wait after signup
        'click_element',  # Click Login
        'wait_for_element',  # Wait for login modal
        'enter_text',  # Enter username
        'enter_text',  # Enter password
        'click_element',  # Click Log in button
        'wait',  # Wait for login to complete
        'verify_text'  # Verify welcome message
    ],
    'Locator_Type': [
        '', '', 'id', 'id', 'id', 'id', 'xpath', '', '', 'id', 'id', 'id', 'id', 'xpath', '', 'id'
    ],
    'Locator_Value': [
        '',
        '',
        'signin2',
        'sign-username',
        'sign-username',
        'sign-password',
        '//button[text()="Sign up"]',
        '',
        '',
        'login2',
        'loginusername',
        'loginusername',
        'loginpassword',
        '//button[text()="Log in"]',
        '',
        'nameofuser'
    ],
    'Value': [
        'https://www.demoblaze.com',
        '2',  # Wait 2 seconds for page to load
        '',
        '',
        unique_username,  # UNIQUE USERNAME HERE
        password,
        '',
        'accept',
        '2',  # Wait 2 seconds after signup
        '',
        '',
        unique_username,  # SAME UNIQUE USERNAME HERE
        password,
        '',
        '3',  # Wait 3 seconds for login to complete
        f'Welcome {unique_username}'  # VERIFY WITH UNIQUE USERNAME
    ],
    'Expected_Result': [
        'Navigate to DemoBlaze homepage',
        'Wait for page to load',
        'Open signup modal',
        'Signup form should be visible',
        f'Enter username: {unique_username}',
        'Enter password',
        'Click Sign up button',
        'Handle signup success alert',
        'Wait for modal to close',
        'Open login modal',
        'Login form should be visible',
        f'Enter username: {unique_username}',
        'Enter password',
        'Click Log in button',
        'Wait for login to complete',
        f'Verify welcome message shows: Welcome {unique_username}'
    ]
}

# Save to Excel
df = pd.DataFrame(test_data)
excel_file = os.path.join(data_dir, "keyword_test_cases.xlsx")

# Delete old file if it exists
if os.path.exists(excel_file):
    os.remove(excel_file)
    print(f"[INFO] Deleted old test file")

df.to_excel(excel_file, sheet_name="Sheet1", index=False, engine='openpyxl')
print(f"[SUCCESS] NEW Excel file created: {excel_file}")
print(f"[INFO] Total test steps: {len(test_data['Test_Step_ID'])}")

# Also print the data to verify
print("\n[DATA PREVIEW]")
print(f"  Username: {unique_username}")
print(f"  Password: {password}")
print(f"  Total Steps: {len(test_data['Test_Step_ID'])}")
print(f"  Last Step: {test_data['Action'][-1]}")

# Verify the file was created correctly by reading it back
df_verify = pd.read_excel(excel_file, sheet_name="Sheet1")
print(f"\n[VERIFICATION]")
print(f"  File has {len(df_verify)} rows")
print(f"  Step 5 will enter: {df_verify.loc[4, 'Value']}")
print(f"  Step 12 will enter: {df_verify.loc[11, 'Value']}")
print(f"  Step 16 will verify: {df_verify.loc[15, 'Value']}")