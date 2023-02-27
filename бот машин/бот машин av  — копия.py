import time
import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import json


bot = telebot.TeleBot('');

dict_admins = {}
dict_forward = {}
dict_data = {}
dict_del ={}


# словарь админов
def check_admin2():

    dict_admins[810809759] = {'user_name': 'pasha', 'rights': True}
    dict_admins[647012868] = {'user_name': 'UITAAP22', 'rights': False}


check_admin2()

# главная клавиатура
inline_markup_main = InlineKeyboardMarkup()
inline_btn_33 = InlineKeyboardButton('Список администраторов', callback_data='c1')
inline_btn_11 = InlineKeyboardButton('Изменить администратора', callback_data='b0')
inline_btn_22 = InlineKeyboardButton('Удалить администратора', callback_data='c0')
inline_markup_main.add(inline_btn_33)
inline_markup_main.add(inline_btn_11)
inline_markup_main.add(inline_btn_22)



inline_markup_n_admin = InlineKeyboardMarkup()
inline_btn_1 = InlineKeyboardButton('Администратор', callback_data='f0')
inline_btn_2 = InlineKeyboardButton('Супер администратор', callback_data='g0')
inline_markup_n_admin.add(inline_btn_1, inline_btn_2)



inline_markup_avto = InlineKeyboardMarkup()
inline_btn_add_car = InlineKeyboardButton('Добавить автомобиль', callback_data='h0')
inline_btn_change_car = InlineKeyboardButton('Изменить автомобиль', callback_data='i0')
inline_btn_del_car = InlineKeyboardButton('Удалить автомобиль', callback_data='u0')
inline_markup_avto.add(inline_btn_add_car)
inline_markup_avto.add(inline_btn_change_car)
inline_markup_avto.add(inline_btn_del_car)



inline_markup_del_admin = InlineKeyboardMarkup()
inline_btn_del_admin = InlineKeyboardButton('Удалить', callback_data='j0')
inline_btn_del_admin2 = InlineKeyboardButton('Отмена', callback_data='l0')
inline_markup_del_admin.add(inline_btn_del_admin, inline_btn_del_admin2)



inline_markup_change_ad = InlineKeyboardMarkup()
inline_btn_change_ad1 = InlineKeyboardButton('Изменить', callback_data='o0')
inline_btn_change_ad2 = InlineKeyboardButton('Отмена', callback_data='p0')
inline_markup_change_ad.add(inline_btn_change_ad1, inline_btn_change_ad2)



# изменение админов
def keyb_change_ad():
    inline_markup_change_ad2 = InlineKeyboardMarkup()
    for k, v in dict_admins.items():
        inline_markup_change_ad2.add(InlineKeyboardButton((v['user_name']), callback_data=f'o1{k}'))
    return inline_markup_change_ad2

# удаление админов
def keyb_del_ad():
    inline_markup_del_ad2 = InlineKeyboardMarkup()
    for k, v in dict_admins.items():
        inline_markup_del_ad2.add(InlineKeyboardButton((v['user_name']), callback_data=f'n0{k}'))
    return inline_markup_del_ad2


inline_markup_delete_admin = InlineKeyboardMarkup()
inline_btn_del_adminn = InlineKeyboardButton('Удалить', callback_data='n1')
inline_markup_delete_admin.add(inline_btn_del_adminn)



inline_markup_change_admin = InlineKeyboardMarkup()
inline_btn_change_admin1 = InlineKeyboardButton('Изменить имя', callback_data='t0')
inline_btn_change_admin2 = InlineKeyboardButton('Изменить права', callback_data='y0')
inline_markup_change_admin.add(inline_btn_change_admin1, inline_btn_change_admin2)



inline_markup_rights_admin = InlineKeyboardMarkup()
inline_btn_right_admin1 = InlineKeyboardButton('Администратор', callback_data='t1')
inline_btn_right_admin2 = InlineKeyboardButton('Супер администратор', callback_data='y1')
inline_markup_rights_admin.add(inline_btn_right_admin1, inline_btn_right_admin2)


@bot.message_handler(content_types=['text'])
def start(message):

    if message.text == '/start':
        bot.send_message(message.chat.id, "Проверка на администратора...")
        check_admin(message)




    if message.text == '/newadmin':
        if message.chat.id in dict_admins and dict_admins[message.chat.id]['rights'] == True:
            bot.send_message(message.chat.id, "Перешлите сообщение и укажите уровень прав нового администратора")
    new_admin(message)


    if message.text == '/stat':
        if message.chat.id in dict_admins and dict_admins[message.chat.id]['rights'] == True:
            bot.send_message(message.chat.id, "Вот вся статистика")


    if message.text == '/newcar':
        if message.chat.id in dict_admins:
            bot.send_message(message.chat.id, "Выберите действие с автомобилем", reply_markup=inline_markup_avto)

    if message.text == '/help':
        bot.send_message(message.chat.id, "Здесь должна быть помощь")



# добваление администаторов
def new_admin(message):
    if message.chat.id in dict_admins and dict_admins[message.chat.id]['rights'] == True:
        try:
            forward_id = message.forward_from.id

            forward_username = message.forward_from.username

            dict_forward[message.chat.id] = forward_id, forward_username

            bot.send_message(message.chat.id, "Укажите уровень прав", reply_markup=inline_markup_n_admin)

        except:
            pass




# проверка на админа
def check_admin(message):
    try:
        if message.chat.id in dict_admins and dict_admins[message.chat.id]['rights'] == True:
            bot.send_message(message.chat.id, "Вы супер администратор", reply_markup=inline_markup_main)
    except:
        pass

    try:
        if message.chat.id in dict_admins and dict_admins[message.chat.id]['rights'] == False:
            bot.send_message(message.chat.id, "Вы администратор")
    except:
        pass

    try:
        if message.chat.id not in dict_admins:
            bot.send_message(message.chat.id, "Вы не админостратор")
    except:
        pass


