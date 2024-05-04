# Telegram bot for ird prediction

To use this bot follow this steps:

1. Clone this repo

```bash
git clone https://github.com/glitchheadgit/tgbot_ird_prediction
```

2. Create `data` folder

```bash
cd tgbot_ird_prediction;
mkdir data
```

3. Download [model file](https://drive.google.com/file/d/1rESkF6b0fyyaGn-Wk-0zP8dIXlc4RiTk) in it
4. Create `.env` file with your telegram bot API token
```bash
echo BOT_TOKEN=your_token > .env
```
5. Install dependencies
```bash
pip install -r requirements.txt
```
7. Start `bot.py`
```bash
python3 bot.py
```
