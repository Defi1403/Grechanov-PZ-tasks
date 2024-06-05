import tkinter as tk
import random

list = []
for i in range(10):
    list.append(random.randint(0, 20))


def add_odd(list):
    odd_numbers = []
    for i in range(10):
        if list[i] % 2 != 0:
            odd_numbers.append(list[i])
    return odd_numbers


def show_result():
    result_list = add_odd(list)
    result_text.delete("1.0", "end")
    result_text.insert("1.0", ''.join(str(len(result_list))))
    result_text.insert("1.0", ''.join('Количество нечетных чисел: '))
    result_text.insert("1.0", ''.join('\n'))
    result_text.insert("1.0", ''.join(str(result_list)))
    result_text.insert("1.0", ''.join('Нечетные числа: '))
    result_text.insert("1.0", ''.join('\n'))
    result_text.insert("1.0", ''.join(str(list)))
    result_text.insert("1.0", ''.join('Изначальный список: '))
    
root = tk.Tk()
root.title("список нечетных чисел")

personal_frame = tk.LabelFrame(root, text="Вывести все содержащиеся в случайном списке нечетные числа и их количество")
personal_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

result_text = tk.Text(personal_frame, height=30, width=57)
result_text.grid(row=0, column=0)

button = tk.Button(root, text="Сгенерировать список", command=show_result)
button.grid(row=1, column=0)

root.mainloop()