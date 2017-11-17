from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tables import Base, User, Student, Subject, Tutor, Task,Mode
import users
import request

engine = create_engine('sqlite:///tea_pot.db')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

# new_user = users.create_user('@try')
#
# session.add(new_user)
# session.commit()
#
# new_tutor = request.add_tutor(session,new_user,Tutor,Subject,Task,Mode)
# new_student = request.add_student(session,new_user,Student,Subject,Task,Mode)
#
# session.add(new_student)
# session.add(new_tutor)
# session.commit()

request.search_tutor(session,Subject,Task,Mode,Tutor,User)
request.search_student(session,Subject,Task,Mode,Student,User)