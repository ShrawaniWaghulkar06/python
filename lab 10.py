# import pandas as pd

# # Load the dataset
# try:
#     df = pd.read_csv('books.csv')
    
#     # a) Print the complete report of books in a Tabular form
#     print("--- Complete Book Report ---")
#     print(df.to_string(index=False))
#     print("\n")

#     # b) Print the list of available books of a given author
#     author_name = input("Enter Author Name to search: ")
#     author_books = df[df['author'] == author_name]
#     print(f"Books by {author_name}:")
#     print(author_books if not author_books.empty else "No books found.")
#     print("\n")

#     # c) Print the list of available books of a given publishing house
#     publisher_name = input("Enter Publishing House to search: ")
#     pub_books = df[df['publishing_house'] == publisher_name]
#     print(f"Books from {publisher_name}:")
#     print(pub_books if not pub_books.empty else "No books found.")
#     print("\n")

#     # d) Print the Titles of cheapest & costliest book available
#     cheapest = df.loc[df['price'].idxmin(), 'title']
#     costliest = df.loc[df['price'].idxmax(), 'title']
#     print(f"Cheapest Book: {cheapest}")
#     print(f"Costliest Book: {costliest}")
#     print("\n")

#     # e) Print the list by sorting based on the year of publication
#     print("--- Books Sorted by Publication Year ---")
#     sorted_df = df.sort_values(by='publication_year')
#     print(sorted_df.to_string(index=False))

# except FileNotFoundError:
#     print("Error: 'books.csv' file not found.")
import pandas as pd

# Create a table (DataFrame) showing information about 5 states
data = {
    'State': ['Maharashtra', 'Rajasthan', 'Goa', 'Uttar Pradesh', 'Sikkim'],
    'Area': [307713, 342239, 3702, 240928, 7096],
    'Population': [112374333, 68548437, 1458545, 199812341, 610577]
}

df_states = pd.DataFrame(data)

# a) Print the complete information of states
print("--- State Information ---")
print(df_states)
print("\n")

# b) Print the name of the State having largest Area
largest_area_state = df_states.loc[df_states['Area'].idxmax(), 'State']
print(f"State with largest Area: {largest_area_state}")

# c) Print the name of State having largest population
largest_pop_state = df_states.loc[df_states['Population'].idxmax(), 'State']
print(f"State with largest Population: {largest_pop_state}")

# d) Create a mechanism to calculate the population density (Population / Area)
df_states['Population_Density'] = df_states['Population'] / df_states['Area']
print("\n--- Updated Table with Population Density ---")
print(df_states)

# e) Determine the name of State with highest population density
highest_density_state = df_states.loc[df_states['Population_Density'].idxmax(), 'State']
print(f"\nState with highest Population Density: {highest_density_state}")

