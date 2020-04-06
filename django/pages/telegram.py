from django.conf import settings
import requests
import logging


def send_text(text):

    if not all([settings.TELEGRAM_API_KEY, settings.TELEGRAM_CHAT_ID]):
        logging.warning("No Telegram settings, aborting message send")
        return

    url = "https://api.telegram.org/bot{token}/sendMessage"
    url = url.format(token=settings.TELEGRAM_API_KEY)

    data = {
        "chat_id": settings.TELEGRAM_CHAT_ID,
        "parse_mode": "Markdown",
    }

    data["text"] = text

    requests.post(url, data=data)
