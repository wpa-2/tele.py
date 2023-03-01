#!/usr/bin/python3
import sys
sys.path.append('/home/wpa2/.local/lib/python3.9/site-packages')
import telegram
import requests

def is_valid_bot_id(bot_id):
    try:
        response = requests.get(f"https://api.telegram.org/bot{bot_id}/getMe")
        if response.status_code == 200:
            return True
        return False
    except:
        return False

def is_valid_chat_id(bot_id, chat_id):
    try:
        response = requests.get(f"https://api.telegram.org/bot{bot_id}/sendMessage?chat_id={chat_id}&text=Valid_details")
        if response.status_code == 200:
            return True
        return False
    except:
        return False

def send_message(bot_id, chat_id, message):
    requests.get(f"https://api.telegram.org/bot{bot_id}/sendMessage?chat_id={chat_id}&text={message}")

bot_id = "BOT_ID GOES HERE"
chat_id = "CHAT_ID GOES HERE"

bot_valid = is_valid_bot_id(bot_id)
chat_valid = is_valid_chat_id(bot_id, chat_id)

if bot_valid:
    bot_result = "Valid bot_id"
else:
    bot_result = "Invalid bot_id"

if chat_valid:
    chat_result = "Valid chat_id"
else:
    chat_result = "Invalid chat_id"

send_message(bot_id, chat_id, f"Bot ID Check Result: {bot_result}\nChat ID Check Result: {chat_result}")
