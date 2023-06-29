import pyshorteners
import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.ttk as ttk

def shorten_url():
    long_url = entry_url.get()
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(long_url)
    result_label.config(text=shortened_url)

def copy_to_clipboard():
    window.clipboard_clear()
    window.clipboard_append(result_label.cget("text"))
    messagebox.showinfo("Copied!", "The shortened URL has been copied to the clipboard.")

window = tk.Tk()
window.title("URL Shortener Application")
window.resizable(False, False)
window.geometry("500x150")

label_instructions = tk.Label(window, text="Enter a long URL to shorten:")
label_instructions.pack(pady=5)

frame_input = tk.Frame(window)
frame_input.pack(pady=5)

entry_url = ttk.Entry(frame_input, width=50)
entry_url.pack(side=tk.LEFT)

button_shorten = ttk.Button(frame_input, text="Shorten", command=shorten_url)
button_shorten.pack(side=tk.LEFT, padx=5)

frame_result = tk.Frame(window)
frame_result.pack(pady=5)

result_label = ttk.Label(frame_result, text="")
result_label.pack(side=tk.LEFT)

button_copy = ttk.Button(frame_result, text="Copy", command=copy_to_clipboard)
button_copy.pack(side=tk.LEFT, padx=5)

style = ttk.Style()
style.configure("TButton", padding=6)
style.configure("TLabel", padding=4)
style.configure("TEntry", padding=4)
style.configure("TFrame", padding=6)

window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
window.mainloop()
