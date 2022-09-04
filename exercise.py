class Exercise:
    def __init__(self, exercise_name, series, reps, load):
        self.exercise_name = exercise_name
        self.series = series
        self.reps = reps
        self.load = load
    
    @property
    def load(self):
        return self.load
    @load.setter
    def load(self, load):
        self.load = load
        