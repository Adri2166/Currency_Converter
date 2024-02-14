Currency Converter
This Python script enables users to convert currency based on the latest exchange rates or historical rates for a specific date. It utilizes the Frankfurter API to fetch currency exchange rate data.
(https://github.com/Adri2166/Currency_Converter.git)

Usage
Installation: Ensure you have Python installed on your system.

Dependencies: The script relies on the requests library. You can install it via pip:


pip install requests
Running the Script: Execute the script in your Python environment.


python currency_converter.py
Usage Instructions: Follow the prompts to input the required details:

Enter the currency you want to convert from and to.
Input the amount you want to convert.
Choose whether you want to convert based on today's rate or a specific date. If selecting a specific date, input the date in DD/MM/YYYY format.
Example
python
Copy code
Enter the currency you'd like to convert from: USD
Enter the currency you'd like to convert to: EUR
Enter the amount of money: 100
Please, enter the date you need in DD/MM/YYYY format: 15/01/2023
100.0 USD ==> 87.81 EUR
Note
Ensure your system is connected to the internet to fetch the latest currency exchange rates.
For historical rates, the script relies on the availability of data from the Frankfurter API.
Feel free to contribute to and enhance this script as needed!
