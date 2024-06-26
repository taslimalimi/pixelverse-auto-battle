# Pixelverse Auto Battle Bot

Pixelverse Auto Battle Bot is an automated battle bot for Pixelverse. It includes functionalities for managing pets, engaging in battles, and displaying user statistics.

## Features

- Automated pet upgrades
- Real-time battle automation
- User statistics display
- Configurable settings via `config.json`

## Requirements

- Python 3.8+
- The following Python packages:
  - `certifi==2024.6.2`
  - `charset-normalizer==3.3.2`
  - `colorama==0.4.6`
  - `idna==3.7`
  - `requests==2.32.3`
  - `urllib3==2.2.1`
  - `websockets==12.0`

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/jawikas/pixelverse.git
    cd pixelverse
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Configure the bot by editing the `config.json` file with your own credentials:
    ```json
    {
        "secret": "your_secret_key",
        "tgId": "your_telegram_id",
        "initData": "your_init_data",
        "upgrade_pets": true
    }
    ```

## Usage

Run the bot using the following command:
```bash
python main.py
