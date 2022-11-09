import re
import tkinter


def is_valid_rep(newval):
    return re.match('^(\d{0,1}|10)$', newval) is not None


def is_validl_weight(newval):
    return re.match('^\d{0,3}$', newval) is not None


def test_rm(exercise):
    rep = int(e_rep.get())
    weight = int(e_weight.get())
    value = RepMax(exercise, rep, weight)
    result['text'] = str(value.get_rep_max())


root = tkinter.Tk()
root.title('Калькулятор RM')
root.geometry('400x300+600+300')
root.resizable(width=False, height=False)

check = (root.register(is_validl_weight), "%P")
check2 = (root.register(is_valid_rep), "%P")

l_rep = tkinter.Label(
    text='количество повторений от 1 до 10',
    font='Arial 12'
)
e_rep = tkinter.Entry(
    font='Arial 12', validate='key', validatecommand=check2,
)
l_weight = tkinter.Label(text='вес штанги кг', font='Arial 12')
e_weight = tkinter.Entry(
    font='Arial 12', validate='key', validatecommand=check,
)
label_choose = tkinter.Label(text='выберите движение', font='Arial 12')
result = tkinter.Label(text='result', font='Arial 12', height=4,)
button_bench = tkinter.Button(
    text='Жим',
    font='Arial 12',
    command=lambda exercise='жим': test_rm(exercise),
)
button_bench.config(bd=5, bg='#cccccc', width=15)
button_deadlift = tkinter.Button(
    text='Тяга',
    font='Arial 12',
    command=lambda exercise='становая': test_rm(exercise)
)
button_deadlift.config(bd=5, bg='#cccccc', width=15, )
button_squats = tkinter.Button(
    text='присед',
    font='Arial 12',
    command=lambda exercise='присед': test_rm(exercise)
)
button_squats.config(bd=5, bg='#cccccc', width=15, )


l_rep.pack()
e_rep.pack()
l_weight.pack()
e_weight.pack()
label_choose.pack()
button_bench.pack()
button_deadlift.pack()
button_squats.pack()
result.pack(side=tkinter.BOTTOM)


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


root.mainloop()

#if __name__ == "__main__":
#    app = RepMaxApp()
#    app.mainloop()
