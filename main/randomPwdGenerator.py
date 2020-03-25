
import random
import charSet as cs


class Random_Password_Generator:

    def mix_chars_and_case(self, cluster):

        indexToChange = random.sample(range(0, len(cluster)+1), 1)
        clusterAsList = list(cluster)

        for indexNumber in indexToChange:
            x = indexNumber
            newletter = random.choice(cs.specialChars)
            clusterAsList.insert(x, newletter)

        return (''.join(clusterAsList))

    def generate_random_password(self, length, strength):
        self.chosenSet = cs.mediumSet

        if strength == 1:
            self.chosenSet = cs.weakSet
            self.password = ''.join(random.choice(self.chosenSet) for _ in range(length))
            return self.password

        elif strength == 2:
            self.chosenSet = cs.mediumSet
            self.password = ''.join(random.choice(self.chosenSet) for _ in range(length))
            return self.password

        elif strength == 3:
            self.chosenSet = cs.mediumSet
            self.password = self.mix_chars_and_case(''.join(random.choice(self.chosenSet) for _ in range(length-1)))
            return self.password

        elif strength == 4:
            self.chosenSet = cs.strongSet
            self.password = ''.join(random.choice(self.chosenSet) for _ in range(length))
            return self.password


        self.password = ''.join(random.choice(self.chosenSet) for _ in range(length))
        return self.password


