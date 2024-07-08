


# Step 2: Generating Real Estate Listings

# Ask the user for the number of listings they want to create
n = input("Enter the number of real estate listings you want to create: ")

# Ensure the input is an integer
try:
    n = int(n)
except ValueError:
    print("Please enter a valid number.")
    exit()
example_format = """

Neighborhood: Green Oaks
Price: $800,000
Bedrooms: 3
Bathrooms: 2
House Size: 2,000 sqft
Description: Welcome to this eco-friendly oasis nestled in the heart of Green Oaks. This charming 3-bedroom, 2-bathroom home boasts energy-efficient features such as solar panels and a well-insulated structure. Natural light floods the living spaces, highlighting the beautiful hardwood floors and eco-conscious finishes. The open-concept kitchen and dining area lead to a spacious backyard with a vegetable garden, perfect for the eco-conscious family. Embrace sustainable living without compromising on style in this Green Oaks gem.
Neighborhood Description: Green Oaks is a close-knit, environmentally-conscious community with access to organic grocery stores, community gardens, and bike paths. Take a stroll through the nearby Green Oaks Park or grab a cup of coffee at the cozy Green Bean Cafe. With easy access to public transportation and bike lanes, commuting is a breeze."""
Prompt = f"Create {n} Real estate listing for the following property with the following example format:{example_format}\n\n"

print(Prompt)
# Step 3: Storing Listings in a Vector Database