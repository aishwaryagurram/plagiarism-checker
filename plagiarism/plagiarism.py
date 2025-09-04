import string
from tkinter import ttk
import tkinter as tk

def preprocess_text(text): 
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation)) 
    return text

def calculate_similarity(text1, text2):
    processed_text1 = preprocess_text(text1)
    processed_text2 = preprocess_text(text2)
    words1 = processed_text1.split()
    words2 = processed_text2.split()
    
    if not words1 or not words2:
        return 0.0  # Prevent division by zero
    
    intersection = len(set(words1) & set(words2))
    union = len(set(words1) | set(words2)) 
    similarity = intersection / union 
    return similarity

def calculate_and_display_similarity(): 
    document1 = entry_document1.get("1.0", tk.END).strip() 
    document2 = entry_document2.get("1.0", tk.END).strip() 
    similarity_score = calculate_similarity(document1, document2) 
    result_label.config(text=f"Similarity Score: {similarity_score:.2%}")

# Create the main window
root = tk.Tk() 
root.title("Text Similarity Calculator")

# Create and place widgets in the window
label_document1 = ttk.Label(root, text="Document 1:") 
label_document1.grid(row=0, column=0, padx=10, pady=5, sticky="w")

entry_document1 = tk.Text(root, height=4, width=40) 
entry_document1.grid(row=1, column=0, padx=10, pady=5) 

label_document2 = ttk.Label(root, text="Document 2:") 
label_document2.grid(row=2, column=0, padx=10, pady=5, sticky="w") 

entry_document2 = tk.Text(root, height=4, width=40) 
entry_document2.grid(row=3, column=0, padx=10, pady=5)

calculate_button = ttk.Button(root, text="Calculate Similarity", command=calculate_and_display_similarity)
calculate_button.grid(row=4, column=0, pady=10)

result_label = ttk.Label(root, text="Similarity Score: N/A") 
result_label.grid(row=5, column=0, pady=5)

# Start the Tkinter event loop
root.mainloop()
