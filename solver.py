from jug import Jug


class WaterJugSolver:

    def __init__(self, jug1_capacity, jug2_capacity, target):
        self.jug1 = Jug(jug1_capacity)
        self.jug2 = Jug(jug2_capacity)
        self.target = target
        self.visited = set()
        self.solution = []

    def is_solved(self):
        return self.jug1.current == self.target or self.jug2.current == self.target

    def get_state(self):
        return (self.jug1.current, self.jug2.current)

    def solve(self):

        queue = [(self.jug1.current, self.jug2.current, [])]

        while queue:
            j1, j2, path = queue.pop(0)
            self.jug1.current, self.jug2.current = j1, j2

            if self.is_solved():
                self.solution = path + [(j1, j2)]
                return self.print_solution()

            if (j1, j2) in self.visited:
                continue
            self.visited.add((j1, j2))

            next_states = [
                (self.jug1.capacity, j2, "Fill Jug 1"),
                (j1, self.jug2.capacity, "Fill Jug 2"),
                (0, j2, "Empty Jug 1"),
                (j1, 0, "Empty Jug 2"),
                (max(0, j1 - (self.jug2.capacity - j2)), min(self.jug2.capacity, j2 + j1), "Pour Jug 1 → Jug 2"),
                (min(self.jug1.capacity, j1 + j2), max(0, j2 - (self.jug1.capacity - j1)), "Pour Jug 2 → Jug 1"),
            ]

            for new_j1, new_j2, action in next_states:
                if (new_j1, new_j2) not in self.visited:
                    queue.append((new_j1, new_j2, path + [(j1, j2, action)]))

        print("No solution found.")

    def print_solution(self):
        print("\n **Solution Found:**\n")
        print(" | Jug 1 | Jug 2 | Action")
        print("-" * 30)
        for step in self.solution:
            if len(step) == 3:
                j1, j2, action = step
            else:
                j1, j2 = step
                action = "Goal Reached!"
            print(f" |  {j1}L  |  {j2}L  | {action}")
        print("-" * 30)
