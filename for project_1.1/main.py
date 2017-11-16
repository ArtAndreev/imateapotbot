import users_stuff
import search_stuff

import sqlite3

# con_users = sqlite3.connect('bot_base.db')
# cur_users = con_users.cursor()
list_for_searching = search_stuff.ListBase()

main_list = users_stuff.UserList()

print('добавление человека: ')
main_list.users.append(users_stuff.User(list_for_searching))
list_for_searching.add_subject('tutor',main_list.users[0].id)
print()
print('запрос на поиск репетитора: ')
list_for_searching.search_tutor(main_list)
print()
print('оценка репетитора:')
rat = input('добавьте плюсики в карму репетитора(0-100): ')
main_list.users[0].change_karma(int(rat))
main_list.show_user(1)