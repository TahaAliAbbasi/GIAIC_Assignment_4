def main():
    print("\nFahrenheit to Celcius convertor !\n")
    user = float(input("Enter temperature in Fahrenheit : "))
    
    celcius = (user - 32) * 5.0/9.0

    print(f"Temperature in fahrenheit = {user} \n Temperature in celcius = {celcius:.2f}")

if __name__ == '__main__':
    main()