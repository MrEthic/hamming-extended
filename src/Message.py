from functools import reduce
from numpy import random

from src import MessageChunk


class Message:
    def __init__(self, message: list):
        self.__transmited = []
        self.__message: list = message
        self.__extended: list = self.__complete_message()
        self.__chunks: list = list()
        self.__populate_chunks()
        self.__encoded = self.__get_encoded()

    @classmethod
    def random(cls, n: int = 16):
        return cls(list(random.randint(0, 2, n)))

    @property
    def message(self) -> list:
        return self.__message

    @property
    def len(self) -> int:
        return len(self.message)

    @property
    def extended(self) -> list:
        return self.__extended

    @property
    def chunks(self) -> list:
        return self.__chunks

    @property
    def encoded(self) -> list:
        return self.__encoded

    @property
    def transmited(self) -> list:
        return self.__transmited

    def __get_encoded(self) -> list:
        enc = []
        for chunk in self.chunks:
            enc.extend(chunk)
        return enc

    def __complete_message(self, n: int = 11) -> list:
        if self.len // n == self.len / n:
            return self.message

        dif: int = n * ((self.len // n) + 1) - self.len
        return self.message + [0 for _ in range(dif)]

    def __populate_chunks(self):
        for i in range(0, len(self.extended), 11):
            chunk = MessageChunk(self.extended[i: i + 11])
            self.chunks.append(chunk.stable)

    def add_error(self, prob: float = 0.01, force_demo: bool = False):
        if force_demo:
            for chunk in self.chunks:
                index = random.randint(0, len(chunk))
                chunk[index] = int(not chunk[index])
                self.transmited.extend(chunk)
            return

        self.__transmited = self.encoded
        for i in range(len(self.transmited)):
            rand: float = random.rand()
            if rand <= prob:
                self.transmited[i] = int(not self.transmited[i])

    def print_message(self):
        for i in range(0, len(self.message), 11):
            print("            " + "".join([str(x) for x in self.message[i: i+11]]))

    def print_extended(self):
        for i in range(0, len(self.extended), 11):
            print("            " + "".join([str(x) for x in self.extended[i: i+11]]))

    def print_encoded(self):
        for i in range(0, len(self.encoded), 16):
            print("          " + "".join([str(x) for x in self.encoded[i: i+16]]))

    def print_error(self):
        for i in range(0, len(self.transmited), 16):
            c = [x for x in self.transmited[i: i+16]]
            chunk = MessageChunk(c)
            print("    " + "".join([str(x) for x in self.transmited[i: i+16]]) + "   ", end=" ")
            xor: int = reduce(lambda x, y: x ^ y, c)
            if xor == 0 and chunk.error == 0:
                print(f'Aucune erreur ({chunk.error}, {xor})')
            if xor == 0 and chunk.error != 0:
                print(f"Erreur sur 2+ bits ({chunk.error}, {xor})")
            if xor == 1:
                print(f'Erreur sur le bit {chunk.error + 1} ({chunk.error}, {xor})')

    @encoded.setter
    def encoded(self, value):
        self.__encoded = value
