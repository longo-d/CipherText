import tkinter as tk
import tkinter.messagebox

# resources
# https://realpython.com/python-gui-tkinter/
# https://www.pythonguis.com/tutorials/create-ui-with-tkinter-grid-layout-manager/
# https://docs.python.org/3/library/tkinter.ttk.html
# https://docs.python.org/3/tutorial/inputoutput.html

def createGUI(): 
    # creates window
    window = tk.Tk()

    # set window size
    window.geometry("1200x800")

    # set window title
    window.title("Cipher Script")

    # background frame
    frameBackground = tk.Frame(
        master = window,
        width=1200,
        height=800
    )
    frameBackground.pack(pady=50, padx=50)

    # input frame
    frameInput = tk.Frame(
        master = frameBackground,
        width=1000,
        height=200
    )
    frameInput.grid(row=0, column=0)

    # input button frame
    frameInputButton = tk.Frame(
        master = frameBackground,
        width=1000,
        height=50
    )
    frameInputButton.grid(row=1, column=0)

    # frame spacing
    frameSpace = tk.Frame(
        master = frameBackground,
        width=1000,
        height=100
    )
    frameSpace.grid(row=2, column=0)

    # output frame
    frameOutput = tk.Frame(
        master = frameBackground,
        width=1000,
        height=200
    )
    frameOutput.grid(row=3, column=0)

    # output button frame
    frameOutputButton = tk.Frame(
        master = frameBackground,
        width=1000,
        height=50
    )
    frameOutputButton.grid(row=4, column=0)

    # disclaimer frame
    frameDisclaimer = tk.Frame(
        master = frameBackground,
        width=1100,
        height=50
    )
    frameDisclaimer.grid(row=5, column=0, columnspan=2)

    # key frame
    frameKey = tk.Frame(
        master = frameBackground,
        width=100,
        height=350
    )
    frameKey.grid(row=0, column=1, rowspan=3)

    # help frame
    frameHelp = tk.Frame(
        master = frameBackground,
        width=100,
        height=250
    )
    frameHelp.grid(row=3, column=1, rowspan=2)

    # label for inputting a message
    inputMessageLabel = tk.Label(
        master = frameInput,
        text = "Input Message:",
        font=("Arial", 14),
        width = 15,
        height = 2
    )
    inputMessageLabel.grid(row=0, column=0, sticky="W")

    # text for user input of accepting a message
    inputMessage = tk.Text(
        master = frameInput, 
        font=("Arial", 14),
        width = 90,
        height = 6,
        relief=tk.RIDGE,
        borderwidth="2px",
        background="white"
    )
    inputMessage.grid(row=1, column=0)

    # get the input message
    message = inputMessage.get("1.0", tk.END)

    # blank label to create space
    blankInputLabel = tk.Label(
        master = frameInputButton,
        text = "          ",
        font = ("Arial", 14),
        width = 65,
        height = 2
    )
    blankInputLabel.grid(row=0, column=0, columnspan=4)

    # button for choosing encryption
    encryptButton = tk.Button(
        master = frameInputButton,
        text = "Encrypt",
        font = ("Arial", 14),
        width = 10,
        height = 1,

    )
    encryptButton.grid(row=0, column=5, padx=5, sticky="E")

    # button for choosing decryption
    decryptButton = tk.Button(
        master = frameInputButton,
        text = "Decrypt",
        font = ("Arial", 14),
        width = 10,
        height = 1,
        
    )
    decryptButton.grid(row=0, column=6, padx=5, sticky="E")

    # label for outputting a message
    outputMessageLabel = tk.Label(
        master = frameOutput,
        text = "Translated Message:",
        font=("Arial", 14),
        width = 20,
        height = 2
    )
    outputMessageLabel.grid(row=0, column=0, sticky="W")

    # output translated text from user message
    outputMessage = tk.Label(
        master = frameOutput,
        font=("Arial", 14),
        width = 90,
        height = 6,
        relief=tk.RIDGE,
        borderwidth="2px",
        background="white"
    )
    outputMessage.grid(row=1, column=0)

    # blank label to create space
    blankOutputLabel = tk.Label(
        master = frameOutputButton,
        text = "          ",
        font = ("Arial", 14),
        width = 75,
        height = 2
    )
    blankOutputLabel.grid(row=0, column=0, columnspan=4)

    # button for copying the translated message
    copyButton = tk.Button(
        master = frameOutputButton,
        text = "Copy",
        font = ("Arial", 14),
        width = 10,
        height = 1
    )
    copyButton.grid(row=0, column=5, sticky="E")

    # disclaimer text 
    disclaimerMessage = tk.Label(
        master = frameDisclaimer, 
        text = "*DISCLAIMER: use of a cipher should not be used as a substitute for encryption purposes.",
        font=("Arial", 14),
        width = 100,
        height = 1
    )
    disclaimerMessage.grid(row=0, column=0)

    # label for key value
    keyLabel = tk.Label(
        master = frameKey,
        text = "Key:",
        font=("Arial", 14),
        width = 5,
        height = 2
    )
    keyLabel.grid(row=0, column=0, sticky="W")

    # spinbox for key value
    keySpin = tk.Spinbox(
        master = frameKey,
        from_= 0, to = 26,
        font = ("Arial", 14),
        width=3,
        wrap=True,
        state="readonly"
    )
    keySpin.grid(row=1, column=0, sticky="W", padx=10)

    # blank label to create space
    blankKeyLabel = tk.Label(
        master = frameKey,
        text = "          ",
        font = ("Arial", 14),
        width = 10,
        height = 11
    )
    blankKeyLabel.grid(row=2, column=0, columnspan=2)

    # button for help
    helpButton = tk.Button(
        master = frameHelp,
        text = "Help?",
        font = ("Arial", 14),
        width = 7,
        height = 1,
        command=onHelpClick
    )
    helpButton.grid(row=0, column=0, sticky="N")

    # packing of elements
    frameBackground.pack()
    
    # listens for events
    window.mainloop()

# help message box
def onHelpClick():
    # opens helpFile.txt and reads the file
    with open("helpFile.txt") as file:
        helpFile = file.read()
        tkinter.messagebox.showinfo("Help", str(helpFile))

# calls createGUI() function
createGUI()