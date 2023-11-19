from prac_09.musician import Musician
from prac_09.guitar import Guitar


class Band:
    def __init__(self, name=""):
        self.name = name
        self.members = []

    def __str__(self):  # Not Finished
        return f"{self.name} {self.members[0]}"

    def __repr__(self):
        return str(self)

    def add(self, member):
        self.members.append(member)

    def play(self):
        members_playing = ""  # Feels like could be done differently
        for member in self.members:
            members_playing += Musician.play(member) + "\n"
        return members_playing
