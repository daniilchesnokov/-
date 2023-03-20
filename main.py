import telebot
import time
import sqlite3
from telebot import types
books = sqlite3.connect('books.db')
sqlbooks = books.cursor() #объявляем таблицу и даём возможность управления
def connect():
    global books
    global sqlbooks
    books = sqlite3.connect('books.db')
    sqlbooks = books.cursor()
bot = telebot.TeleBot("5897613855:AAFfeweFNCtGmi8tzf_zsNbcI_34GsL-e5I")

botRegister = '-1001846131574'
botTeh = '-760778011'
worker = '5838451409'














#---------------------------------------------------Основной код--------------------------------------------------------



#------------------------------------------------старт и регистрация----------------------------------------------------
@bot.message_handler(commands=['start'])
def send_start(message):
    bot.send_message(message.chat.id, 'Привет! Я твой электронный помощник в библиотеке МАОУ СОШ №33 \nВерсия 0.00.1\nДля получения информации /info\nНажми /reg')





@bot.message_handler(commands=['reg'])
def red1(message):
    people_id = message.chat.id
    books = sqlite3.connect('books.db')
    sqlbooks = books.cursor()
    sqlbooks.execute(f"SELECT id FROM users WHERE id = {people_id}")
    data = sqlbooks.fetchone()
    if data is None:
        msg = bot.send_message(message.chat.id, 'Заполни информацию о себе \nНапример: "Иванов Иван 8 А" ')
        bot.register_next_step_handler(msg, reg2)
    else:
        bot.send_message(message.chat.id, 'Ты зарегистрирован')





def reg2(message):

    a = message.text
    a = a.split()
    role = 'Ученик'
    id_book = '-'
    id = message.chat.id
    books = sqlite3.connect('books.db')
    sqlbooks = books.cursor()
    sqlbooks.execute(f"INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?)", (id, a[0], a[1], a[2], a[3], role, id_book ))
    books.commit()
    bot.send_message(message.chat.id, 'Пользователь успешно зарегистрирован!')
    mess = str(id)+' '+str(a[0])+' '+str(a[1])+' '+str(a[2])+' '+str(a[3])
    bot.send_message(botRegister, mess)






#---------------------------------------------поиск по фамилии----------------------------------------------------------
@bot.message_handler(commands=['searchsurname'])
def send_searchsurname(message):
    msg = bot.send_message(message.chat.id, 'Введи интересующую тебя фамилию автора')
    bot.register_next_step_handler(msg, searchsurname)
def searchsurname(message):

    connect()
    sql = "SELECT title FROM books WHERE surname = ?"
    sqlbooks.execute(sql, (message.text,))
    items = sqlbooks.fetchall()
    if items == []:
        bot.send_message(message.chat.id, 'Такого автора нет')
    else:
        for el in items:
            bot.send_message(message.chat.id, el)










#------------------мой профиль------------------------------------------------------------------------------------------




@bot.message_handler(commands=['profile'])
def profile(message):
    books = sqlite3.connect('books.db')
    sqlbooks = books.cursor()
    id1 = message.chat.id
    sql = "SELECT surname FROM users WHERE id = ?"
    sqlbooks.execute(sql, (id1,))
    items = sqlbooks.fetchall()
    for el in items:
        el = str(el)
        el = el.replace('(', '')
        el = el.replace(')', '')
        el = el.replace(',', '')
        el = el.replace("'", '')
        v = 'Фамилия- ' + str(el)
        bot.send_message(message.chat.id, v)


    sql1 = "SELECT name FROM users WHERE id = ?"
    sqlbooks.execute(sql1, (id1,))
    items = sqlbooks.fetchall()
    for el in items:
        el = str(el)
        el = el.replace('(', '')
        el = el.replace(')', '')
        el = el.replace(',', '')
        el = el.replace("'", '')
        v = 'Имя- ' + str(el)
        bot.send_message(message.chat.id, v)


    sql2 = "SELECT clas FROM users WHERE id = ?"
    sqlbooks.execute(sql2, (id1,))
    items = sqlbooks.fetchall()
    for el in items:
        el = str(el)
        el = el.replace('(', '')
        el = el.replace(')', '')
        el = el.replace(',', '')
        el = el.replace("'", '')
        v = 'Класс- ' + str(el)
        bot.send_message(message.chat.id, v)

    sql3 = "SELECT liter FROM users WHERE id = ?"
    sqlbooks.execute(sql3, (id1,))
    items = sqlbooks.fetchall()
    for el in items:
        el = str(el)
        el = el.replace('(', '')
        el = el.replace(')', '')
        el = el.replace(',', '')
        el = el.replace("'", '')
        v = 'Литер- ' + str(el)
        bot.send_message(message.chat.id, v)






