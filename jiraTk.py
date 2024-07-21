import tkinter as tk
from tkinter import ttk


def add_position():
    position = entry1.get()
    department = entry2.get()
    people = entry3.get()
    salary = entry4.get()
    work = entry5.get()
    hours = entry6.get()
    overview_list = [position, department, people, salary, work, hours]
    for i in overview_list:
        overview_text.insert(tk.END, i + "\n")
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    entry4.delete(0, tk.END)
    entry5.delete(0, tk.END)
    entry6.delete(0, tk.END)


root = tk.Tk()
root.configure(background="LavenderBlush3")
root.title("Самописная Jira")

text0 = tk.Label(root, text="Заявка на поиск сотрудника", bg="LavenderBlush3", fg="black", font=("Arial", 18))
text0.grid(row=0, column=1, pady=20)

text1 = tk.Label(root, text="Название позиции", bg="LavenderBlush3", fg="black", font=("Arial", 13))
text1.grid(row=1, column=0, pady=10, padx=20)

entry1 = tk.Entry(root, width=42, bg="LavenderBlush4", fg="black")
entry1.grid(row=1, column=1)

text2 = tk.Label(root, text="Подразделение", bg="LavenderBlush3", fg="black", font=("Arial", 13))
text2.grid(row=2, column=0, pady=10)

options1 = ["Департамент консалтинга", "ИТ департамент", "Юридический департамент", "Административный департамент",
            "Департамент маркетинга", "Департамент продаж"]
entry2 = ttk.Combobox(root, values=options1, width=40)
entry2.grid(row=2, column=1)

text3 = tk.Label(root, text="Количество человек", bg="LavenderBlush3", fg="black", font=("Arial", 13))
text3.grid(row=3, column=0, pady=10)

entry3 = tk.Entry(root, width=42, bg="LavenderBlush4", fg="black")
entry3.grid(row=3, column=1)

text4 = tk.Label(root, text="Оклад", bg="LavenderBlush3", fg="black", font=("Arial", 13))
text4.grid(row=5, column=0, pady=10)

entry4 = tk.Entry(root, width=42, bg="LavenderBlush4", fg="black")
entry4.grid(row=5, column=1)

text5 = tk.Label(root, text="Оформление", bg="LavenderBlush3", fg="black", font=("Arial", 13))
text5.grid(row=6, column=0, pady=10)

options2 = ["Трудовой договор", "Самозанятый", "ИП", "ГПХ", "Другое"]
entry5 = ttk.Combobox(root, values=options2, width=40)
entry5.grid(row=6, column=1)

text6 = tk.Label(root, text="График работы", bg="LavenderBlush3", fg="black", font=("Arial", 13))
text6.grid(row=7, column=0, pady=10)

options3 = ["40 часов, офис", "40 часов, гибрид", "40 часов, удаленка", "35 часов, офис", "35 часов, гибрид",
            "35 часов, удаленка", "Проектная занятость"]
entry6 = ttk.Combobox(root, values=options3, width=40)
entry6.grid(row=7, column=1)

enter_button = tk.Button(root, text="Отправить заявку", height=1, font=("Arial", 14), command=add_position)
enter_button.grid(row=8, column=1, pady=15)

text7 = tk.Label(root, text="Агрегированная информация", bg="LavenderBlush3", fg="black", font=("Arial", 18))
text7.grid(row=0, column=3)
overview_text = tk.Text(root, height=8, width=55, bg="LavenderBlush4", fg="black", font=("Arial", 12))
overview_text.grid(row=1, column=3, rowspan=3, padx=30)

root.mainloop()
