import sys
import requests

def calculate_cost_in_usd(amount_in_btc):
    try:
        # Fetch the current exchange rate of Bitcoin in USD from the coindesk API
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        current_price = data["bpi"]["USD"]["rate_float"]
        # Multiply the current price of Bitcoin in USD by the provided amount in Bitcoin
        return current_price * amount_in_btc
    except requests.RequestException:
        # Exit the program if there is a request exception
        sys.exit()

def main():
    try:
        # Attempt to convert the first command line argument to a float
        n = float(sys.argv[1])
    except IndexError:
        # If there are no command-line arguments, print an error message and exit the program
        sys.exit("Missing command-line argument")
    except ValueError:
        # If the first command-line argument cannot be converted to a float, print an error message and exit the program
        sys.exit("Command-line argument is not a number")

    # Calculate the cost of valid amount of Bitcoin in USD
    cost_in_usd = calculate_cost_in_usd(n)
    # Print the USD value
    print(f"${cost_in_usd:,.4f}")

# Call the main function if the script is run as a standalone program
if __name__ == "__main__":
    main()