#---------------------------------------поиск по назвванию и вывод инфы по ней------------------------------------------
@bot.message_handler(commands=['searchtitle'])
def send_searchtitle(message):
    msg = bot.send_message(message.chat.id, 'Введи интересующую тебя книгу')
    bot.register_next_step_handler(msg, searchtitle)
def searchtitle(message):
    connect()
    sql = "SELECT surname FROM books WHERE title = ?"
    sqlbooks.execute(sql, (message.text,))
    items = sqlbooks.fetchall()
    if items == []:
        bot.send_message(message.chat.id, 'Такой книги нет')
    else:
        connect()

        sql0 = "SELECT id FROM books WHERE title = ?"
        sqlbooks.execute(sql0, (message.text,))
        items = sqlbooks.fetchall()

        for el in items:
            el = str(el)
            el = el.replace('(', '')
            el = el.replace(')', '')
            el = el.replace(',', '')
            el = el.replace("'", '')
            v0 = 'ID- ' +  str(el)
            bot.send_message(message.chat.id, v0)



        sql = "SELECT surname FROM books WHERE title = ?"
        sqlbooks.execute(sql, (message.text,))
        items = sqlbooks.fetchall()


        for el in items:
            el = str(el)
            el = el.replace('(', '')
            el = el.replace(')', '')
            el = el.replace(',', '')
            el = el.replace("'", '')
            v = 'Автор- ' +str(el)
            bot.send_message(message.chat.id, v)


            sql1 = "SELECT genre FROM books WHERE title = ?"
            sqlbooks.execute(sql1, (message.text,))
            items = sqlbooks.fetchall()
            for el in items:
                el = str(el)
                el = el.replace('(', '')
                el = el.replace(')', '')
                el = el.replace(',', '')
                el = el.replace("'", '')
                v1 = 'Жанр- ' +str(el)
                bot.send_message(message.chat.id, v1)


                sql2 = "SELECT ywriting FROM books WHERE title = ?"
                sqlbooks.execute(sql2, (message.text,))
            items = sqlbooks.fetchall()
            for el in items:
                el = str(el)
                el = el.replace('(', '')
                el = el.replace(')', '')
                el = el.replace(',', '')
                el = el.replace("'", '')
                v2 = 'Год написания- ' +str(el)
                bot.send_message(message.chat.id, v2)


                sql3 = "SELECT quantily FROM books WHERE title = ?"
                sqlbooks.execute(sql3, (message.text,))
            items = sqlbooks.fetchall()
            for el in items:
                el = str(el)
                el = el.replace('(', '')
                el = el.replace(')', '')
                el = el.replace(',', '')
                el = el.replace("'", '')
                v3 = 'Количество- ' +str(el)
                bot.send_message(message.chat.id, v3)



                sql4 = "SELECT description FROM books WHERE title = ?"
                sqlbooks.execute(sql4, (message.text,))
            items = sqlbooks.fetchall()
            for el in items:
                el = str(el)
                el = el.replace('(', '')
                el = el.replace(')', '')
                el = el.replace(',', '')
                el = el.replace("'", '')
                v4 = 'Описание: ' +str(el)
                bot.send_message(message.chat.id, v4)

















#-----------------получение книги---------------------------------------------------------------------------------------



