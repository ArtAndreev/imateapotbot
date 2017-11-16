list_of_subjects = ['1 - матан', '2 - линал', '3 - тер вер', '4 - бкит', '5 - путон', '6 - элтех']
list_of_modes = ['1 - скайп', '2 - лично', '3 - самостоятельное решение']
list_of_tasks = ['1 - рк', '2 - типовик', '3 - текущее дз', '4 - эссе', '5 - лаба', '6 - экзамен']


class Task:
    def __init__(self, name, mode, price=0):
        self.name = name
        self.price = price
        self.mode = mode

    def change_price(self, new_price):
        self.price = new_price

    def change_mode(self, new_mode):
        self.mode = new_mode


class Subject:
    tasks = []

    def __init__(self, name):
        self.name = name
        self.knowlege = 0
        self.counter = 0

    def add_task(self, check):  # check отвечает за выбор tutor\student
        print(list_of_tasks)
        task_name = list_of_tasks[int(input('выберете номер варианта: '))-1]

        print(list_of_modes)
        task_mode = list_of_modes[int(input('выберете номер режима: '))-1]

        if check == 'tutor':
            task_price = input('что вы хотите за выполнение?: ')
            self.tasks.append(Task(task_name, task_mode, task_price))

        else:
            self.tasks.append(Task(name=task_name, mode=task_mode))

    def change_knowlege(self, rating):
        self.counter += 1
        self.knowlege = (self.knowlege + rating) / self.counter
