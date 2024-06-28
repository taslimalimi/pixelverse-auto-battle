# Pixelverse Auto Battle Bot

Pixelverse Auto Battle Bot is an automated battle bot for Pixelverse. It includes functionalities for managing pets, engaging in battles, and displaying user statistics.

## fix some fuction (6/28/2024): 

 - update upgrade_pet fuction
 - add argument (--upgrade)
 - add min & max hit speed configuration
 - update config.json
 - update balance after fight

## Features

- Automated pet upgrades
- Real-time battle automation
- User statistics display
- Configurable settings via `config.json`
- min & max hit speed configuration `NEW`
- argument (--upgrade) to activate upgrade_pets

## Requirements

- Python 3.8+ (recomended)
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
        "upgrade_pets": false,
        "min_hit_speed": 0.1,
        "max_hit_speed": 0.12
    }
    ```

## Usage

Run the bot using the following command:
```bash
python main.py
```
Run the bot & UPGRADE_PET fuction with Fuction following command:
```bash
python main.py --upgrade
```
## Config.json data?
You need some data for config.json, please follow the steps below:
- Goto telegram website and open the app bots
- Press ```F12``` on your keyboard to open ```devtool``` or right click on app and ```select Inspect```

![image](https://github.com/jawikas/pixelverse/assets/63976518/d9f08858-e650-4605-86ad-48367ab13f7d)

## File Descriptions
```
api_pet.py
Handles interactions with the Pixelverse API, including fetching user data, statistics, pets, and performing pet upgrades.

Battle.py
Contains the Battle class, which manages the websocket connection for battles, handles sending hits, and listening to messages from the server.

core.py
Main logic for the bot, including user information updates and battle initiation. It utilizes the UserPixel class from api_pet.py and the Battle class from Battle.py.

main.py
Entry point for the bot. It initializes and runs the main asynchronous loop defined in core.py.

requirements.txt
List of required Python packages for the project.

config.json
Configuration file containing necessary credentials and settings for the bot.
```

## License
This project is licensed under the NONE License.

## Contact
If you have any questions or suggestions, please feel free to contact at [ https://t.me/itsjaw_real ].

## Thanks to
Template based by [akasakaid]([url](https://github.com/akasakaid)) & [adearman]([url](https://github.com/adearman))

- https://github.com/adearman
- https://github.com/akasakaid
