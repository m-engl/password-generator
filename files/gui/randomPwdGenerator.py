
import random
import charSet as cs


class Random_Password_Generator:

    def generate_random_password(self, length, strength):
        self.chosenSet = cs.mediumSet

        if strength == 1:
            self.chosenSet = cs.weakSet
        elif strength == 2:
            self.chosenSet = cs.mediumSet
        elif strength == 3:
            self.chosenSet = cs.strongSet
        elif strength == 4:
            pass

        self.password = ''.join(random.choice(self.chosenSet) for _ in range(length))
        return self.password


