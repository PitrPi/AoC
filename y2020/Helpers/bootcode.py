from typing import Optional


class Bootcode():
    def __init__(self, instructions=None):
        self.INSTRUCTIONS = instructions
        self.num_of_instructions = len(self.INSTRUCTIONS)
        self.accumulator = 0
        self.opidx = 0
        self.visited = []
        self.status = "Running"

    def log_myself(self):
        self.visited.append(self.opidx)

    def nop(self, value: Optional[int]):
        self.log_myself()
        self.opidx += 1

    def jmp(self, value: int):
        self.log_myself()
        self.opidx += value

    def acc(self, value: int):
        self.log_myself()
        self.accumulator += value
        self.opidx += 1

    def check_loop(self):
        if self.opidx in self.visited:
            return True
        return False

    def execute_instruction(self, break_loop=True):
        if break_loop and self.check_loop():
            self.status = "Infinite loop"
            return False
        elif self.opidx == self.num_of_instructions:
            self.status = "Out of instructions"
            return False
        elif self.opidx > self.num_of_instructions:
            self.status = "Jumped out of instructions"
            return False
        instruction = self.INSTRUCTIONS[self.opidx]
        ins = instruction[0]
        val = int(instruction[1])
        getattr(self, ins)(val)
        return True

    def execute_instructions(self, break_loop=True):
        while self.execute_instruction(break_loop):
            pass
        return None


if __name__ == '__main__':
    def _test_bootcode_creation():
        bc = Bootcode()
        assert bc.opidx == 0
        assert bc.visited == []
        assert bc.accumulator == 0

    def _test_bootcode_step():
        bc = Bootcode()
        bc.nop()
        assert bc.opidx == 1
        assert bc.visited == [0]
        assert bc.accumulator == 0

    def _test_bootcode_accumulator():
        bc = Bootcode()
        bc.acc(1)
        assert bc.accumulator == 1
        bc.acc(10)
        assert bc.accumulator == 11
        bc.acc(-45)
        assert bc.accumulator == 11-45

    def _test_bootcode_jump():
        bc = Bootcode()
        bc.jmp(3)
        assert bc.opidx == 3
        assert bc.visited == [0]
        bc.jmp(-5)
        assert bc.opidx == -2
        assert bc.visited == [0, 3]
