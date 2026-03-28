from tkinter import StringVar
import customtkinter

app = customtkinter.CTk()
app.geometry("400x500")

apptemp = StringVar(value="")


def convert_temp(temp: float, unit: str) -> tuple:
    if unit == "C":
        C = temp
        F = (C * 1.8) + 32
        K = C + 273.15
        return (F, C, K)
    if unit == "F":
        F = temp
        C = (F - 32) / 1.8
        K = C + 273.15
        return (F, C, K)
    if unit == "K":
        K = temp
        C = K - 273.15
        F = (C * 1.8) + 32
        return (F, C, K)
    return (0, 0, 0)


def calculate(choice):
    try:
        temp = float(apptemp.get())
        unit = choice

        contemp: tuple = convert_temp(temp, unit)

        Clable.configure(text="C = " + str(contemp[1]))
        Flable.configure(text="F = " + str(contemp[0]))
        Klable.configure(text="K = " + str(contemp[2]))

    except ValueError:
        Clable.configure(text="wrong input")


tempentry = customtkinter.CTkEntry(
    app, placeholder_text="temperature", textvariable=apptemp
)
tempentry.pack(padx=20, pady=20)

unitoption = customtkinter.CTkOptionMenu(
    app, values=["select", "C", "F", "K"], command=calculate
)
unitoption.pack(padx=20, pady=20)

Clable = customtkinter.CTkLabel(app, text="C = 0")
Flable = customtkinter.CTkLabel(app, text="F = 0")
Klable = customtkinter.CTkLabel(app, text="K = 0")

Clable.pack(padx=20, pady=20)
Flable.pack(padx=20, pady=20)
Klable.pack(padx=20, pady=20)

app.mainloop()
