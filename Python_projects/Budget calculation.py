# defaultdict (module collection) - this method allows you to check do you have requered key or not. If you don't have then this methode offers you key by default

class BudgetSaver:

    def __init__(self, budget=0):  # we create example "budget" for methode init
        self.budget = budget  # if we made busget as self.budget then it becomes accessable for all methodes
        self.dct = {}

    def flow(self, summa, categoria, agent, date):  # date: '21.02.22'
        self.budget += summa
        tuple_date = tuple(
            date.split('.'))  # Split is used for STR and return data in massive. We turn it in touple (cortage)
        if tuple_date not in self.dct.keys():  # if this date is available in keys of dct - self.dct

         self.dct[tuple_date] = {} # if date doesn't exists among keys then dictionary is empty

        # if date exists among keys then we check operations for this date
        # we need create keys in kind of operations
        # when we apply to dictionary by key like self.dct[tuple_date] we recieve value.
        # what value contains in this case - new internal dictionary with own keys.
        # If we apply to dictionary by key and by index - we recieve key of internal dictionary self.dct[tuple_date][str(len(self.dct[tuple_date]))
        # [str(len(self.dct[tuple_date]))] - is index for keys of internal dictionary. We turn index in str.
        # assign other new keys to each key of internal dictionary

        self.dct[tuple_date][str(len(self.dct[tuple_date]))] = {
            'summa': summa,
            'categoria': categoria,
            'agent': agent
        }

    def show(self, period='all'):  # period='all' means all operations for whole period
        if self.dct == {}:  # 1.
            print('Операций нет')
        elif period == 'all':  # 2.
            for date in self.dct:  # 3.
                print('-'.join(date))  # through "-" join touple of dates which are in str. Join works only with str.
                print()
                for transaction in self.dct[
                    date]:  # 4. self.dct[date] - we call internal massive where "transaction" is runung by key (operations index) of internal massive
                    operation = self.dct[date][
                        transaction]  # 5.self.dct[date][transaction]- calls value of last dictionary
                    print('Категория:', operation['categoria'])  # 6. shows values of key "catergory"
                    print('Агент:', operation['agent'])  # 7. shows values of key "agent"
                    print('Сумма:', operation['summa'])  # 8. shows values of key "sum"
                    print()
                print('----------------------')
                print()

my_wallet = BudgetSaver()

my_wallet.flow(100, 'Нашел', 'Незнакомец', '20.02.22')

my_wallet.flow(-100, 'Потерял', 'Я', '21.02.22')

my_wallet.flow(100000, 'Google', 'Сергей Брин', '22.02.22')

my_wallet.flow(-80000, 'Яндекс', 'YandexHR', '23.02.22')

for i, k in my_wallet.dct.items():#.dct.items() - create touples with 2 elements. First (i or date) - keys, second (k or internal dcts)- values.
                                  #self.dct = {} was defined in the begining
    print(i)
    print(k)
    print()

my_wallet.show()

my_wallet.flow(-300, 'Fastfood', 'Starbaks', '21.02.22')
my_wallet.flow(500, 'Fastfood', 'Qwerty', '23.02.22')

my_wallet.dct

my_wallet.show()