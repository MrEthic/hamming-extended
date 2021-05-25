from functools import reduce


class MessageChunk:
    def __init__(self, message: list):
        """
        Constructor for MessageChunk
        Args:
            message list: List of bite representing the chunk
        """
        if len(message) == 11:
            self.__message = message
            self.__bits: list = [0, 0, 0] + [message[0], ] + [0, ] + message[1:4] + [0, ] + message[4:]
            self.__stable: list = self.__get_stable()

        if len(message) == 16:
            self.__stable = message
            self.__error = reduce(lambda x, y: x ^ y, self.__get_ones_index(enumerate(self.__stable)))

    @property
    def message(self) -> list:
        return self.__message

    @property
    def bits(self) -> list:
        return self.__bits

    @property
    def stable(self) -> list:
        return self.__stable

    @property
    def error(self) -> int:
        return self.__error

    def __repr__(self) -> str:
        return (
            f"SenderMessage(\n\tinitial:\t{self.message}\n\tstable:  \t{self.stable})"
        )

    def __len__(self) -> int:
        return len(self.bits)

    @staticmethod
    def __get_ones_index(msg: enumerate) -> list:
        """
        Get index of sets bite
        Args:
            msg enumerate: enum of (bite, index)

        Returns:
            List of index of sets bite
        """
        return [i for i, bit in msg if bit]

    def __get_stable(self) -> list:
        """
        Get stable version of the chunk
        Returns:
            Stable chunk
        """
        stable = self.bits.copy()
        enum: enumerate = enumerate(self.bits)
        ons: list = self.__get_ones_index(enum)
        xor_ons: int = reduce(lambda x, y: x ^ y, ons)
        parity_values = ("000" + bin(xor_ons)[2:])[-4:]
        stable[8] = int(parity_values[0])
        stable[4] = int(parity_values[1])
        stable[2] = int(parity_values[2])
        stable[1] = int(parity_values[3])
        xor: int = reduce(lambda x, y: x ^ y, stable)
        stable[0] = xor
        return stable
