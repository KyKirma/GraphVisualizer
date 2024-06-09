import tkinter as tk

def main():
    # Create the main window
    window = tk.Tk()
    window.title("Grid Layout Example")

    # Configure the window size and minimum size
    window.geometry("400x300")
    window.minsize(width=400, height=300)

    # Create and configure the frames
    header_frame = tk.Frame(window, background="#d3d3d3")
    header_frame.grid(row=0, columnspan=3, sticky="nsew", padx=5, pady=5)

    left_frame = tk.Frame(window, background="#f2f2f2")
    left_frame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

    right_frame = tk.Frame(window, background="#f2f2f2")
    right_frame.grid(row=1, columnspan=2, sticky="nsew", padx=5, pady=5)

    # Create and configure the widgets within the frames
    header_label = tk.Label(header_frame, text="Grid Layout Example", font=("Arial", 16, "bold"))
    header_label.grid(row=0, column=0, sticky="w")

    label1 = tk.Label(left_frame, text="Label 1", width=15)
    label1.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

    entry1 = tk.Entry(left_frame, width=20)
    entry1.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

    button1 = tk.Button(left_frame, text="Button 1")
    button1.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

    label2 = tk.Label(right_frame, text="Label 2", width=15)
    label2.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

    entry2 = tk.Entry(right_frame, width=20)
    entry2.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

    button2 = tk.Button(right_frame, text="Button 2")
    button2.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

    # Adjust column weights to distribute space evenly
    window.columnconfigure(1, weight=1)
    right_frame.columnconfigure(0, weight=1)

    # Run the main event loop
    window.mainloop()

if __name__ == "__main__":
    main()
