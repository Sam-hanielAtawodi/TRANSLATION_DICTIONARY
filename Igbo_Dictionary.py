from tkinter import Tk, Entry, Button, Label, StringVar
window = Tk()
window.geometry("500x500")
window.title("The Igbo Dictionary")


entry_text = Entry(window)
entry_text.pack()

result = StringVar()
result_label = Label(window, textvariable=result)
result_label.pack()



igbo_dictionary = {
    'aka': "hand",
    'anya': "eye",
    'azu': "back",
    'kwusi': "stop",
    'nwa' : "child",
    'bia': "come",
    'gawa' : "go",
    'imi' : "nose",
    'nti' : "ear",
    'ukwu' : "leg",
    'isi' : "head",
    'onu' : "mouth",
    'eze' : "teeth",
    'ire' : "tongue",
    'ngwu' : "shoulder",
    'otu' : "one",
    'abuo' : "two",
    'ato' : "three",
    'ano' : "four",
    'ise' : "five",
    'asato' : "seven",

}

def search(word):
    if word in igbo_dictionary:
        result.set(igbo_dictionary[word])
        print(igbo_dictionary[word])

    else:
        result.set("Not found")

search_btn = Button(window, text="Translate", command=lambda: search(entry_text.get()))
search_btn.pack()

window.mainloop()