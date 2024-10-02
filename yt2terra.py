import os
import time
from pytube import YouTube
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import tkinter as tk
from tkinter import messagebox
import ssl
import certifi


def download_youtube_video(url, download_path):
    try:
        # Use certifi certificate bundle
        ssl_context = ssl.create_default_context(cafile=certifi.where())
        yt = YouTube(url, ssl_context=ssl_context)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=download_path)
        print(f"Downloaded {yt.title} to {download_path}")
        return os.path.join(download_path, stream.default_filename)
    except Exception as e:
        messagebox.showerror("Download Error", f"An error occurred: {e}")
        return None


def upload_to_terabox_via_google(email, password, file_path):
    # Initialize the Chrome WebDriver
    service = Service(
        executable_path="path/to/chromedriver")  # Update with the path to your chromedriver
    driver = webdriver.Chrome(service=service)

    try:
        driver.get("https://www.terabox.com/")
        wait = WebDriverWait(driver, 10)

        # Click the login button
        login_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Login']")))
        login_button.click()

        # Click on the Google Sign-In button
        google_login_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='sign-in-btn'][@data-service='google']")))
        google_login_button.click()

        # Handle the Google Sign-In process
        # Switch to Google login window
        driver.switch_to.window(driver.window_handles[1])

        email_field = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//input[@type='email']")))
        email_field.send_keys(email)
        email_field.send_keys(Keys.RETURN)

        time.sleep(2)  # Adjust based on network speed

        password_field = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//input[@type='password']")))
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)

        # Switch back to the main window
        driver.switch_to.window(driver.window_handles[0])

        # Navigate to the upload section
        upload_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@data-action='upload']")))
        upload_button.click()

        # Upload the file
        file_input = driver.find_element(By.XPATH, "//input[@type='file']")
        file_input.send_keys(file_path)

        time.sleep(10)  # Wait for the upload to complete (adjust as necessary)
        messagebox.showinfo("Success", "Upload completed")

    except TimeoutException as e:
        messagebox.showerror("Timeout Error", f"An error occurred: {e}")
    finally:
        driver.quit()


def start_process():
    youtube_url = yt_url_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not youtube_url or not email or not password:
        messagebox.showerror("Input Error", "Please fill in all fields")
        return

    download_path = "./downloads"  # Specify your download directory

    # Ensure download path exists
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    # Download YouTube video
    video_file = download_youtube_video(youtube_url, download_path)

    # Upload to Terabox via Google Sign-In
    if video_file:
        upload_to_terabox_via_google(email, password, video_file)


# GUI Setup
root = tk.Tk()
root.title("YouTube to Terabox Uploader")

# YouTube URL
tk.Label(root, text="YouTube URL:").grid(row=0, column=0, padx=10, pady=10)
yt_url_entry = tk.Entry(root, width=50)
yt_url_entry.grid(row=0, column=1, padx=10, pady=10)

# Google Email
tk.Label(root, text="Google Email:").grid(row=1, column=0, padx=10, pady=10)
email_entry = tk.Entry(root, width=50)
email_entry.grid(row=1, column=1, padx=10, pady=10)

# Google Password
tk.Label(root, text="Google Password:").grid(row=2, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, show="*", width=50)
password_entry.grid(row=2, column=1, padx=10, pady=10)

# Start Button
start_button = tk.Button(root, text="Start", command=start_process)
start_button.grid(row=3, column=0, columnspan=2, pady=20)

# Run the application
root.mainloop()
