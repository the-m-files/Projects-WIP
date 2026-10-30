import tkinter as tk

root = tk.Tk()

rat_card = tk.Frame(root, borderwidth=2, relief="solid")
rat_card.pack(padx=20, pady=20)

label = tk.Label(rat_card, text="RAT SIM")
label.pack()

name = tk.Label(rat_card, text="Mongo")
health = tk.Label(rat_card, text="Health: 10")

name.pack()
health.pack()


def test_action():
    health.config(text="Health: 50")
    action.config(relief="raised")


action = tk.Button(
    rat_card,
    text="PRESS ME",
    border=1,
    borderwidth=1,
    relief="sunken",
    command=test_action
)

action.pack()

root.mainloop()