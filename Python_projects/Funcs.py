import random as rd

people = [['name', 'sex', 'age', 'city']]
for i in range(1000):

    # create empty massive for each person
    # before each runung this massive becomes empty

    vr = []

    # [*'йцукенгшщзхфывапролджэячсмитбю'] - open this massive.
    # k=5 - choose 5 different letters from above massive
    # ''.join - join different letter

    name = ''.join(rd.choices([*'йцукенгшщзхфывапролджэячсмитбю'], k = 5))
    vr.append(name)
    sex = rd.choice(['m', 'f'])
    vr.append(sex)
    age = rd.randint(18, 69)
    vr.append(age)
    city = rd.choice(['msk', 'spb', 'ekb', 'smr', 'ntg', 'nvsb'])
    vr.append(city)

    people.append(vr)  # add to first general massive people add all small arrays for each person VR

print(people[:10]) # print first 10 people


def sql(array, column, value):  # create format of sql
    '''...
    ///
    ;;;'''
    # 0 element in array is first massive in above ['name', 'sex', 'age', 'city']
    # now columns has the name of columns of array

    columns = array[0]
    if column in columns:
        #         result = []
        column_id = columns.index(
            column)  # index where is required column place. Age column is 2nd index in all internal massives
        #         for row in array[1:]:            #starting from second internal massive
        #             if row[column_id] == value:  #row is small internal massives
        #                 result.append(row)
        result = [row for row in array[1:] if row[column_id] == value]  # short way of cycle
        return result
    else:
        print('Такой колонки', column, 'нет')

print(sql(people, 'age', 18))