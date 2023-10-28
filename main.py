from tkinter import StringVar, filedialog
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import customtkinter 
from audio_to_text import *
from summarizer import *
import PyPDF2
from pdf_generative import *


customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue")  

def p():
    val = summarizer()

    textbox1.insert("0.0", val)
    print(val)

def recording():
    freq = 44100
    
    # Recording duration
    duration = slider.get()
    
    # Start recorder with the given values 
    # of duration and sample frequency
    recording = sd.rec(int(duration * freq), 
                    samplerate=freq, channels=2)
    
    # Record audio for the given number of seconds
    sd.wait()
    
    # This will convert the NumPy array to an audio
    # file with the given sampling frequency
    write("recording0.wav", freq, recording)
    
    # Convert the NumPy array to audio file
    wv.write("recording1.wav", recording, freq, sampwidth=2)
    p()


def open_pdf():
    import_button_text.set("loading...")
    open_file = filedialog.askopenfilename(initialdir="C:/", filetypes=[("PDF files", "*.pdf")])

    if open_file:
        s = pdftotext(open_file)
        import_button_text.set("Import")
        textbox1.insert("0.0", s)
    else:
        print('No file selected')
    
    

def prompt_run():
    if combobox.get() == "Pdf":
        sol2 = answer(textbox1.get("0.0","end") , prompt.get())
        textbox2.delete("0.0","end")
        textbox2.insert("0.0",sol2)
    elif combobox.get() == "Current Text":
        sol2 = answer(textbox2.get("0.0","end") , prompt.get())
        textbox2.delete("0.0","end")
        textbox2.insert("0.0",sol2)


def s():
    if combobox.get() == "Pdf":
        sol = summarizer(textbox1.get("0.0","end") , int(slider2.get()))
        textbox2.delete("0.0","end")
        textbox2.insert("0.0",sol)
    elif combobox.get() == "Current Text":
        sol = summarizer(textbox2.get("0.0","end") , int(slider2.get()))
        textbox2.delete("0.0","end")
        textbox2.insert("0.0",sol)



def remove_pdf():
    textbox1.delete("0.0","end")
    textbox2.delete("0.0","end")

app = customtkinter.CTk() 
app.geometry("1000x800")
app.minsize(1000,800)
app.maxsize(1000,800)


slider = customtkinter.CTkSlider(master=app, from_=0, to=40 , width=145)
slider.place(relx=0.05, rely=0.1)

button = customtkinter.CTkButton(master=app, text="Start Recording", command=recording  ,fg_color="maroon",height=40)
button.place(relx=0.05, rely=0.2)

import_button_text = StringVar()
import_pdf_button = customtkinter.CTkButton(master=app,textvariable=import_button_text , command = open_pdf ,height=40 , width=160)
import_pdf_button.place(relx=0.05, rely=0.8)
import_button_text.set("Import")

textbox1 = customtkinter.CTkTextbox(app ,  width = 600 , height = 620)
textbox1.place(relx=0.36, rely=0.08)
textbox2 = customtkinter.CTkTextbox(app , width = 600 , height = 620)
textbox2.place(relx=0.36, rely=0.08)    

prompt = customtkinter.CTkEntry(master=app, placeholder_text="Ask me your question" , height=40 , width = 425 ,fg_color='black')
prompt.place(relx=0.51, rely=0.9)

summar = customtkinter.CTkButton(master=app, text="Summarize", command=s ,height=40)
summar.place(relx=0.36, rely=0.9)

slider2 = customtkinter.CTkSlider(master=app, from_=0, to=80 ,  width=160)
slider2.place(relx=0.05, rely=0.6)

button2 = customtkinter.CTkButton(master=app, text=">", command=prompt_run , height=40 , width = 39 ,fg_color='black')
button2.place(relx=0.94, rely=0.9)

remove_pdf = customtkinter.CTkButton(app,text="Remove Pdf",command=remove_pdf,height=40, width=160)
remove_pdf.place(relx=0.05, rely=0.9)

combobox = customtkinter.CTkComboBox(master=app,
                                     values=["Pdf", "Current Text"],height=40, width=160
                                     )
combobox.place(relx=0.05, rely=0.7)
app.mainloop()
