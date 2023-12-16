import requests
from settings import URL
from time import sleep
from sends import send_message


mes = '''Assalomu Alaykum!

Ijodimizga qiziqish bildirganingiz uchun tashakkur!

Hozircha siz uchun futbolka, xudi, svitshot, kepka va stikerlar 
mavjud. Yaqin orada tanlovni kengaytiramiz. Aytganday, istagan 
turdagi kiyim buyurtma berganlarlarga qo'shimcha ravishda 
stikerpak sovg'a qilinadi :)

O'zbekiston bo'ylab yetkazib berish 2-5 ish kunini tashkil qiladi.

Toshkent bo'ylab yetkazib berish - 20 000 so'm.
Ozbekiston bo'ylab yetkazib berish - 30 000 som.

450 000 so'mdan ortiq buyurtmalarni yetkazib berish - tekin!

Agar bu shartlar sizni qoniqtirsa, “🔥 Mahsulotlar” bo'limiga o'tish 
orqali buyurtma berishni boshlashingiz mumkin.'''

def get_last_update(url: str) -> dict:
    endpoint = '/getUpdates'
    url += endpoint
    
    response = requests.get(url)
    if response.status_code == 200:
        result = response.json()['result']

        if len(result) != 0:
            return result[-1]
        else:
            return 404
    
    return response.status_code


def main(url):
    last_update_id = -1
    while True:
        curr_update = get_last_update(url)

        if curr_update['update_id'] != last_update_id:
            user = curr_update['message']['from']
            text = curr_update['message'].get('text')

            if text == "/start":
                btn1 = {
                  "text": "Mahsulotlar",
                }
                btn2 = {
                    "text": "Savat",
                }
                btn3 = {
                    "text": "Hamkorlik",
                }
                btn4 = {
                    "text": "Malumotlar",
                }
                btn5 = {
                    "text": "Tilni tanlang",
                }
                reply_markup = {
                    "keyboard": [
                        [btn1, btn2],
                        [btn3,btn4],
                        [btn5]
                    ],
                    "resize_keyboard": True,
                }
                send_message(url,user["id"],mes,reply_markup)
            elif text == "Malumotlar":
                btn1 = {
                  "text": "Izoh qoldirish",
                }
                btn2 = {
                    "text": "Yetkazish shartlari",
                }
                btn3 = {
                    "text": "Kontaktlar",
                }
                btn4 = {
                    "text": "Bosh menyu",
                }
                reply_markup = {
                    "keyboard": [
                        [btn1],
                        [btn2,btn3],
                        [btn4]
                    ],
                    "resize_keyboard": True,
                }
                send_message(url,user["id"],"Kerakli bo'limni tanlang ⬇️",reply_markup)
            elif text == "Tilni tanlang":
                btn1 = {
                  "text": "Uzbek tili",   
                  "url" : "https://www.google.com/search?q=google+translate"
                }
                btn2 = {
                    "text": "Rus tili",
                    "url":"https://www.google.com/search?q=google+translate"
                }
                reply_markup = {
                    "inline_keyboard": [
                        [btn1],
                        [btn2]
                    ],
                    "resize_keyboard": True,
                }
                send_message(url,user["id"],"Iltimos, tilni tanlang",reply_markup)
            elif text == "Bosh menyu":
                btn1 = {
                  "text": "Mahsulotlar",
                }
                btn2 = {
                    "text": "Savat",
                }
                btn3 = {
                    "text": "Hamkorlik",
                }
                btn4 = {
                    "text": "Malumotlar",
                }
                btn5 = {
                    "text": "Tilni tanlang",
                }
                reply_markup = {
                    "keyboard": [
                        [btn1, btn2],
                        [btn3,btn4],
                        [btn5]
                    ],
                    "resize_keyboard": True,
                }
                send_message(url,user["id"],mes,reply_markup)
            last_update_id = curr_update['update_id']

        sleep(0.5)
main(URL)
