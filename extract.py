from bs4 import BeautifulSoup

# Read the XML file
with open('data.xml', 'r') as file:
    xml_data = file.read()

# Parse the XML data using the XML parser
soup = BeautifulSoup(xml_data, 'lxml-xml')

# Find all <wp:meta_key> elements with a value of "country"
meta_keys = soup.find_all('wp:meta_key', string='country')

# Extract the corresponding <wp:meta_value> values and store unique countries in a set
countries = set(meta_key.find_next_sibling('wp:meta_value').string for meta_key in meta_keys)

# Sort the countries alphabetically
sorted_countries = sorted(countries)

# Print the sorted countries
for country in sorted_countries:
    print(country)