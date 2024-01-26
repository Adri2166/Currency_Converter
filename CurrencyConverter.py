import requests

# Function to prompt user for input and validate
def get_user_choice():
    while True:
        user_input = input("Please, enter the date you need in DD/MM/YYYY format: ").upper()

        if len(user_input) == 10 and user_input[2] == '/' and user_input[5] == '/':
            return user_input
        else:
            print("Incorrect input. Please enter a correct date.")

# Main function for currency conversion
def convert_currency():
    from_currency = str(input("Enter the currency you'd like to convert from: ")).upper()
    to_currency = str(input("Enter the currency you'd like to convert to: ")).upper()

    amount = float(input("Enter the amount of money: "))

    # Ask user for choice
    user_choice = get_user_choice()

    if user_choice == True:
        response = requests.get(f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")
    else:
        day, month, year = user_choice.split('/')
        date_formatted = f"{year}-{month}-{day}"
        response = requests.get(f"https://api.frankfurter.app/{date_formatted}?amount={amount}&from={from_currency}&to={to_currency}")

    if response.status_code == 200:
        data = response.json()
        if 'rates' in data:
            conversion_rate = data['rates'][to_currency]
            print(f"{amount} {from_currency} ==> {conversion_rate} {to_currency}")
        else:
            print("Error: Currency rates not found in response.")
    else:
        print(f"Error: Request failed with status code {response.status_code}")

# Call the main function
convert_currency()

