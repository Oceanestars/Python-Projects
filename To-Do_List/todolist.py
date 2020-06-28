# Write your code here
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()
class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())
    def __repr__(self):
        return self.task
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
rows = session.query(Table).order_by(Table.deadline).all()
today = datetime.today()

def alltask():
    task_counter = 0
    if not rows:
        print('Nothing to do!')
    for i in rows:
        task_counter += 1
        first_row = i
        print(str(task_counter) + '. ' + first_row.task + '. ' + str(i.deadline.day)
                      + ' ' + i.deadline.strftime('%b'))
    print('\n')

def todolist():
    print("1) Today's tasks")
    print("2) Week's tasks")
    print("3) All tasks")
    print("4) Missed tasks")
    print("5) Add task")
    print("6) Delete task")
    print("0) Exit")
todolist()
user_choice = int(input())
while user_choice != 0:
    if user_choice == 1:
        counter = 0
        rows_today = session.query(Table).filter(Table.deadline == today.date()).all()
        print("Today",today.day, today.strftime('%b') + ':')
        if len(rows_today) != 0:
            for i in range(0, len(rows_today)):
                counter += 1
                first_row = rows_today[i]
                print(str(counter) + ". " + str(first_row.task))
            counter = 0
            todolist()
            user_choice = int(input())
        else:
            print("Nothing to do!")
            todolist()
            user_choice = int(input())
    elif user_choice == 2:
        task_counter = 0
        for i in range(0,8):
            day_week = today + timedelta(days=i) # a timedelta object represents a duration, the difference between two dates or times.
            print('\n')
            print(day_week.strftime('%A'), day_week.day,day_week.strftime('%b') + ':')
            rows_week = session.query(Table).filter(Table.deadline == day_week.date()).all()
            if len(rows_week) == 0:
                print("Nothing to do!")
            if len(rows_week) != 0:
                for i in range(0, len(rows_week)):
                    task_counter += 1
                    first_row = rows_week[i]
                    print(str(task_counter) + ". " + str(first_row.task))
                task_counter = 0
        todolist()
        user_choice = int(input())
    elif user_choice == 3:
        alltask()
        todolist()
        user_choice = int(input())
    elif user_choice == 4:
        task_counter = 0
        rows_missed = session.query(Table).filter(Table.deadline < datetime.today()).all()
        print("Missed tasks:")
        if len(rows_missed) == 0:
            print("Nothing is missed!")
        if len(rows_missed) != 0:
            for i in rows_missed:
                task_counter += 1
                first_row = i
                print(str(task_counter) + '. ' + first_row.task + '. ' + str(i.deadline.day)
                           + ' ' + i.deadline.strftime('%b'))
            task_counter = 0
        print('\n')
        todolist()
        user_choice = int(input())
    elif user_choice == 5:
        enter = input("Enter task\n")
        new_deadline = input("Enter deadline\n")
        new_task = Table(task=enter, deadline=datetime.strptime(new_deadline, '%Y-%m-%d').date())
        session.add(new_task)
        session.commit()
        print("The task has been added!\n")
        todolist()
        user_choice = int(input())
    elif user_choice == 6:
        task_counter = 0
        print("Chose the number of the task you want to delete:")
        if not rows:
            print('Nothing to do!')
        for i in rows:
            task_counter += 1
            first_row = i
            print(str(task_counter) + '. ' + first_row.task + '. ' + str(i.deadline.day)
                          + ' ' + i.deadline.strftime('%b'))
        delete_num = int(input())
        specific_row = rows[delete_num-1] # in case rows is not empty
        session.delete(specific_row)
        session.commit()
        print("The task has been deleted!\n")
        todolist()
        user_choice = int(input())
    elif user_choice == 0:
        exit()
print("Bye!")
