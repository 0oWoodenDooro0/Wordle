import tkinter as tk

from words import Wordle

window = tk.Tk()
window.title("Wordle")
window.geometry("800x600")

frame1 = tk.Frame(window)
frame2 = tk.Frame(window)
frame3 = tk.Frame(window)

ans = Wordle().question()
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
    ans = Wordle().question()
    times = 0
    input_word.delete(0, "end")
    for i in range(6):
        for j in range(5):
            tk.Label(frame2, text=" ", relief="flat", bg="gray", font=("Arial", 20), bd=10, fg="white", width=2,
                     height=1).grid(row=i, column=j, padx=5, pady=5)
    window.update_idletasks()


reset_bttn = tk.Button(frame3, text="Restart", font=("Arial", 15), command=reset)


def check_answer(event):
    global times
    if times == 6: return
    guess = var_input_word.get()
    input_word.delete(0, "end")
    window.update_idletasks()
    if len(guess) != len(ans):
        print("請重新輸入,字數要對")
    elif Wordle().check(guess):
        times += 1
        l = ["", "", "", "", ""]
        for i in range(len(ans)):
            for j in range(len(ans)):
                if l[i] == "":
                    tk.Label(frame2, text=guess[i], relief="flat", bg="gray", font=("Arial", 20), bd=10,
                             fg="white", width=2, height=1).grid(row=times - 1, column=i, padx=5, pady=5)
                if guess[i] == ans[j]:
                    if i == j:
                        tk.Label(frame2, text=guess[i], relief="flat", bg="green", font=("Arial", 20), bd=10,
                                 fg="white", width=2, height=1).grid(row=times - 1, column=i, padx=5, pady=5)
                        l[i] = "g"
                    elif l[i] != "g":
                        tk.Label(frame2, text=guess[i], relief="flat", bg="orange", font=("Arial", 20), bd=10,
                                 fg="white", width=2, height=1).grid(row=times - 1, column=i, padx=5, pady=5)
                        l[i] = "o"
        if l == ["g", "g", "g", "g", "g"]: times = 6
    else:
        print("沒有這個單字")
    if times == 6:
        print("答案是", ans)


header_label.pack()
input_word.pack()
reset_bttn.pack()
frame1.pack()
frame2.pack()
frame3.pack()

window.bind("<Return>", check_answer)

window.mainloop()

# ans = Wordle().question()
# location = []
# right = "______"
# while True:
#     guess = str(input("輸入要猜的英文單字:"))
#     if guess == ans:
#         break
#     if guess == "ans":
#         print(ans)
#     elif len(guess) != len(ans):
#         print("請重新輸入,字數要對")
#     if Wordle().check(guess):
#         for i in range(len(ans)):
#             for j in range(len(ans)):
#                 if guess[i] == ans[j]:
#                     if guess[i] not in location:
#                         location.append(guess[i])
#                     if i == j:
#                         right = right[:i] + guess[i] + right[i + 1:]
#         print(right[:len(ans)])
#         print("對的字：", location)
#     else:
#         print("沒有這個單字")
# print("恭喜你猜對啦")
