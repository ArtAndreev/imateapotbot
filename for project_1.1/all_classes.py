# list_of_subjects = ['1 - матан', '2 - линал', '3 - тер вер', '4 - бкит', '5 - путон', '6 - элтех']
# list_of_modes = ['1 - скайп', '2 - лично', '3 - самостоятельное решение']
# list_of_tasks = ['1 - рк', '2 - типовик', '3 - текущее дз', '4 - эссе', '5 - лаба', '6 - экзамен']
#
#
# class Task:
#     def __init__(self, name, mode, price=0):
#         self.name = name
#         self.price = price
#         self.mode = mode
#
#     def change_price(self, new_price):
#         self.price = new_price
#
#     def change_mode(self, new_mode):
#         self.mode = new_mode
#
#
# class Subject:
#     tasks = []
#
#     def __init__(self, name):
#         self.name = name
#         self.knowlege = 0
#         self.counter = 0
#
#     def add_task(self, check):  # check отвечает за выбор tutor\student
#         print(list_of_tasks)
#         task_name = list_of_tasks[int(input('выберете номер варианта: '))-1]
#
#         print(list_of_modes)
#         task_mode = list_of_modes[int(input('выберете номер режима: '))-1]
#
#         if check == 'tutor':
#             task_price = input('что вы хотите за выполнение?: ')
#             self.tasks.append(Task(task_name, task_mode, task_price))
#
#         else:
#             self.tasks.append(Task(name=task_name, mode=task_mode))
#
#     def change_knowlege(self, rating):
#         self.counter += 1
#         self.knowlege = (self.knowlege + rating) / self.counter
#
#
# class ListBase:
#
#     def __init__(self):
#         self.tutor = list()
#         self.student = list()
#
#     def add_tutor(self, tut_id):
#         self.tutor.append({'user_id': tut_id,
#                            'subject': list()})
#
#     def add_student(self, stud_id):
#         self.student.append({'user_id': stud_id,
#                              'subject': list()})
#
#     def add_subject(self, check, us_id):
#
#         if check == 'tutor':
#             for person in self.tutor:
#                 if person['user_id'] == us_id:
#                     print(list_of_subjects)
#                     name = list_of_subjects[int(input('выберете номер предмета: '))-1]
#                     person['subject'].append(Subject(name))
#
#                     a = input('добавить задание?(да/нет)')
#
#                     if a == 'да':
#                         i = len(person['subject'])
#                         person['subject'][i - 1].add_task('tutor')
#
#         else:
#             for person in self.student:
#                 if person['user_id'] == us_id:
#                     print(list_of_subjects)
#                     name = list_of_subjects[int(input('выберете номер предмета: '))-1]
#                     person['subject'].append(Subject(name))
#
#                     a = input('добавить задание?(да/нет)')
#
#                     if a == 'да':
#                         i = len(person['subject'])
#                         person['subject'][i - 1].add_task('student')
#
#     def delete_subject(self, us_id, check, name):
#
#         if check == 'tutor':
#
#             for person in self.tutor:
#
#                 if person['user_id'] == us_id:
#
#                     for i in range(len(person['subject'])):
#
#                         if person['subject'].name == name:
#                             person['subject'].pop([i])
#
#     def search_tutor(self):
#         print(list_of_subjects)
#         subject_name = list_of_subjects[int(input('выберете номер предмета: ')) - 1]
#
#         print(list_of_tasks)
#         task_name = list_of_tasks[int(input('выберете номер варианта: ')) - 1]
#
#         print(list_of_modes)
#         task_mode = list_of_modes[int(input('выберете номер режима: ')) - 1]
#
#         knowledge_stuff = int(input('какой процент знаний вас устроит?(от 0 до 100): '))
#
#         for person in self.tutor:
#
#             for subj in person['subject']:
#
#                 if subj.name == subject_name and subj.knowlege >= knowledge_stuff:
#
#                     for task in subj.tasks:
#
#                         if task.name == task_name and task.mode == task_mode:
#
#                             main_list.show_user(person['user_id'])
#
#     # def search_student(self)
#
#
# list_for_searching = ListBase()  # лист со списками туторов и студнтов
#
#
# class Id:
#     def __init__(self):
#         self.counter = 0
#
#     def new_id(self):
#         self.counter += 1
#         return self.counter
#
#
# create_id = Id()  # создает уникальные id
#
#
# class User:
#     # разобраться с connect, photo
#     student = False
#     tutor = False
#
#     def __init__(self):
#         self.name = input('Как тебя зовут?: ')
#         self.faculty = input('С какого ты факультета?: ')
#         self.rat_counter = 0
#         self.karma = 0
#         self.id = create_id.new_id()
#
#         ans_for_student = input('Ты хочешь найти репетитора?(да/нет): ')
#
#         if ans_for_student == 'да':
#             self.student = True
#             list_for_searching.add_student(self.id)
#
#         ans_for_tutor = input('Ты хочешь кому-то помочь?(да/нет): ')
#
#         if ans_for_tutor == 'да':
#             self.tutor = True
#             list_for_searching.add_tutor(self.id)
#
#     def change_karma(self, rating):
#         self.rat_counter += 1
#         self.karma = (self.karma + rating) / self.rat_counter
#
#
# class UserList:
#     users = []
#
#     def add_user(self):
#         self.users.append(User())
#
#     def find_user(self, us_id):
#
#         i = 0
#         for person in self.users:
#
#             if person.id == us_id:
#
#                 return i
#
#         i += 1
#
#     def show_user(self, us_id):
#
#         for person in self.users:
#
#             if person.id == us_id:
#
#                 print('Имя: {}\n Факультет {}\n Карма {}'.format(person))
#
#     # def delete_user(self, check, id)
#
#
# main_list = UserList()
# main_list.add_user()
#
# list_for_searching.add_subject('tutor', main_list.users[0].id)
#
# print('проверка поиска: ')
# list_for_searching.search_tutor()