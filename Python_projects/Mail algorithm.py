import json


class Mails:

    def __init__(self):
        # transfer self.data to registration section
        self.login = False

    def registration(self):
        print('РЕГИСТРАЦИЯ\n')
        reg_login = input("Введите логин: ")
        if len(reg_login) == 0:
            print("Поле логин не может быть пустым")
            Mails.registration(self)
        try:
            with open(reg_login + '.json', 'r') as file:
                ...  # we check if the same login already exist and saved in json.
            let_login = False  # if it is false then file does not exist
        except:
            let_login = True  # if it is true then
        if let_login:  # we ask to registrate password
            reg_password = input("Введите пароль: ")
            if len(reg_password) == 0:
                print("Поле 'пароль' не может быть пустым")
                Mails.registration(self)

            self.data = {}  # create self.data after registration
            self.data[reg_login] = {}
            self.data[reg_login]['password'] = reg_password
            self.data[reg_login]['in_mails'] = {}
            self.data[reg_login]['out_mails'] = {}

            with open(reg_login + '.json',
                      'w') as user_file:  # Create JSON file. We don't have it but we create it through adding extend .son to reg_loging
                json.dump(self.data, user_file)

            print('Вы успешно зарегестрировались!\n')
        else:
            print("Такой логин уже есть")
            user_qw = input('0 - перейти ко входу')
            if user_qw == '0':
                Mails.enter(self)
            else:
                Mails.registration(self)
        Mails.enter(self)

    def enter(self):
        print('ВХОД\n')
        login = input("Введите логин: ")
        password = input("Введите пароль: ")
        if login not in self.data:
            print("Пользователя с таким логином не существует,\nПовторте попытку или зарегистрируйтесь.")
            user_qw = input('1: Попробовать снова | 2: Регистрация')
            if user_qw == '1':
                Mails.enter(self)
            else:
                Mails.registration(self)
        else:
            if password == self.data[login]['password']:
                print("Вход выполнен успешно!")
                self.login = login

                with open(login + '.json',
                          'r') as user_file:  # we read Json file if person check his email and doesn`t need registration
                    self.data = json.load(user_file)

            self.letters = self.data[login]['in_mails']
            Mails.main_menu(self)

        print("Вы ввели неверный пароль, повторите попытку.")
        Mails.enter(self)

    def main_menu(self):
        print('ГЛАВНОЕ МЕНЮ\n')
        if self.login == False:
            Mails.registration(self)
        else:
            print('''
                1: Просмотреть входящие письма
                2: Написать письмо
                3: Просмотреть отправленные письма''')
            user_qw = input('Ваш выбор:  ')
            if user_qw == '1':
                Mails.see_mails(self)
            elif user_qw == '2':
                Mails.new_message(self)
            elif user_qw == '3':
                print('Такая функция еще не реализована')
                Mails.main_menu(self)
            elif user_qw.lower().strip() == 'выход':
                return
            else:
                print('Такого варианта нет')
                Mails.main_menu(self)

    def see_mails(self):
        for i in self.letters:
            print(i, ":", self.letters[i])
        user_qw = input('Если хотите посмотреть письмо, напишите его номер:  ')
        if user_qw in self.letters:
            Mails.see_message(self, user_qw)
        else:
            Mails.main_menu(self)

    def see_message(self, key):
        print(self.letters[key])
        user_qw = input('1: Вернуться назад | 2: Главное меню')
        if user_qw == '1':
            Mails.see_mails(self)
        else:
            Mails.main_menu(self)

    def new_message(self):
        topic = input('Введите тему черновика: ')
        if topic == '':
            topic = 'Без темы'
        draft = input('Введите текст черновика: ')
        if draft == '':
            draft = 'Пустое сообщение'
        to_who = input('Введите имя пользователя:  ')
        try:  # it is possible that data of reciever doesn`t registered. Then we transfer him on new message. if 'Try' works then we open user's json file. if it 'Try' doesn't work then we will transfer user to part "Except"
            # we change self.data in in_mails and out_mails. that is why we should rewrite json file. We open file of reciever
            # we change self.data on reciever because self.data was transfered from global to registration section.
            # it means that now it is not general. it contains only our data. That is why we cannot use it for another person.
            # we write smth to reciever. It means we change json file.

            # 1) open json file of reciever:
            with open(to_who + '.json', 'r') as user_file:
                reciever = json.load(user_file)
            print('Прочитал собеседника')

            # 2) update dct of reciever:
            reciever[to_who]['in_mails'][str(len(reciever[to_who]['in_mails']) + 1)] = topic + ' | ' + draft
            print('обновил его словарь')

            # 3) rewrite json file of reciever:
            with open(to_who + '.json', 'w') as user_file:
                json.dump(reciever, user_file)
            print('записал ему письмо')

            # 1) open own json file :
            with open(self.login + '.json', 'r') as user_file:
                self.data = json.load(user_file)
            print('прочитал тебя')

            # 2) update own dct:
            self.data[self.login]['out_mails'][str(len(self.data[self.login]['out_mails']) + 1)] = topic + ' | ' + draft
            print('обновил твой словарик')

            # 3) rewrite own json file
            with open(self.login + '.json', 'w') as user_file:
                json.dump(self.data, user_file)

            print('Сообщение', to_who, 'отправлено успешно!')
            Mails.main_menu(self)

        except:
            print('Такого пользователя не существует')
            Mails.main_menu(self)


me = Mails()

me.registration()
