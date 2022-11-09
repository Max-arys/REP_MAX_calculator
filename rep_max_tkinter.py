import re
import tkinter

import rep_max


def is_valid_rep(newval):
    return re.match('^(\d{0,1}|10)$', newval) is not None


def is_validl_weight(newval):
    return re.match('^\d{0,3}$', newval) is not None


def test_rm(exercise):
    rep = int(entry_rep.get())
    weight = int(entry_weight.get())
    value = rep_max.RepMax(exercise, rep, weight)
    label_result['text'] = str(value.get_rep_max())


root = tkinter.Tk()
root.title('Калькулятор RM')
root.geometry('400x300+600+300')
root.resizable(width=False, height=False)

check = (root.register(is_validl_weight), "%P")
check2 = (root.register(is_valid_rep), "%P")

label_rep = tkinter.Label(
    text='количество повторений от 1 до 10',
    font='Arial 12'
)
label_weight = tkinter.Label(text='вес штанги кг', font='Arial 12')
label_choose = tkinter.Label(text='выберите движение', font='Arial 12')
entry_rep = tkinter.Entry(
    font='Arial 12',
    validate='key',
    validatecommand=check2,
)
entry_weight = tkinter.Entry(
    font='Arial 12',
    validate='key',
    validatecommand=check,
)
label_result = tkinter.Label(
    text='одноповторный максимум:',
    font='Arial 12',
    height=4,
)
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


label_rep.pack()
entry_rep.pack()
label_weight.pack()
entry_weight.pack()
label_choose.pack()
button_bench.pack()
button_deadlift.pack()
button_squats.pack()
label_result.pack(side=tkinter.BOTTOM)

root.mainloop()
