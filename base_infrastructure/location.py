class Location:
    def __init__(self, city=None, state=None, pin_code=None):
        self.city = city
        self.state = state
        self.pin_code = pin_code

    def __str__(self):
        return self.city
