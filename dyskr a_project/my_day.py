import random
from enum import Enum

class State(Enum):
    SLEEP = 1
    AWAKE = 2
    PANIC = 3
    EAT = 4
    WORK = 5
    RELAX = 6

class FiniteStateMachine:
    def __init__(self):
        self.state = State.SLEEP
    def transition(self, hour):
        event = random.random()
        if self.state == State.SLEEP:
            if event > 0.5 and hour == 7:
                print("Ah.. a good new day!")
                self.state = State.AWAKE
            elif hour == 8:
                print("Oh no, I shouldn't drank so much yesterday...")
                self.state = State.PANIC
            else:
                print("Zzzz.....")
        elif self.state== State.PANIC:
            if hour == 9 and event > 0.7:
                print("Ahh man, I realy want to eat, let's grab some sandwich")
                self.state = State.EAT
            else:
                print("Ahhh i don't have time even to eat, i have to hury for work")
                self.state=State.WORK
        elif self.state == State.AWAKE:
            if hour == 8:
                print("Feeling hungry, time to nyam nyam!")
                self.state = State.EAT
        elif self.state == State.EAT:
            if hour == 14:
                print("Lunch is done, back to work!")
                self.state = State.WORK
            elif hour == 9:
                print("Good... time to start working")
                self.state = State.WORK
        elif self.state == State.WORK:
            if event < 0.2 and 13<=hour<=18:
                print("Feeling tired, time to relax")
                self.state = State.RELAX
            elif hour == 18:
                print("Work done, time to relax!")
                self.state = State.RELAX
            elif hour==13:
                print("Well I should go grab something to eat")
                self.state=State.EAT
            else:
                print("Code...")
        elif self.state == State.RELAX:
            if hour == 22:
                print("Time to sleep...")
                self.state = State.SLEEP
            else:
                print("Scroling Tik Tok")

def simulate_day():
    fsm = FiniteStateMachine()
    for hour in range(24):
        fsm.transition(hour)

simulate_day()
