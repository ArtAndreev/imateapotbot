class Id:
    def __init__(self):
        self.counter = 0

    def new_id(self):
        self.counter += 1
        return self.counter


create_id = Id()  # создает уникальные id


class User:
    # разобраться с connect, photo
    student = False
    tutor = False

    def __init__(self,search_list):
        self.name = input('Как тебя зовут?: ')
        self.faculty = input('С какого ты факультета?: ')
        self.rat_counter = 0
        self.karma = 0
        self.id = create_id.new_id()

        ans_for_student = input('Ты хочешь найти репетитора?(да/нет): ')

        if ans_for_student == 'да':
            self.student = True
            search_list.add_student(self.id)

        ans_for_tutor = input('Ты хочешь кому-то помочь?(да/нет): ')

        if ans_for_tutor == 'да':
            self.tutor = True
            search_list.add_tutor(self.id)

    def change_karma(self, rating):
        self.rat_counter += 1
        self.karma = (self.karma + rating) / self.rat_counter


class UserList:
    users = []

    def add_user(self):
        self.users.append(User())

    def find_user(self, us_id):

        i = 0
        for person in self.users:

            if person.id == us_id:

                return i

        i += 1

    def show_user(self, us_id):

        for person in self.users:

            if person.id == us_id:

                print('Имя: {}\n Факультет {}\n Карма {}'.format(person.name,person.faculty,person.karma))

    # def delete_user(self, check, id)