# event.py

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0  # Initialize participant count

    def add_participant(self):
        """Increase the participant count by 1."""
        self.participant_count += 1
        print(f"Participant added. Current count: {self.participant_count}.")

    def get_participant_count(self):
        """Return the current participant count."""
        return self.participant_count

# Demonstration script
if __name__ == "__main__":
    # Creating Event instance
    event1 = Event("City Marathon", "2024-05-01")

    # Display initial participant count
    print(f"Initial participant count for {event1.name}: {event1.get_participant_count()}")

    # Adding participants
    event1.add_participant()
    event1.add_participant()
    event1.add_participant()

    # Display updated participant count
    print(f"Updated participant count for {event1.name}: {event1.get_participant_count()}")
