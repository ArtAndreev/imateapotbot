import sqlite3
import subjects_stuff


class ListBase:

    def __init__(self):
        self.tutor = list()
        self.student = list()

    def add_tutor(self, tut_id):
        self.tutor.append({'user_id': tut_id,
                           'subject': list()})

    def add_student(self, stud_id):
        self.student.append({'user_id': stud_id,
                             'subject': list()})

    def add_subject(self, check, us_id):

        if check == 'tutor':
            for person in self.tutor:
                if person['user_id'] == us_id:
                    print(subjects_stuff.list_of_subjects)
                    name = subjects_stuff.list_of_subjects[int(input('выберете номер предмета: '))-1]
                    person['subject'].append(subjects_stuff.Subject(name))

                    a = input('добавить задание?(да/нет)')

                    if a == 'да':
                        i = len(person['subject'])
                        person['subject'][i - 1].add_task('tutor')

        else:
            for person in self.student:
                if person['user_id'] == us_id:
                    print(subjects_stuff.list_of_subjects)
                    name = subjects_stuff.list_of_subjects[int(input('выберете номер предмета: '))-1]
                    person['subject'].append(subjects_stuff.Subject(name))

                    a = input('добавить задание?(да/нет)')

                    if a == 'да':
                        i = len(person['subject'])
                        person['subject'][i - 1].add_task('student')

    def delete_subject(self, us_id, check, name):

        if check == 'tutor':

            for person in self.tutor:

                if person['user_id'] == us_id:

                    for i in range(len(person['subject'])):

                        if person['subject'].name == name:
                            person['subject'].pop([i])

    def search_tutor(self, search_list):
        print(subjects_stuff.list_of_subjects)
        subject_name = subjects_stuff.list_of_subjects[int(input('выберете номер предмета: ')) - 1]

        print(subjects_stuff.list_of_tasks)
        task_name = subjects_stuff.list_of_tasks[int(input('выберете номер варианта: ')) - 1]

        print(subjects_stuff.list_of_modes)
        task_mode = subjects_stuff.list_of_modes[int(input('выберете номер режима: ')) - 1]

        knowledge_stuff = int(input('какой процент знаний вас устроит?(от 0 до 100): '))

        for person in self.tutor:

            for subj in person['subject']:

                if subj.name == subject_name and subj.knowlege >= knowledge_stuff:

                    for task in subj.tasks:

                        if task.name == task_name and task.mode == task_mode:

                            search_list.show_user(person['user_id'])
                            print('цена: {}'.format(task.price))

    # def search_student(self)


list_for_searching = ListBase() # лист со списками туторов и студнтов
