from tkinter import *

# Initialize the main application window
root = Tk()
root.title("Paint App")  # Set window title
root.geometry("1100x600")  # Set window size
root.resizable(False, False)  # Disable window resizing

# Create the top frame for holding tools
frame1 = Frame(root, height=150, width=1100, bg="red")
frame1.grid(row=0, column=0, sticky=NW) # NW = North West = Top Left Corner

# Create a sub-frame inside frame1 for tools
toolsFrame = Frame(frame1, height=100, width=100, bg='green')
toolsFrame.grid(row=0, column=0)

# Variable to store the stroke color
stroke_color = StringVar()
stroke_color.set("green")  # Default color

# Function to activate the pencil tool
def usePencil():
    stroke_color.set("black")  # Set drawing color to black
    canvas["cursor"] = "pencil"  # Change cursor to indicate pencil

# Function to activate the eraser tool
def useEraser():
    stroke_color.set("white")  # Set drawing color to white (acts as eraser)
    canvas["cursor"] = "X_cursor"  # Change cursor to indicate eraser

# Button to select the pencil tool
pencilButton = Button(toolsFrame, text="Pencil", width=10, command=usePencil)
pencilButton.grid(row=0, column=0)

# Button to select the eraser tool
eraserButton = Button(toolsFrame, text="Eraser", width=10, command=useEraser)
eraserButton.grid(row=1, column=0)

# Label for the tools section
toolsLabel = Label(toolsFrame, text="Tools", width=10)
toolsLabel.grid(row=3, column=0)

# Create the bottom frame where the canvas will be placed
frame2 = Frame(root, height=450, width=1100, bg="blue")
frame2.grid(row=1, column=0)

# Create the canvas where users can draw
canvas = Canvas(frame2, height=450, width=1100, bg="white")
canvas.grid(row=0, column=0)

# Variables to keep track of previous and current points for drawing
prevPoint = [0, 0]
currentPoint = [0, 0]

# Function to handle drawing on the canvas
def paint(event):
    global prevPoint, currentPoint
    
    # Get the current cursor position
    x = event.x
    y = event.y
    currentPoint = [x, y]
    
    # Draw a line from the previous point to the current point
    if prevPoint != [0, 0]:
        canvas.create_line(prevPoint[0], prevPoint[1], currentPoint[0], currentPoint[1], fill=stroke_color.get())
    
    # Update previous point
    prevPoint = currentPoint
    
    # Reset previous point when mouse button is released
    if event.type == "5":  # ButtonRelease event
        prevPoint = [0, 0]

# Bind mouse events to the canvas
canvas.bind("<B1-Motion>", paint)  # Draw while holding left mouse button
canvas.bind("<ButtonRelease-1>", paint)  # Reset previous point on mouse release

# Run the Tkinter event loop
root.mainloop()
