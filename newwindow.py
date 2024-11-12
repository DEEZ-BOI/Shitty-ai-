def child_window(window, final_answer):    
    import tkinter as tk
    import texttospeech as tts
    
    # Create the window
    child = tk.Toplevel(window)
    child.geometry('400x500')
    child.configure(bg='#1F1F1F')
    child.title('Response')
    
    # Create the frame
    frame = tk.Frame(child, bg='#1F1F1F')
    frame.pack(fill='both', expand=True)
    
    # Create the text widget
    text_widget = tk.Text(frame, bg='#1F1F1F', fg='#FFFFFF', wrap=tk.WORD)
    text_widget.pack(fill='both', expand=True)
    
    # Create the scrollbar
    scrollbar = tk.Scrollbar(frame, command=text_widget.yview)
    scrollbar.pack(side='right', fill='y', padx=(0, 10))  # Add some padding to separate scrollbar from text
    text_widget.config(yscrollcommand=scrollbar.set)
    text_widget.pack(side='left', fill='both', expand=True)  # Pack text widget to the left
    
    # Insert the final answer into the text widget
    text_widget.insert(tk.END, final_answer)
    text_widget.config(state='disabled')
    
    # Create the speak button
    speak_button = tk.Button(child, text='Speak', command=lambda: tts.speak(final_answer), width=25, bg='blue', fg='#FFFFFF')
    speak_button.pack(padx=10, pady=10)
    
    # Configure the window to always be on top
    child.wm_attributes('-topmost', True)
    
    # Start the main loop
    child.mainloop()