# изменение имени админа
def new_name_ad(message):
    dict_admins[int(dict_data[message.chat.id])] = {'user_name': message.text, 'rights': dict_admins[int(dict_data[message.chat.id])]['rights']}
    bot.send_message(message.chat.id, "Администратор изменён")
    print(dict_admins)





@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id, )
    id = call.message.chat.id
    flag = call.data[0:2]
    data = call.data[2:]



    if flag == 'c1':
        for k, v in dict_admins.items():
            bot.send_message(id, f"Имя пользователя: {v['user_name']} \nУровень прав: {v['rights']}")


    if flag == 'b0':
        bot.send_message(id, "Вы действительно хотите изменить администратора?", reply_markup=inline_markup_change_ad)


    if flag == 'o0':
        bot.send_message(id, "Выберите администратора, которого хотите изменить", reply_markup=keyb_change_ad())




    if flag == 'o1':
        dict_data[id] = data
        print("dict_data", dict_data)
        # print(data)
        bot.send_message(id, f"Имя пользователя: {dict_admins[int(data)]['user_name']} \nУровень прав: "
                             f"{dict_admins[int(data)]['rights']}", reply_markup=inline_markup_change_admin)



    if flag == 't0':
        new_name = bot.send_message(id, "Укажите новое имя")
        bot.register_next_step_handler(new_name, new_name_ad)
        with open('dict_admins.json', 'w', encoding='utf-8') as f:
            json.dump(dict_admins, f, ensure_ascii=False, indent=4)

        f = open('dict_admins.json', 'r', encoding='utf-8')
        d = json.loads(f.read())
        f.close()
        print(d)
        print(dict_admins)


    if flag == 'y0':
        bot.send_message(id, "Укажите права", reply_markup=inline_markup_rights_admin)
        with open('dict_admins.json', 'w', encoding='utf-8') as f:
            json.dump(dict_admins, f, ensure_ascii=False, indent=4)

        f = open('dict_admins.json', 'r', encoding='utf-8')
        d = json.loads(f.read())
        f.close()
        print(d)

    if flag == 't1':
        dict_admins[int(dict_data[id])] = {'user_name': dict_admins[int(dict_data[id])]['user_name'], 'rights': False}
        bot.send_message(id, "Администратор добавлен")
        with open('dict_admins.json', 'w', encoding='utf-8') as f:
            json.dump(dict_admins, f, ensure_ascii=False, indent=4)

        f = open('dict_admins.json', 'r', encoding='utf-8')
        d = json.loads(f.read())
        f.close()
        print(d)
        print(dict_admins)


    if flag == 'y1':
        dict_admins[int(dict_data[id])] = {'user_name': dict_admins[int(dict_data[id])]['user_name'], 'rights': True}
        bot.send_message(id, "Супер администратор добавлен")
        with open('dict_admins.json', 'w', encoding='utf-8') as f:
            json.dump(dict_admins, f, ensure_ascii=False, indent=4)

        f = open('dict_admins.json', 'r', encoding='utf-8')
        d = json.loads(f.read())
        f.close()
        print(d)
        print(dict_admins)


    if flag == 'p0':
        bot.send_message(id, "Отмена изменения")


    if flag == 'c0':
        # bot.send_message(id, call.message.id)
        bot.send_message(id, "Вы действительно хотите удалить администратора?", reply_markup=inline_markup_del_admin)


    if flag == 'j0':
        bot.send_message(id, "Выберите администратора, которого хотите удалить", reply_markup=keyb_del_ad())


    if flag == 'n0':
        dict_del[id] = data
        print(dict_del)
        bot.send_message(id, f"Имя пользователя: {dict_admins[int(data)]['user_name']} \nУровень прав: "
                             f"{dict_admins[int(data)]['rights']}", reply_markup=inline_markup_delete_admin)


    if flag == 'n1':
        dict_admins.pop(int(dict_del[id]))
        bot.send_message(id, "Администратор удалён")
        with open('dict_admins.json', 'w', encoding='utf-8') as f:
            json.dump(dict_admins, f, ensure_ascii=False, indent=4)

        f = open('dict_admins.json', 'r', encoding='utf-8')
        d = json.loads(f.read())
        f.close()
        print(d)
        print(dict_admins)


    if flag == 'l0':
        bot.send_message(id, "Отмена удаления")


    if flag == 'f0':
        for k, v in dict_forward.values():
            pass
        dict_admins[k] = {'user_name': v, 'rights': False}
        bot.send_message(id, "Администратор добавлен")
        # print(dict_admins[forward_id])
        # print(forward_id)
        with open('dict_admins.json', 'w', encoding='utf-8') as f:
            json.dump(dict_admins, f, ensure_ascii=False, indent=4)

        f = open('dict_admins.json', 'r', encoding='utf-8')
        d = json.loads(f.read())
        f.close()
        print(d)
        print(dict_admins)
        dict_forward.popitem()
        # print(dict_forward)

    if flag == 'g0':
        for k, v in dict_forward.values():
            pass
        dict_admins[k] = {'user_name': v, 'rights': True}
        bot.send_message(id, "Супер администратор добавлен")
        with open('dict_admins.json', 'w', encoding='utf-8') as f:
            json.dump(dict_admins, f, ensure_ascii=False, indent=4)

        f = open('dict_admins.json', 'r', encoding='utf-8')
        d = json.loads(f.read())
        f.close()
        print(d)
        print(dict_admins)
        dict_forward.popitem()


print("Ready")
bot.infinity_polling()


