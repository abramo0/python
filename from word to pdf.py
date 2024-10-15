from tkinter import Tk, filedialog, messagebox, ttk
from docx2pdf import convert
import os
import threading
import time

def select_file(label):
    global file_path
    file_path = filedialog.askopenfilename()
    if file_path.endswith('.docx'):
        label.config(text=f"Selected file: {file_path}")
    else:
        messagebox.showerror("Error", "The selected file is not a .docx file")

def convert_file(progress_bar):
    if file_path:
        # Aggiorna la progress bar (0%)
        progress_bar['value'] = 0
        root.update_idletasks()

        # Simuliamo un piccolo ritardo per mostrare la progressione (puoi rimuoverlo)
        time.sleep(1)
        progress_bar['value'] = 20
        root.update_idletasks()

        try:
            output_path = os.path.splitext(file_path)[0] + ".pdf"
            # Esegui la conversione in un thread separato
            convert(file_path, output_path)

            # Aggiorna la progress bar (100%)
            progress_bar['value'] = 100
            root.update_idletasks()
            messagebox.showinfo("Success", f"File converted and inserted into: {output_path}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during the conversion: {e}")
        finally:
            # Reset della progress bar dopo la conversione
            progress_bar['value'] = 0
            root.update_idletasks()
    else:
        messagebox.showerror("Error", "No file selected")

def start_conversion(progress_bar):
    # Crea un thread per eseguire la conversione
    thread = threading.Thread(target=convert_file, args=(progress_bar,))
    thread.start()

def graphics():
    global root
    root = Tk()
    root.title("Convert from .docx to .pdf")
    frm = ttk.Frame(root, padding=200)
    frm.grid()
    
    # Etichetta per la selezione del file
    ttk.Label(frm, text="Select the file").grid(column=0, row=0)
    file_label = ttk.Label(frm, text="")
    file_label.grid(column=0, row=1, columnspan=2)

    # Bottone per sfogliare i file
    ttk.Button(frm, text="Browse", command=lambda: select_file(file_label)).grid(column=1, row=0)

    # Bottone per avviare la conversione
    ttk.Button(frm, text="Convert", command=lambda: start_conversion(progress_bar)).grid(column=2, row=0)

    # Aggiungi la Progress Bar
    global progress_bar
    progress_bar = ttk.Progressbar(frm, orient='horizontal', length=200, mode='determinate')
    progress_bar.grid(column=0, row=2, columnspan=3, pady=10)

    root.mainloop()

if __name__ == "__main__":
    file_path = None
    graphics()
