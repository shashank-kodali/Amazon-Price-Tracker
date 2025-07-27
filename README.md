# Amazon Price Tracker

A simple Python script that monitors the price of a specific product on Amazon India and sends an email notification if the price drops to or below a predefined target.

## ✨ Features

  * **Price Monitoring:** Automatically fetches the current price of a specified Amazon product.
  * **Email Alerts:** Sends an email alert if the product's price meets or falls below your desired buying price.
  * **Secure Credentials:** Utilizes environment variables to keep your email and other sensitive credentials secure.
  * **Easy to Use:** Set it up once and let it run (e.g., via a scheduler like Cron or Windows Task Scheduler).

## 🚀 Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

  * Python 3.x (Tested with Python 3.10+)
  * `pip` (Python package installer)

### Installation

1.  **Clone the repository (or create the files manually):**

    ```bash
    git clone https://github.com/your-username/amazon-price-tracker.git # Replace with your repo URL
    cd amazon-price-tracker
    ```

    If you're not using Git, simply create a folder and place your `main.py` file inside it.

2.  **Create a `requirements.txt` file:**
    In the same directory as your `main.py` file, create a file named `requirements.txt` and add the following lines:

    ```
    requests
    beautifulsoup4
    python-dotenv
    ```

3.  **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

## ⚙️ Configuration

This script relies on environment variables for sensitive information like email credentials and the recipient's email.

1.  **Create a `.env` file:**
    In the root directory of your project (where `main.py` is located), create a file named `.env`.

2.  **Add your environment variables to `.env`:**
    Populate the `.env` file with your details. Make sure there are no spaces around the `=` sign.

    ```dotenv
    SMTP_ADDRESS=smtp.gmail.com           # Or your email provider's SMTP address (e.g., smtp.mail.yahoo.com)
    EMAIL_ADDRESS=your_sending_email@gmail.com # Your email address (the one sending the alerts)
    EMAIL_PASSWORD=your_app_password      # Your email password or app password (RECOMMENDED for Gmail/Outlook)
    TO_EMAIL=your_recipient_email@example.com # The email address to receive the alerts
    ```

    **Important Note on `EMAIL_PASSWORD`:**

      * **Gmail:** If you use Gmail and have 2-Factor Authentication (2FA) enabled (which you should\!), you'll need to generate an **App Password** for your script. You can do this in your Google Account security settings. Using your regular Gmail password directly is often blocked.
      * **Other Providers:** Check your email provider's documentation for "App Passwords" or "less secure app access" if you encounter login issues.

3.  **Update the Product URL and Target Price in `main.py`:**
    Open `main.py` and modify the `URL` and `BUY` variables to match your desired product and target price.

    ```python
    URL = "https://www.amazon.in/CMF-NOTHING-Buds-Dirac-Tuned-Bluetooth/dp/B0FFN49G12/" # Change to your product URL
    # ...
    BUY = 2200 # Set your desired maximum buying price here
    ```

## 🚀 Usage

To run the script, simply execute `main.py` from your terminal:

```bash
python main.py
```

You can set up a cron job (Linux/macOS) or a scheduled task (Windows) to run this script periodically (e.g., once a day, every hour) to continuously monitor the price.

## 🤝 How it Works

1.  **Loads Environment Variables:** Uses `python-dotenv` to load configuration from the `.env` file.
2.  **Fetches Webpage:** Sends an HTTP GET request to the specified Amazon product URL, mimicking a web browser using custom `headers`.
3.  **Parses HTML:** Uses `BeautifulSoup` to parse the received HTML content.
4.  **Extracts Data:** Locates the product price (using class `a-price-whole`) and title (using ID `productTitle`) from the parsed HTML. It then cleans the price string by removing commas and dots, converting it to a float.
5.  **Compares Price:** Checks if the extracted `price` is less than or equal to the `BUY` threshold.
6.  **Sends Email:** If the condition is met, it connects to your specified SMTP server, logs in, and sends an email alert containing the product title and current sale price.

## ⚠️ Troubleshooting

  * **`AttributeError: 'NoneType' object has no attribute 'getText'`**:
    This means `BeautifulSoup` could not find the HTML element with the specified class (`a-price-whole`) or ID (`productTitle`). Amazon frequently changes its HTML structure and class names.
    **Solution:**

    1.  Go to the product page in your browser.
    2.  Right-click on the price/title and select "Inspect" (or "Inspect Element").
    3.  Find the current `class` or `id` of the element containing the price/title.
    4.  Update `soup.find(class_="a-price-whole")` or `soup.find(id="productTitle")` in your `main.py` file with the new values.

  * **Email not sending / `smtplib.SMTPAuthenticationError`**:

      * Double-check your `SMTP_ADDRESS`, `EMAIL_ADDRESS`, `EMAIL_PASSWORD`, and `TO_EMAIL` in the `.env` file.
      * For Gmail users, ensure you are using an **App Password** if you have 2FA enabled.
      * Ensure your internet connection is active and there are no firewall rules blocking outgoing connections on port 587.

  * **`ValueError: could not convert string to float`**:
    This indicates that the price string obtained from the website has an unexpected format that your `.replace(",", "").replace(".", "")` logic can't handle.
    **Solution:** Print the `price_text_raw` variable just before the cleaning steps to see its exact format and adjust the cleaning logic accordingly.

  * **Script not getting the correct product page (e.g., CAPTCHA or empty page)**:
    Amazon (and other e-commerce sites) have anti-bot measures. The `header` might not be sufficient to mimic a real browser perfectly.
    **Solution:** You might need to experiment with different `User-Agent` strings (use a current browser's User-Agent) or consider adding delays between requests if you plan to scrape multiple items. For more advanced cases, tools like `Selenium` or `Playwright` might be necessary, as they simulate a full browser.

-----

## **Disclaimer:** Web scraping can be against a website's Terms of Service. Please use this script responsibly and ethically. The author is not responsible for any misuse.