@bot.message_handler(commands=['get'])
def reg(message):
    print('get')
    ida = int(message.chat.id)
    print(ida)

    books = sqlite3.connect('books.db')
    sqlbooks = books.cursor()

    sql = "SELECT id_book FROM users WHERE id = ?"
    sqlbooks.execute(sql, (ida,))
    nalbook = sqlbooks.fetchone()
    el = nalbook
    el = str(el)
    el = el.replace('(', '')
    el = el.replace(')', '')
    el = el.replace(',', '')
    el = el.replace("'", '')
    nalbook = el
    print(nalbook)
    if nalbook != '-':
        bot.send_message(message.chat.id, 'У тебя уже есть книга \nСдай книгу чтоб взять новую')

    else:
        sql = "SELECT surname FROM users WHERE id = ?"
        sqlbooks.execute(sql, (ida,))
        surname = sqlbooks.fetchone()
        el = surname
        el = str(el)
        el = el.replace('(', '')
        el = el.replace(')', '')
        el = el.replace(',', '')
        el = el.replace("'", '')
        surname = el
        print(surname)

        sql = "SELECT name FROM users WHERE id = ?"
        sqlbooks.execute(sql, (ida,))
        name = sqlbooks.fetchone()
        el = name
        el = str(el)
        el = el.replace('(', '')
        el = el.replace(')', '')
        el = el.replace(',', '')
        el = el.replace("'", '')
        name = el
        print(name)

        sql = "SELECT clas FROM users WHERE id = ?"
        sqlbooks.execute(sql, (ida,))
        clas = sqlbooks.fetchone()
        el = clas
        el = str(el)
        el = el.replace('(', '')
        el = el.replace(')', '')
        el = el.replace(',', '')
        el = el.replace("'", '')
        clas = el
        print(clas)

        sql = "SELECT liter FROM users WHERE id = ?"
        sqlbooks.execute(sql, (ida,))
        liter = sqlbooks.fetchone()
        el = liter
        el = str(el)
        el = el.replace('(', '')
        el = el.replace(')', '')
        el = el.replace(',', '')
        el = el.replace("'", '')
        liter = el
        print(liter)



        sqlbooks.execute(f"INSERT INTO time VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (ida, name, surname, clas, liter, 0, 0,0 ))
        print('id_user')
        books.commit()

        msg = bot.send_message(message.chat.id, 'Какую книгу ты хочешь получить?' )
        bot.register_next_step_handler(msg, reg1)



def reg1(message):
    title_book = message.text
    print(title_book)
    ida = int(message.chat.id)
    print(ida)

    books = sqlite3.connect('books.db')
    sqlbooks = books.cursor()



    sql = "SELECT name FROM users WHERE id = ?"
    sqlbooks.execute(sql, (ida,))
    name = sqlbooks.fetchone()
    el = name
    el = str(el)
    el = el.replace('(', '')
    el = el.replace(')', '')
    el = el.replace(',', '')
    el = el.replace("'", '')
    name = el
    print(name)

    sql = "SELECT surname FROM users WHERE id = ?"
    sqlbooks.execute(sql, (ida,))
    surname = sqlbooks.fetchone()
    el = surname
    el = str(el)
    el = el.replace('(', '')
    el = el.replace(')', '')
    el = el.replace(',', '')
    el = el.replace("'", '')
    surname = el
    print(surname)

    sql = "SELECT clas FROM users WHERE id = ?"
    sqlbooks.execute(sql, (ida,))
    clas = sqlbooks.fetchone()
    el = clas
    el = str(el)
    el = el.replace('(', '')
    el = el.replace(')', '')
    el = el.replace(',', '')
    el = el.replace("'", '')
    clas = el
    print(clas)

    sql = "SELECT liter FROM users WHERE id = ?"
    sqlbooks.execute(sql, (ida,))
    liter = sqlbooks.fetchone()
    el = liter
    el = str(el)
    el = el.replace('(', '')
    el = el.replace(')', '')
    el = el.replace(',', '')
    el = el.replace("'", '')
    liter = el
    print(liter)


    sql = "SELECT id FROM books WHERE title = ?"
    sqlbooks.execute(sql, (title_book,))
    id_book = sqlbooks.fetchone()
    el = id_book
    el = str(el)
    el = el.replace('(', '')
    el = el.replace(')', '')
    el = el.replace(',', '')
    el = el.replace("'", '')
    id_book = el
    print(id_book)

    if id_book == 'None':
        bot.send_message(message.chat.id, 'Такой книги нет в нашей библиотеке')

    else:
        id_book = int(id_book)
        print(id_book)
        sql = "SELECT quantily FROM books WHERE title = ?"
        sqlbooks.execute(sql, (title_book,))
        quantily = sqlbooks.fetchone()
        el = quantily
        el = str(el)
        el = el.replace('(', '')
        el = el.replace(')', '')
        el = el.replace(',', '')
        el = el.replace("'", '')
        quantily = el
        quantily = int(quantily)
        print(quantily)

        if quantily < 1:
            bot.send_message(message.chat.id, 'В данный момент этой книги нет')

        else:
            ida = int(message.chat.id)
            books = sqlite3.connect('books.db')
            sqlbooks = books.cursor()
            sql = "UPDATE time SET id_book = ? WHERE id_user = ?"
            sqlbooks.execute(sql, (id_book, ida,))
            books.commit()

            sql = "SELECT title FROM books WHERE id = ?"
            sqlbooks.execute(sql, (id_book,))
            title_book = sqlbooks.fetchone()
            el = title_book
            el = str(el)
            el = el.replace('(', '')
            el = el.replace(')', '')
            el = el.replace(',', '')
            el = el.replace("'", '')
            title_book = el
            print(title_book)
            sql = "UPDATE time SET title_book = ? WHERE id_user = ?"
            sqlbooks.execute(sql, (title_book, ida,))
            books.commit()

            sql = "SELECT surname FROM books WHERE id = ?"
            sqlbooks.execute(sql, (id_book,))
            surname_book = sqlbooks.fetchone()
            el = surname_book
            el = str(el)
            el = el.replace('(', '')
            el = el.replace(')', '')
            el = el.replace(',', '')
            el = el.replace("'", '')
            surname_book = el
            print(surname_book)
            sql = "UPDATE time SET surname_book = ? WHERE id_user = ?"
            sqlbooks.execute(sql, (surname_book, ida,))
            books.commit()










            buttons = types.InlineKeyboardMarkup(row_width=2)
            mess = 'Выдать книгу "'+title_book+'"\nУченик- '+surname+' '+name+' '+clas+liter+'?'
            ida = str(ida)
            but1 = 'yes'+ida
            but2 = 'no'+ida
            button1 = types.InlineKeyboardButton('ДА', callback_data=but1)
            button2 = types.InlineKeyboardButton('НЕТ', callback_data=but2)
            buttons.add(button1, button2)
            bot.send_message(worker, text=mess, reply_markup=buttons)





@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    books = sqlite3.connect('books.db')
    sqlbooks = books.cursor()
    el = call.data
    el = str(el)
    el = el.replace('0', '')
    el = el.replace('1', '')
    el = el.replace('2', '')
    el = el.replace("3", '')
    el = el.replace('4', '')
    el = el.replace('5', '')
    el = el.replace('6', '')
    el = el.replace("7", '')
    el = el.replace('8', '')
    el = el.replace('9', '')
    cback = el
    print(cback)

    el = call.data
    el = str(el)
    el = el.replace('y', '')
    el = el.replace('e', '')
    el = el.replace('s', '')
    el = el.replace("n", '')
    el = el.replace('o', '')
    id_user = el
    id_user = str(id_user)
    print(id_user)

    if cback == 'no':
        bot.send_message(id_user, 'К сожалению ты сейчас не можешь получить книгу')
        sql = "UPDATE time SET id_user = 0 WHERE id_user = ?"
        sqlbooks.execute(sql, (id_user,))
        books.commit()

        sqlbooks.execute("DELETE FROM time WHERE id_user = 0")
        books.commit()
        print('Запись удалена')

    elif cback == 'yes':

        sql = "SELECT id_book FROM time WHERE id_user = ?"
        sqlbooks.execute(sql, (id_user,))
        id_book = sqlbooks.fetchone()
        el = id_book
        el = str(el)
        el = el.replace('(', '')
        el = el.replace(')', '')
        el = el.replace(',', '')
        el = el.replace("'", '')
        id_book = el
        print(id_book)

        sql = "UPDATE users SET id_book = ? WHERE id = ?"
        sqlbooks.execute(sql, (id_book, id_user,))
        books.commit()
        bot.send_message(id_user, 'Поздравляю с получением книги')

        sql = "UPDATE time SET id_user = 0 WHERE id_user = ?"
        sqlbooks.execute(sql, (id_user,))
        books.commit()

        sqlbooks.execute("DELETE FROM time WHERE id_user = 0")
        books.commit()
        print('Запись удалена')






@bot.message_handler(commands=['info'])
def send_info(message):
    bot.send_message(message.chat.id, 'Поиск произведений по фамилии автора /searchsurname'
                                      '\nМой профиль /profile'
                                      '\nПоиск книги по названию /searchtitle'
                                      '\nПолучить книгу /get'
                                      '\nВернуть книгу /revert')


@bot.message_handler(commands=['revert'])
def revert(message):
    bot.send_message(message.chat.id, 'У тебя нет книг для возврата')













































if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            time.sleep(1)
            print(e)

