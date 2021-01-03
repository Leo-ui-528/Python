class Worker:

    def __init__(self, name='Ivan', surname='Ivanov', position='engineer', wage=100, bonus=20):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_full_salary(self):
        return self._income['wage'] + self._income['bonus']


t = Position('Иван', 'Иванов', 'engineer', 110, 30)
print(f'New attributes are: {t.name}, {t.surname}, {t.position}, {t._income}')
print(f'Total salary of {t.get_full_name()} is {t.get_full_salary()}')