import tkinter as tk
import numpy as np

def bankers_algorithm(num_processes, num_resources, current_allocation, max_matrix, available_resources):
    finish = np.zeros(num_processes, dtype=int)
    safe_seq = np.zeros(num_processes, dtype=int)
    seq_index = 0
    need = np.zeros((num_processes, num_resources), dtype=int)

    for i in range(num_processes):
        for j in range(num_resources):
            need[i][j] = max_matrix[i][j] - current_allocation[i][j]

    is_safe_state = False  # Track if a safe sequence is found

    for _ in range(num_processes):
        for process_index in range(num_processes):
            if finish[process_index] == 0:
                is_safe = True
                for resource_index in range(num_resources):
                    if need[process_index][resource_index] > available_resources[resource_index]:
                        is_safe = False
                        break

                if is_safe:
                    safe_seq[seq_index] = process_index
                    seq_index += 1
                    for resource_index in range(num_resources):
                        available_resources[resource_index] += current_allocation[process_index][resource_index]
                    finish[process_index] = 1
                    is_safe_state = True  # Set safe state flag to True

    if is_safe_state:
        safe_sequence = [f"P{process_num + 1}" for process_num in safe_seq]
        display_message(f"The system is in a safe state.\nSafe Sequence: {', '.join(safe_sequence)}")
    else:
        display_message("The system is in an unsafe state.")

def run_code():
    num_processes = int(processes_entry.get())
    num_resources = int(resources_entry.get())

    current_allocation_text = current_allocation_textbox.get("1.0", tk.END)
    current_allocation = [[int(val) for val in row.split()] for row in current_allocation_text.strip().split("\n")]

    max_matrix_text = max_matrix_textbox.get("1.0", tk.END)
    max_matrix = [[int(val) for val in row.split()] for row in max_matrix_text.strip().split("\n")]

    available_resources = list(map(int, available_resources_entry.get().split()))

    bankers_algorithm(num_processes, num_resources, current_allocation, max_matrix, available_resources)

# Create the main window
window = tk.Tk()
window.title("Bankers Algorithm")

# Create labels and entry fields for num_processes and num_resources
processes_label = tk.Label(window, text="Number of Processes:")
processes_label.grid(row=0, column=0, sticky=tk.W)

processes_entry = tk.Entry(window)
processes_entry.grid(row=0, column=1)

resources_label = tk.Label(window, text="Number of Resources:")
resources_label.grid(row=1, column=0, sticky=tk.W)

resources_entry = tk.Entry(window)
resources_entry.grid(row=1, column=1)

# Create label and text box for current_allocation matrix
current_allocation_label = tk.Label(window, text="Current Allocation:")
current_allocation_label.grid(row=2, column=0, sticky=tk.W)

current_allocation_textbox = tk.Text(window, width=40, height=5)
current_allocation_textbox.grid(row=3, column=0, columnspan=2)

# Create label and text box for max_matrix
max_matrix_label = tk.Label(window, text="Maximum Resource Matrix:")
max_matrix_label.grid(row=8, column=0, sticky=tk.W)

max_matrix_textbox = tk.Text(window, width=40, height=5)
max_matrix_textbox.grid(row=9, column=0, columnspan=2)

# Create label and entry field for available_resources
available_resources_label = tk.Label(window, text="Available Resources:")
available_resources_label.grid(row=14, column=0, sticky=tk.W)

available_resources_entry = tk.Entry(window)
available_resources_entry.grid(row=14, column=1)

# Create the run button
run_button = tk.Button(window, text="Run", command=run_code)
run_button.grid(row=15, column=0, columnspan=2)

# Create the message box
message_box = tk.Text(window, width=40, height=5)
message_box.grid(row=16, column=0, columnspan=2, pady=10)

def display_message(message):
    message_box.insert(tk.END, message + "\n")

# Start the main event loop
window.mainloop()