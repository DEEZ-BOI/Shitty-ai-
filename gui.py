import wooframalpha as wra
import creativetext as ct
import srtingmech as sm
import pediawiki as wki 
import tkinter as tk
import newwindow as nw 

root = tk.Tk() 

root.geometry('400x80') ## Window Size
root.configure(bg ='#1F1F1F') ## Background Colour
root.title('AI Assisstant') ## Title

##Instruction
basic_instruction = tk.Label(root, text='Enter a Prompt', bg='#1F1F1F', fg='#FFFFFF')
basic_instruction.pack()

##Input
def get_response(): ## Command for Submit button
    text = entry.get()     
    final_answer = sm.classify_query(text)
    if final_answer == 'wolfram_alpha':
        final_answer = wra.wolframalpha(text)
    elif final_answer == 'wikipedia':
        final_answer = wki.fn(text)
    elif final_answer == 'creative':
        final_answer = ct.creative_answer(text)
    nw.child_window(root, final_answer)

entry = tk.Entry(root, bg='#1F1F1F', fg='#FFFFFF', width=40)
entry.pack()

##Submit button
button = tk.Button(root, text = 'Submit!',width=20, command=get_response, bg='#641132', fg='#FFFFFF')
button.pack()

root.mainloop()