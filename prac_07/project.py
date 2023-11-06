"""
Estimated: 4hrs
Actual: 5hrs
"""


class Project:
    """Represent a Project object."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise a Project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        """Return a string containing project information."""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate}, " \
               f"completion: {self.completion_percentage}%"

    def __gt__(self, other):
        """Compare project years."""
        return self.start_date > other.start_date

    def update_percentage(self, new_percentage):
        """Update percentage."""
        self.completion_percentage = new_percentage
