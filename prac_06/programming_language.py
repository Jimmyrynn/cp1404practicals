class ProgrammingLanguage:
    """Represent a Language object."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a Language instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determines if typing is dynamic."""
        if self.typing == "Dynamic":
            return True
        else:
            return False

    def __str__(self):
        """Returns a string containing language information"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
