
from cgitb import reset


class Flight:

    def __init__(self, seats) -> None:
        self.seats = seats
        self.pasangers = []

    def add_pasanger(self, pasanger):
        if not self.open_seat():
            return False
        self.pasangers.append(pasanger)
        return True

    def open_seat(self):
        return self.seats - len(self.pasangers)


pasangers = ['ali', 'arash', 'sara', 'amir']

flight = Flight(3)
for person in pasangers:
    if flight.add_pasanger(person):
        print(f"{person} added to the flight")
    else:
        print(f"no available seat for{person}")