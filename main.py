student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import csv

# Can also be done using df.iterrows() in pandas
with open("nato_phonetic_alphabet.csv") as file:
    data = list(csv.reader(file))
    my_dict = {row[0]: row[1] for row in data[1:]}
    # print(my_dict)

name = input("Enter your name: ")
my_lst = [my_dict[letter] for letter in name.upper()]
print(my_lst)
