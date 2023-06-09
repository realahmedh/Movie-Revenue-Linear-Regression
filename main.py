import tkinter as tk
from tkinter import messagebox
import pickle

# Create a GUI using tkinter
root = tk.Tk()
root.title('Revenue Predictor')


# Create a function that uses the saved model to predict the revenue
def predict_revenue():
    try:
        # Load the saved model
        with open('model.pkl', 'rb') as f:
            model = pickle.load(f)

        # Get the input from the user
        budget = float(budget_input.get())

        # Use the model to predict the revenue
        revenue = model.predict([[budget]])[0]

        # Display the predicted revenue in the GUI
        result_label.config(text='Predicted Revenue: ${:,.2f}'.format(revenue))

    except ValueError:
        messagebox.showerror('Error', 'Invalid input. Please enter a valid number.')


# Create a label and an entry field for the budget input
budget_label = tk.Label(root, text='Production Budget ($):')
budget_label.pack()
budget_input = tk.Entry(root)
budget_input.pack()

# Create a button to predict the revenue
predict_button = tk.Button(root, text='Predict Revenue', command=predict_revenue)
predict_button.pack()

# Create a label to display the predicted revenue
result_label = tk.Label(root)
result_label.pack()

# Run the GUI
root.mainloop()
