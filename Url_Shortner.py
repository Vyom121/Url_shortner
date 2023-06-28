# import pyshorteners

# # URL shorting function
# def shorten_url(url):
#     # Initialize the Shortener object
#     s = pyshorteners.Shortener()

#     # Shorten the URL
#     shortened_url = s.tinyurl.short(url)

#     return shortened_url


# url_value=input("Enter the URL:")
# print("Shortened URL:",shorten_url(url_value))


import pyshorteners
import tkinter as tk

def shorten_url():
    # Retrieve the long URL from the Entry widget
    long_url = entry_url.get()

    # Initialize the Shortener object
    s = pyshorteners.Shortener()

    # Shorten the URL
    shortened_url = s.tinyurl.short(long_url)

    # Update the result label with the shortened URL
    result_label.config(text=shortened_url)

# Create the main window
window = tk.Tk()
window.title("URL Shortener")

# Create an Entry widget to enter the long URL
entry_url = tk.Entry(window, width=50)
entry_url.pack(pady=10)

# Create a button to shorten the URL
button_shorten = tk.Button(window, text="Shorten", command=shorten_url)
button_shorten.pack()

# Create a label to display the result
result_label = tk.Label(window, text="")
result_label.pack(pady=10)

# Start the GUI main loop
window.mainloop()