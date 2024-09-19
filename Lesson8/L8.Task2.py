# Creating a dictionary.

# Create a function called make_country,
# which takes in a country’s name and capital as parameters.
# Then create a dictionary from those parameters, with ‘name’ and ‘capital’ as keys.
# Make the function print out the values of the dictionary to make sure that it works as intended.

def make_country(name, capital):
    country_dict = {
        "name": name,
        "capital": capital,
    }
    return country_dict


print(make_country('Ukraine', 'Kiev'))
