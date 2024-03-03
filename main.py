import tkinter as tk

def dodaj_liczbe(liczba):
    wprowadzenie.set(wprowadzenie.get() + str(liczba))

def oblicz_wynik():
    try:
        wprowadzenie.set(eval(wprowadzenie.get()))
    except Exception as e:
        wprowadzenie.set("Błąd")

def wyczysc_wprowadzenie():
    wprowadzenie.set("")

root = tk.Tk()
root.title("Kalkulator")

wprowadzenie = tk.StringVar()
wprowadzenie.set("")

frame = tk.Frame(root, padx=10, pady=10)
frame.grid(row=0, column=0, columnspan=4)

entry = tk.Entry(frame, textvariable=wprowadzenie, font=('Arial', 20), bd=10, insertwidth=4, width=14, justify='right')
entry.grid(row=0, column=0, columnspan=4)

button7 = tk.Button(frame, text='7', padx=20, pady=20, font=('Arial', 20), command=lambda: dodaj_liczbe(7))
button8 = tk.Button(frame, text='8', padx=20, pady=20, font=('Arial', 20), command=lambda: dodaj_liczbe(8))
button9 = tk.Button(frame, text='9', padx=20, pady=20, font=('Arial', 20), command=lambda: dodaj_liczbe(9))
button_plus = tk.Button(frame, text='+', padx=20, pady=20, font=('Arial', 20), command=lambda: dodaj_liczbe('+'))

button4 = tk.Button(frame, text='4', padx=20, pady=20, font=('Arial', 20), command=lambda: dodaj_liczbe(4))
button5 = tk.Button(frame, text='5', padx=20, pady=20, font=('Arial', 20), command=lambda: dodaj_liczbe(5))
button6 = tk.Button(frame, text='6', padx=20, pady=20, font=('Arial', 20), command=lambda: dodaj_liczbe(6))
button_minus = tk.Button(frame, text='-', padx=20, pady=20, font=('Arial', 20), command=lambda: dodaj_liczbe('-'))

button1 = tk.Button(frame, text='1', padx=20, pady=20, font=('Arial', 20), command=lambda: dodaj_liczbe(1))
button2 = tk.Button(frame, text='2', padx=20, pady=20, font=('Arial', 20), command=lambda: dodaj_liczbe(2))
button3 = tk.Button(frame, text='3', padx=20, pady=20, font=('Arial', 20), command=lambda: dodaj_liczbe(3))
button_mnozenie = tk.Button(frame, text='*', padx=20, pady=20, font=('Arial', 20), command=lambda: dodaj_liczbe('*'))

button0 = tk.Button(frame, text='0', padx=20, pady=20, font=('Arial', 20), command=lambda: dodaj_liczbe(0))
button_clear = tk.Button(frame, text='C', padx=20, pady=20, font=('Arial', 20), command=wyczysc_wprowadzenie)
button_dzielenie = tk.Button(frame, text='/', padx=20, pady=20, font=('Arial', 20), command=lambda: dodaj_liczbe('/'))
button_wynik = tk.Button(frame, text='=', padx=20, pady=20, font=('Arial', 20), command=oblicz_wynik)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button_plus.grid(row=1, column=3)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button_minus.grid(row=2, column=3)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button_mnozenie.grid(row=3, column=3)

button0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_dzielenie.grid(row=4, column=2)
button_wynik.grid(row=4, column=3)

root.mainloop()