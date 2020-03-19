class Value_Action():


# GET VALUE
    def get_value(self, value, whereFrom):
        value = whereFrom.get()
        return value

# +/- BUTTON METHODS

    def increment(self, value, place):

        value = self.get_value(value, place)
        value = int(value)
        value += 1
        value = str(value)
        place.delete(0, 'end')
        place.insert(0, value)

    def decrement(self, value, place):

        value = self.get_value(value, place)
        value = int(value)

        if value > 0:
            value -= 1
        else:
            value = 0

        value = str(value)
        place.delete(0, 'end')
        place.insert(0, value)



