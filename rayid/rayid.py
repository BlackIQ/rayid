import random

values = {
    "digit": "0123456789",
    "lower": "abcdefghijklmnopqrstuvwxyz",
    "upper": "abcdefghijklmnopqrstuvwxyz".upper(),
}


class RayID:
    def __init__(self, type) -> None:
        self.type = type

    def engine(self, length):
        result = ""

        characters = self.characters()

        for i in range(0, length):
            result += random.choice(characters)

        return result

    def characters(self):
        valuesResult = ""

        if (self.type == "all"):
            for v in values:
                valuesResult += values[v]
        else:
            valuesResult = values[self.type]

        return valuesResult

    def gen(self, length):
        generated = self.engine(length)

        if (generated[0] == "0"):
            return self.engine(length)
        else:
            return generated
