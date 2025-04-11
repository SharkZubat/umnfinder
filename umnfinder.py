import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Dictionary of magic numbers to file types
MAGIC_NUMBERS = {
    b"\x89PNG\r\n\x1a\n": "PNG Image",
    b"\xFF\xD8\xFF": "JPEG Image",
    b"GIF87a": "GIF Image (GIF87a)",
    b"GIF89a": "GIF Image (GIF89a)",
    b"\x25\x50\x44\x46": "PDF Document",
    b"\x50\x4B\x03\x04": "ZIP Archive",
    b"\x1F\x8B": "GZIP Archive",
    # Add more magic numbers as needed
}

def get_magic_number(file_path):
    """Gets the magic number name for a file."""
    try:
        with open(file_path, "rb") as file:
            file_header = file.read(16)  # Read the first 16 bytes
            for magic, file_type in MAGIC_NUMBERS.items():
                if file_header.startswith(magic):
                    return file_type
            return "Unknown File Type"
    except Exception as e:
        return f"Error reading file: {e}"

def start_locator():
    """Start the UMNFinder locator."""
    if not file_paths:
        messagebox.showwarning("No Files Selected", "Please select files to analyze.")
        return
    
    results = []
    for file_path in file_paths:
        file_name = os.path.basename(file_path)
        magic_name = get_magic_number(file_path)
        results.append(f"{file_name}: {magic_name}")
    
    # Display results in a message box
    messagebox.showinfo("UMNFinder Results", "\n".join(results))

def add_files():
    """Add files to the list."""
    global file_paths
    selected_files = filedialog.askopenfilenames(title="Select Files")
    if selected_files:
        file_paths.extend(selected_files)
        files_listbox.delete(0, tk.END)
        for file in file_paths:
            files_listbox.insert(tk.END, file)

def clear_files():
    """Clear all selected files."""
    global file_paths
    file_paths = []
    files_listbox.delete(0, tk.END)

# Initialize the main Tkinter window
file_paths = []
root = tk.Tk()
root.title("UMNFinder")

# Create and place widgets
title_label = tk.Label(root, text="UMNFinder", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

files_listbox = tk.Listbox(root, width=50, height=10)
files_listbox.pack(pady=10)

add_files_button = tk.Button(root, text="Add Files", command=add_files)
add_files_button.pack(pady=5)

clear_files_button = tk.Button(root, text="Clear Files", command=clear_files)
clear_files_button.pack(pady=5)

start_button = tk.Button(root, text="Start Locator", command=start_locator)
start_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()