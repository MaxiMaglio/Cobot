class ArmPositions():
    def __init__(self, initial_position, pullback_position):
        self._initial_position = initial_position
        self._pullback_position = pullback_position

    def initial_position(self):
        return self._initial_position

    def pullback_position(self):
        return self._pullback_position
