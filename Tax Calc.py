def calculate_weekly_tax(weekly_salary):
    # Calculate annual salary
    annual_salary = weekly_salary * 52
    
    # Australian tax brackets for 2023-2024
    if annual_salary <= 18200:
        annual_tax = 0
    elif annual_salary <= 45000:
        annual_tax = (annual_salary - 18200) * 0.19
    elif annual_salary <= 120000:
        annual_tax = 5092 + (annual_salary - 45000) * 0.325
    elif annual_salary <= 180000:
        annual_tax = 29467 + (annual_salary - 120000) * 0.37
    else:
        annual_tax = 51667 + (annual_salary - 180000) * 0.45
    
    # Calculate weekly tax
    weekly_tax = annual_tax / 52
    
    # Calculate Medicare Levy (2% of annual salary)
    annual_medicare_levy = annual_salary * 0.02
    weekly_medicare_levy = annual_medicare_levy / 52
    
    # Total weekly tax
    total_weekly_tax = weekly_tax + weekly_medicare_levy
    
    return total_weekly_tax

def calculate_superannuation(weekly_salary):
    # Superannuation is 10% of pre-tax income
    weekly_superannuation = weekly_salary * 0.10
    return weekly_superannuation

# Main function to get user input and calculate tax and superannuation
def main():
    try:
        weekly_salary = float(input("Enter your weekly salary: "))
        if weekly_salary < 0:
            print("Please enter a valid positive number for your salary.")
            return
        
        weekly_tax = calculate_weekly_tax(weekly_salary)
        weekly_superannuation = calculate_superannuation(weekly_salary)
        
        print(f"You should set aside approximately AUD {weekly_tax:.2f} for tax each week.")
        print(f"Your weekly superannuation contribution should be approximately AUD {weekly_superannuation:.2f}.")
    
    except ValueError:
        print("Invalid input. Please enter a numerical value for your salary.")

if __name__ == "__main__":
    main()