from route import Route
from user import User

class Thing():

    def __init__(self) -> None:
        pass


    def add_route(self):
        
        grade = input("give grade: ")
        location = input("give location: ")
        # climber = self.user

        new_route = Route(grade, location)

        # todo: add to database


    def add_user(self):

        name = input("give name: ")
        password = input("give password: ")

        new_user = User(name, password)

        # todo: do something with this

if __name__=="__main__":
    try_out = Thing()
    try_out.add_user()
    try_out.add_route()
