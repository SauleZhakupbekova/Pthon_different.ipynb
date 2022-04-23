import random as rd
people = [['name', 'sex', 'age', 'city']]
for i in range(1000):
    # create empty massive for each person
    # before each runung this massive becomes empty

    vr = []

    # [*'йцукенгшщзхфывапролджэячсмитбю'] - open this massive.
    # k=5 - choose 5 different letters from above massive
    # ''.join - join different letter

    name = ''.join(rd.choices([*'йцукенгшщзхфывапролджэячсмитбю'], k=5))
    vr.append(name)
    sex = rd.choice(['m', 'f'])
    vr.append(sex)
    age = rd.randint(18, 69)
    vr.append(age)
    city = rd.choice(['msk', 'spb', 'ekb', 'smr', 'ntg', 'nvsb'])
    vr.append(city)

    # add to first general massive people add all small massives for each person VR

    people.append(vr)

# print first 10 people
people[:10]