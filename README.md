# Pixelverse Auto Battle Bot

Pixelverse Auto Battle Bot is an automated battle bot for Pixelverse. It includes functionalities for managing pets, engaging in battles, and displaying user statistics.

### Buy me Coffee ☕ 
```
0x705C71fc031B378586695c8f888231e9d24381b4
```

## Fix some fuction (7/8/2024): 

In this update: (`https://t.me/zddfs`)

- Added checks for the presence of keys in the stats dictionary `new`

- Fixed update_user_info function to handle missing keys `new`

- Updated strings so that the code can work correctly with parameters from the query string `new`

 - Fix superHit `new`
 - Remove "tg id" and "secret" `new`
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
- argument (--upgrade) to activate upgrade_pets `NEW`

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
    git clone https://github.com/jawikas/pixelverse-auto-battle.git
    cd pixelverse-auto-battle
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Configure the bot by editing or create the `config.json` file with your own credentials:
    ```json
   {
       "secret": "", "tgId": "",
       "initData": "YourQuery_id=xxxxisHere",
       "upgrade_pets": false,
       "min_hit_speed": 0.09,
       "max_hit_speed": 0.111
   }
    ```
( Update 7/7/2024 ) reduce the need for "tg id" and "secret" because now it is automatically executed in Battle.py, and you only need to enter the Query ID into config.json

Please Leave "tg id" and "secret" blank

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

### Note : Please Leave "tg id" and "secret" blank (only need your Query_id)

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
