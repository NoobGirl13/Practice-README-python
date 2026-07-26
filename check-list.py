import tkinter as tk

def add():
    text = entry.get().strip()
    if text:
        listbox.insert(tk.END, "[ ] "+text)
        entry.delete(0, tk.END)

def delete():
    listbox.delete(tk.ACTIVE)

def tick():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        text = listbox.get(index)
        if text.startswith("[ ] "):
            new_text = text.replace("[ ] ", "[x] ", 1)
        elif text.startswith("[x] "):
            new_text = text.replace("[x] ", "[ ] ", 1)
        else:
            new_text = "[x] "+text

    listbox.delete(index)
    listbox.insert(index, new_text)

root = tk.Tk()
root.geometry("1000x1000")
root.configure(bg="#222021")

listbox = tk.Listbox(bg="#6A5646", font=("Arial", 18), selectbackground="#808588", selectforeground="white")
listbox.pack(pady=50)
listbox.bind("<Double-Button-1>", lambda event: tick())

entry = tk.Entry(bg="#7A7A7A", fg="#111111", font=("Arial", 14))
entry.pack(pady=10)

add_button = tk.Button(text="add", bg="#707070", font="Arial", command=add)
add_button.pack(pady=10)

del_button = tk.Button(text="delete", bg="#707070", font="Arial", command=delete)
del_button.pack(padx=50)



root.mainloop()