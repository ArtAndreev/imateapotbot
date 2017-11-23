from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tables import Base, User, Student, Subject, Tutor, Task,Mode, Deal
import users
import request

engine = create_engine('sqlite:///tea_pot.db')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()


def deal_rating(stud_id, req_id, stud_karma, tut_karma, rating):
    deal = session.query(Deal).filter(Deal.student_id == stud_id,
                                                 Deal.request_id == req_id).first()
    deal.student_karma = stud_karma
    deal.knowledge_rating = rating
    deal.tutor_karma = tut_karma
    deal.status = 'end'
    users.change_karma(session, User, stud_id, stud_karma)
    users.change_karma(session, User, tut_karma, stud_karma)
    request.change_knowledge(session, Tutor, req_id, rating)


# new_user = users.create_user(session, '@try')
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

# request.search_tutor(session,Subject,Task,Mode,Tutor,User)
# request.search_student(session,Subject,Task,Mode,Student,User)
