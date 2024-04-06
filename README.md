# Pyrogram Auto Name and Bio Changer

This Python script utilizes the Pyrogram library to automatically change the last name and bio of a Telegram account at regular intervals. It utilizes the aiocron library for scheduling the task.

## Requirements

- Python 3.x
- Pyrogram
- aiocron

## Installation

1. Install Python if you haven't already. You can download it from [python.org](https://www.python.org/downloads/).
2. Install the required libraries using pip:

    ```
    pip install pyrogram aiocron
    ```

## Configuration

1. Obtain `api_id`, `api_hash`, and `phone_number` from [Telegram's website](https://my.telegram.org/auth).
2. Replace `'ايبي ايدي'`, `'ايبي هاش'`, and `'+964 رقمك'` with your `api_id`, `api_hash`, and `phone_number` respectively.
3. Customize `time_zone` to your preferred timezone. The default is set to "Asia/Baghdad".
4. Customize `fonts` if you wish to use different characters for your name and bio.

## Usage

1. Run the script:

    ```
    python main.py
    ```

2. The script will automatically start changing the last name and bio of your Telegram account at regular intervals.

## Important Notes

- Ensure that your Telegram account is registered with the phone number provided in the configuration.
- Be cautious with the interval frequency to avoid rate limiting or other issues with the Telegram API.
- Make sure to handle errors gracefully, especially in case of network issues or API limitations.
