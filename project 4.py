"""
Project: Functional Treat - Data Analyzer and Transformer
Description: A menu-driven program to analyze and transform 1D list data 
using built-in functions, UDFs, *args, **kwargs, recursion, and lambda functions.
"""

# Global variable to store current dataset
dataset = []

def input_data():
    """Takes input values from user and stores them in the global dataset list."""
    global dataset
    user_input = input("\nEnter data for a 1D array (separated by spaces):\n")
    try:
        dataset = [float(x) if '.' in x else int(x) for x in user_input.strip().split()]
        print("\nData has been stored successfully!")
    except ValueError:
        print("\nError: Please enter valid numbers separated by spaces.")

def display_summary():
    """Displays basic dataset statistics using built-in functions like len(), min(), max(), sum()."""
    if not dataset:
        print("\nNo data available! Please input data first.")
        return
    
    total = len(dataset)
    min_val = min(dataset)
    max_val = max(dataset)
    sum_val = sum(dataset)
    avg_val = sum_val / total
    
    print("\nData Summary:")
    print(f"- Total elements: {total}")
    print(f"- Minimum value: {min_val}")
    print(f"- Maximum value: {max_val}")
    print(f"- Sum of all values: {sum_val}")
    print(f"- Average value: {avg_val:.2f}")

def calculate_factorial(n):
    """Calculates the factorial of a number using recursion."""
    if n < 0:
        return "Factorial does not exist for negative numbers."
    if n == 0 or n == 1:
        return 1
    return n * calculate_factorial(n - 1)

def filter_data_by_threshold():
    """Filters dataset values above or equal to a user-defined threshold using a lambda function."""
    if not dataset:
        print("\nNo data available! Please input data first.")
        return
    
    try:
        threshold = float(input("\nEnter a threshold value to filter out data above this value:\n"))
        # Using lambda function with filter
        filter_fn = lambda x: x >= threshold
        filtered_results = list(filter(filter_fn, dataset))
        
        formatted_results = ", ".join(str(x) for x in filtered_results)
        print(f"\nFiltered Data (values >= {threshold}):")
        print(formatted_results if formatted_results else "No values met the criteria.")
    except ValueError:
        print("\nError: Invalid input for threshold.")

def sort_data():
    """Sorts data in Ascending or Descending order."""
    if not dataset:
        print("\nNo data available! Please input data first.")
        return
        
    print("\nChoose sorting option:")
    print("1. Ascending")
    print("2. Descending")
    
    choice = input("\nEnter your choice: ")
    if choice == '1':
        sorted_list = sorted(dataset)
        print("\nSorted Data in Ascending Order:")
        print(", ".join(str(x) for x in sorted_list))
    elif choice == '2':
        sorted_list = sorted(dataset, reverse=True)
        print("\nSorted Data in Descending Order:")
        print(", ".join(str(x) for x in sorted_list))
    else:
        print("\nInvalid choice for sorting!")

def calculate_statistics(*args):
    """
    Calculates and returns multiple values: min, max, sum, and average of provided positional arguments (*args).
    """
    if not args:
        return None, None, None, None
    
    min_val = min(args)
    max_val = max(args)
    sum_val = sum(args)
    avg_val = sum_val / len(args)
    
    return min_val, max_val, sum_val, avg_val

def print_dataset_summary(**kwargs):
    """
    Demonstrates usage of **kwargs to display dataset characteristics as key-value pairs.
    """
    print("\nDataset Characteristics Summary (**kwargs):")
    for key, value in kwargs.items():
        print(f"- {key}: {value}")

def main():
    """Main menu loop for the application."""
    print("Welcome to the Data Analyzer and Transformer Program")
    
    while True:
        print("\nMain Menu:")
        print("1. Input Data")
        print("2. Display Data Summary (Built-in Functions)")
        print("3. Calculate Factorial (Recursion)")
        print("4. Filter Data by Threshold (Lambda Function)")
        print("5. Sort Data")
        print("6. Display Dataset Statistics (Return Multiple Values)")
        print("7. Exit Program")
        
        choice = input("Please enter your choice: ")
        
        if choice == '1':
            input_data()
            
        elif choice == '2':
            display_summary()
            
        elif choice == '3':
            try:
                num = int(input("\nEnter a number to calculate its factorial: "))
                result = calculate_factorial(num)
                print(f"\nFactorial of {num} is: {result}")
            except ValueError:
                print("\nPlease enter a valid integer.")
                
        elif choice == '4':
            filter_data_by_threshold()
            
        elif choice == '5':
            sort_data()
            
        elif choice == '6':
            if not dataset:
                print("\nNo data available! Please input data first.")
            else:
                # Unpacking *dataset as *args into calculate_statistics
                min_v, max_v, sum_v, avg_v = calculate_statistics(*dataset)
                
                print("\nDataset Statistics:")
                print(f"- Minimum value: {min_v}")
                print(f"- Maximum value: {max_v}")
                print(f"- Sum of all values: {sum_v}")
                print(f"- Average value: {avg_v:.2f}")
                
                # Demonstrating **kwargs usage optional feature requirement
                print_dataset_summary(
                    total_count=len(dataset),
                    minimum=min_v,
                    maximum=max_v,
                    average=round(avg_v, 2)
                )
                
        elif choice == '7':
            print("\nThank you for using the Data Analyzer and Transformer Program. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please select a valid option from 1 to 7.")

if __name__ == "__main__":
    main()