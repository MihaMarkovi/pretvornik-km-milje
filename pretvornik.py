import Tkinter
import tkMessageBox

window = Tkinter.Tk()

greeting = Tkinter.Label(window, text="Dobrodosli v pretvorniku kilomerov v milje")
greeting.pack()

greeting_2 = Tkinter.Label(window, text="Vpisite koliko kilometrov")
greeting_2.pack()

guess = Tkinter.Entry(window)
guess.pack()

def show_answer():
    result ="To je " + str(int(guess.get()) * 0.62137) + " milj"


    tkMessageBox.showinfo(message = result)

# submit button
submit = Tkinter.Button(window, text="Submit", command=show_answer)  # check_guess, not check_guess()
submit.pack()

window.mainloop()