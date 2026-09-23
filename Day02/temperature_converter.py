current_celcius = float(input("Enter the Celcius value - "))

print("Kelvin Temp - " , current_celcius + 273.15 , " | " ,
      "Fahrenheit Temp - " , (current_celcius * 9/5) + 32)

current_kelvin = float(input("Enter the Kelvin value - "))
fahrenheit_temp = ((current_kelvin - 273.15) * 9/5)+32

print("Celcius Temp - " , current_kelvin - 273.15 , " | " ,
      f"Farenheit Temp - {fahrenheit_temp}")