def temp_converty():
    # Prompt user to choose between Celsius to Fahrenheit or Fahrenheit to Celsius
    choice = int(input("Enter 1 for Celsius to Fahrenheit and 2 for Fahrenheit to Celsius: "))

    # Convert temperature based on user's choice
    if choice == 1:  # Celsius to Fahrenheit
        celsius = float(input("Enter the temperature in Celsius: "))
        fahrenheit = (celsius * 9 / 5) + 32
        print("The temperature is {:.2f} Fahrenheit".format(fahrenheit))
    elif choice == 2:  # Fahrenheit to Celsius
        fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5 / 9
        print("The temperature is {:.2f} Celsius".format(celsius))
