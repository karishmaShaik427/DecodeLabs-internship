def track_expenses():
    # Initialize the accumulator variable
    total_spent = 0.0
    
    print("====================================")
    print("   DecodeLabs Expense Tracker v1.0  ")
    print("====================================")
    print("Enter your expenses one by one.")
    print("Type 'exit' or 'done' when you are finished.\n")
    
    while True:
        user_input = input("Enter expense amount ($): ").strip().lower()
        
        # Check if the user wants to stop entering expenses
        if user_input in ['exit', 'done']:
            break
            
        try:
            # Convert input to a float for decimal support (e.g., 10.50)
            expense = float(user_input)
            
            # Prevent negative expense inputs
            if expense < 0:
                print("❌ Expense cannot be negative. Please enter a valid amount.")
                continue
            
            # The Accumulator Pattern: total = total + new_expense
            total_spent += expense
            print(f"Added ${expense:.2f}. Current Total: ${total_spent:.2f}\n")
            
        except ValueError:
            # Handle cases where input is not a number
            print("❌ Invalid input! Please enter a numeric value or type 'exit' to finish.\n")
            
    print("\n====================================")
    print(f"🎉 Session Finished! TOTAL SPENT: ${total_spent:.2f}")
    print("====================================")

if __name__ == "__main__":
    track_expenses()
