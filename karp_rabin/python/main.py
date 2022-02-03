import math


class RollingHash:

    def __init__(self):
        self.value = 0
        self.base = 255
        self.divider = self.get_prime()

    def append(self, letter: str):
        if letter_value not in range(self.base + 1):
            raise ValueError(f"Character value {letter}={int(letter)} not in range(0, {self.base + 1}).")
        letter_value = int(letter) * self.base
        self.value *= self.base
        self.value += letter_value

    def hash(self):
        return self.value % self.divider

    def get_prime(self):
        number = 1_000_001
        while True:
            if self.check_prime(number):
                return number
            number += 1

    @staticmethod
    def check_prime(value: int) -> bool:
        stop = math.ceil(math.sqrt(value))
        for idx in range(2, stop):
            if value % idx == 0:
                return False
        return True


r = RollingHash()
r.get_prime()
print(r.divider)
