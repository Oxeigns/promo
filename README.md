# Promo Main Bot

Promo Main is a Telegram bot that lets users promote their Telegram groups using a join‑for‑join credit system. Users earn credits by joining other groups and spend credits to promote their own. Payments are handled manually through UPI transactions so the bot can run on free hosting without payment gateways.

## Features
- Join‑for‑join promotion system
- Manual UPI payment workflow
- Admin commands for approving or banning users
- Simple credit tracking with MongoDB
- Start and menu commands with inline buttons

## Folder Structure
```
.
├── database/        # MongoDB connection and query helpers
├── handlers/        # Pyrogram event handlers
├── utils/           # Helper utilities (buttons, config, logger, markdown)
├── main.py          # Bot entry point
├── requirements.txt
├── runtime.txt
└── Procfile (optional)
```

## Setup
1. Clone the repository and install the requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Copy `sample.env` to `.env` and fill in your bot token, API credentials and MongoDB URL.
3. Run the bot locally with:
   ```bash
   python main.py
   ```
   The bot will start and keep running until interrupted.

### Deployment
The project includes a `runtime.txt` and `Procfile` to make it easy to deploy on platforms such as Heroku. Ensure environment variables from `.env` are configured on the platform.

## Manual Payment System
Payments are collected manually. Users send money using the displayed UPI address and then run `/paid <transaction_id>` in the bot. The admin reviews the transaction and upgrades the user by running `/approve <user_id>`.

## Credits
This project is built using [Pyrogram](https://docs.pyrogram.org/) and requires MongoDB for data storage.
