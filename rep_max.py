
class RepMax():
    BENCH_PRESS = {
        1: 1, 2: 1.035, 3: 1.08, 4: 1.115, 5: 1.15,
        6: 1.18, 7: 1.22, 8: 1.255, 9: 1.29, 10: 1.325,
    }
    DEADLIFT = {
        1: 1, 2: 1.065, 3: 1.13, 4: 1.147, 5: 1.164,
        6: 1.181, 7: 1.198, 8: 1.232, 9: 1.232, 10: 1.24,
    }
    POWER_SQUATS = {
        1: 1, 2: 1.0475, 3: 1.13, 4: 1.1575, 5: 1.2,
        6: 1.242, 7: 1.284, 8: 1.326, 9: 1.368, 10: 1.41,
    }
    exercises = {
        'жим': BENCH_PRESS,
        'становая': DEADLIFT,
        'присед': POWER_SQUATS,
    }

    def __init__(self, exercise: str, rep: int, weight: int,):
        self.exercise = exercise
        self.rep = rep
        self.weight = weight

    def get_rep_max(self) -> str:
        coef = self.exercises[self.exercise][self.rep]
        rm = coef * self.weight
        return f'{self.exercise}, одноповторный максимум: {rm:.2f}'
