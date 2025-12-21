from abc import ABC, abstractmethod

# SOLID: Single Responsibility
class User:
    def __init__(self, name):
        self.name = name

class UserRepository:
    def save(self, user):
        print(f"Saving {user.name} to DB")

class EmailService:
    def send(self, user, msg):
        print(f"Sending email to {user.name}: {msg}")

# SOLID: Interface Segregation
class Workable(ABC):
    @abstractmethod
    def work(self): pass

class Eatable(ABC):
    @abstractmethod
    def eat(self): pass

class Human(Workable, Eatable):
    def work(self): return "Working"
    def eat(self): return "Eating"

class Robot(Workable):
    def work(self): return "Working"

if __name__ == "__main__":
    user = User("Bob")
    repo = UserRepository()
    repo.save(user)
    
    email = EmailService()
    email.send(user, "Welcome!")
    
    human = Human()
    print(human.work(), human.eat())
    
    robot = Robot()
    print(robot.work())
