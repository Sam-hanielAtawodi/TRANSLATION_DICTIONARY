from tkinter import Tk, Entry, Button, Label, StringVar
window = Tk()
window.geometry("500x500")
window.title("The General Dictionary")


def pack_first_page():
    button_frame.pack()
    yoruba_button.pack()
    igbo_button.pack()
    french_button.pack()
    nupe_button.pack()

def handle_navigate_forward(target):
    global current_language
    current_language = target
    print(f"{target} button clicked!")
    print(f"Current language: {current_language}")
    button_frame.pack_forget()
    sub_heading.pack_forget()
    translation_frame.pack()
    word_entry.pack()
    translation_label.pack()
    translate_button.pack()
    back_button.pack()

    def handle_navigate_back():
        translation.set("")
        word_entry.delete(0, tk.END)
        translation_frame.pack_forget()
        pack_first_page()

    def translate_word(word, language):
        print(f"Translating {word} from {language}")


        word = word.lower()

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

yoruba_dictionary = {
    'owo': "hand",
    'oju': "eye",
    'ati': "ear",
    'ori': "head",
    'ajika': "shoulder",
    'wa': "come",
    'gba': "take",
    'ese': "leg",
    'enu': "mouth",
    'sara': "run",
    'jada': "out",
    'odabor': "goodbye",
    'maji': "two",
    'metar': "three",
    'shibi': "spoon",
    'abour': "plate",
    'omi': "water",
    'oko': "dick",
    'ojen': "food",
    'aja': "dog",
}

nupe_dictionary = {
    'dzuko': "market",
    'be': "come",
    'emi': "home",
    'ede': "cloth",
    'ebi': "knife",
    'esa': "chair",
    'bichi': "leg",
    'soku': "broom",
    'layam': "give me",
    'ewugi': "spoon",
    'kubelazi': "good_morning",
    'kubegidi': "good_afternoon",
    'yeshi': "night",
    'azo': "beans",
    'asibiti': "hospital",
    'pati': "mountain",
    'misu': "mouth",
    'egwalo': "right_hand",
    'eyi': "guinea_corn",
    'kubelozu': "good_evening"

}

French_dictionary = {
    'bonjour': "Good Morning",
    'merci': "Thank you",
    'qui': "Yes",
    'non': "No",
    'excuse-moi': "Excuse me",
    'pardon': "Sorry",
    'comment': "How",
    'pourquol': "Why",
    'quand': "When",
    'qui': "Who",
    'je': "I",
    'tu': "You",
    'il': "He",
    'elle': "She",
    'nous': "We",
    'et': "And",
    'bon': "Good",
    'chaud': "Hot",
    'froid': "Cold",
    'bonsoir': "Good evening"

}

def search(word):
    if word in igbo_dictionary:
        result.set(igbo_dictionary[word])
        print(igbo_dictionary[word])

    else:
        result.set("Not found")

    elif language == "yoruba":
        if word in yoruba_dictionary:
            print(yoruba_dictionary[word])
            translation.set(yoruba_dictionary[word])
        else:
            print("Not found")
            translation.set("Word not found")

    elif language == "nupe":
        if word in nupe_dictionary:
            print(nupe_dictionary[word])
            translation.set(nupe_dictionary[word])
        else:
            print("Not found")
            translation.set("Word not found")

    elif language == "french":
        if word in french_dictionary:
            print(french_dictionary[word])
            translation.set(french_dictionary[word])
        else:
            print("Not found")
            translation.set("Word not found")

heading = tk.Label(root, text="Welcome to the Multi-language dictionary", font=("Times new roman", 30), pady=30)
sub_heading = tk.Label(root, text="Select a language to translate", font=("Times new roman", 25), pady=15)

button_frame = tk.Frame(root)
yoruba_button = tk.Button(button_frame, text="Yoruba", width=40, pady=10, command=lambda:handle_navigate_forward("yoruba"))
igbo_button = tk.Button(button_frame,text="Igbo", width=40, pady=10, command=lambda:handle_navigate_forward("igbo"))
french_button = tk.Button(button_frame, text="French", width=40, pady=10, command=lambda:handle_navigate_forward("French"))
nupe_button = tk.Button(button_frame, text="Nupe", width=40, pady=10, command=lambda:handle_navigate_forward("Nupe"))


translation = tk.StringVar()
translation_frame = tk.Frame(root)
word_entry = tk.Entry(translation_frame, width=40, font=("Arial", 20))
translate_button = tk.Button(translation_frame, text="Translate", width=40, pady=10, command=lambda:translate_word(word_entry.get(), current_language))
translation_label = tk.Label(translation_frame, textvariable=translation, font=("Arial", 20), pady=15)
back_button = tk.Button(translation_frame, text="Back", width=40, pady=10, command=handle_navigate_back)

heading.pack()
pack_first_page()

window.mainloop() 
