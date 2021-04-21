from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""I am **{bn}** !!
Grubunuzun sesli sohbetinde müzik çalmanıza izin 😉
Şu anda desteklediğim komutlar şunlardır:
⚜️ /play - yanıtlanan ses dosyasını veya YouTube videosunu link.__ aracılığıyla __oynatılır
⚜️ /pause - Sesli Sohbet Music.__ __Durdurur
⚜️ /resume - sesli sohbet Music.__ __Devam ettirir
⚜️ /skip - Geçerli Ses Atlanır.__ Çalan Müzik __atlanır
⚜️ /stop - Sırayı __Temizler ve Sesli Sohbet Müziklerin listesini kaldırır.__
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "☕Grup☕", url="https://t.me/sohbetskyfall"
                    ),
                    InlineKeyboardButton(
                        "🗣️Kanal🗣️", url="https://t.me/kanalEfsanestar"
                    ),                    
                    InlineKeyboardButton(
                        "👤Sahip👤", url="https://t.me/EfsaneStar" 
                    ), 
                ]
            ]
        )
    )
