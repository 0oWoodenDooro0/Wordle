import tkinter as tk
import wordle

window = tk.Tk()
window.title("Wordle")
window.geometry("350x500")

frame1 = tk.Frame(window)
frame2 = tk.Frame(window)
frame3 = tk.Frame(window)

ans = wordle.question()
times = 0

header_label = tk.Label(frame1, text="Wordle", font=("Arial", 25))

for i in range(6):
    for j in range(5):
        tk.Label(frame2, text=" ", relief="flat", bg="gray", font=("Arial", 20), bd=10, fg="white", width=2,
                 height=1).grid(row=i, column=j, padx=5, pady=5)

var_input_word = tk.StringVar()
input_word = tk.Entry(frame3, textvariable=var_input_word, show=None, font=("Arial", 15))

input_word.focus()


def reset():
    global times
    global ans
    ans = wordle.question()
    times = 0
    input_word.delete(0, "end")
    for i in range(6):
        for j in range(5):
            tk.Label(frame2, text=" ", relief="flat", bg="gray", font=("Arial", 20), bd=10, fg="white", width=2,
                     height=1).grid(row=i, column=j, padx=5, pady=5)
    window.update_idletasks()


reset_btn = tk.Button(frame3, text="Restart", font=("Arial", 15), command=reset)


def check_answer(event):
    global times
    if times == 6: return
    guess = var_input_word.get()
    input_word.delete(0, "end")
    window.update_idletasks()
    if len(guess) != len(ans):
        print("請重新輸入,字數要對")
    elif wordle.check(guess):
        times += 1
        check_list = ["", "", "", "", ""]
        guess_set = set()
        for i in range(5):
            guess_set.add(guess[i])
        for i in range(5):
            for j in range(5):
                if guess[i] == ans[j] and ans[j] in guess_set:
                    if i == j:
                        check_list[i] = "g"
                        guess_set.remove(ans[j])
                    elif check_list[i] != "g":
                        check_list[i] = "o"
                        guess_set.remove(ans[j])
        for i in range(5):
            if check_list[i] == "g":
                tk.Label(frame2, text=guess[i], relief="flat", bg="green", font=("Arial", 20), bd=10, fg="white",
                         width=2, height=1).grid(row=times - 1, column=i, padx=5, pady=5)
            elif check_list[i] == "o":
                tk.Label(frame2, text=guess[i], relief="flat", bg="orange", font=("Arial", 20), bd=10,
                         fg="white", width=2, height=1).grid(row=times - 1, column=i, padx=5, pady=5)
            else:
                tk.Label(frame2, text=guess[i], relief="flat", bg="gray", font=("Arial", 20), bd=10, fg="white",
                         width=2, height=1).grid(row=times - 1, column=i, padx=5, pady=5)
        if check_list == ["g", "g", "g", "g", "g"]:
            times = 6
    else:
        print("沒有這個單字")
    if times == 6:
        print("答案是", ans)


header_label.pack()
input_word.pack()
reset_btn.pack()
frame1.pack()
frame2.pack()
frame3.pack()

window.bind("<Return>", check_answer)

window.mainloop()

# def check_answer(event):
#     global times
#     if times == 6: return
#     guess = var_input_word.get()
#     input_word.delete(0, "end")
#     window.update_idletasks()
#     if len(guess) != len(ans):
#         print("請重新輸入,字數要對")
#     elif wordle.check(guess):
#         times += 1
#         l = ["", "", "", "", ""]
#         for i in range(len(ans)):
#             for j in range(len(ans)):
#                 if l[i] == "":
#                     tk.Label(frame2, text=guess[i], relief="flat", bg="gray", font=("Arial", 20), bd=10,
#                              fg="white", width=2, height=1).grid(row=times - 1, column=i, padx=5, pady=5)
#                 if guess[i] == ans[j]:
#                     if i == j:
#                         tk.Label(frame2, text=guess[i], relief="flat", bg="green", font=("Arial", 20), bd=10,
#                                  fg="white", width=2, height=1).grid(row=times - 1, column=i, padx=5, pady=5)
#                         l[i] = "g"
#                     elif l[i] != "g":
#                         tk.Label(frame2, text=guess[i], relief="flat", bg="orange", font=("Arial", 20), bd=10,
#                                  fg="white", width=2, height=1).grid(row=times - 1, column=i, padx=5, pady=5)
#                         l[i] = "o"
#         if l == ["g", "g", "g", "g", "g"]: times = 6
#     else:
#         print("沒有這個單字")
#     if times == 6:
#         print("答案是", ans)
