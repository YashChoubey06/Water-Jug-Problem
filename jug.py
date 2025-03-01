class Jug:

    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0

    def fill(self):
        self.current = self.capacity

    def empty(self):
        self.current = 0

    def pour_into(self, other_jug):
        transfer_amount = min(self.current, other_jug.capacity - other_jug.current)
        self.current -= transfer_amount
        other_jug.current += transfer_amount
