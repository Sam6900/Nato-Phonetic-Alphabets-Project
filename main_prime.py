# with open("file1.txt") as file:
#     lst1 = [int(line.rstrip()) for line in file.readlines()]
#     print(lst1)
#
# with open("file2.txt") as file:
#     lst2 = [int(line.rstrip()) for line in file.readlines()]
#     print(lst2)
#
# new_lst = [num for num in lst1 if num in lst2]
# print(new_lst)

# sentence = "My name is Sahil Sharma How are you"
# dct = {word: len(word) for word in sentence.split()}
# print(dct)

import pandas as pd

my_dict = {"Number": [10, 20, 30, 40, 50], "Marks": [100, 200, 300, 400, 500]}
# new_dict = {2 * key: 2 * value for key, value in my_dict.items()}
# print(new_dict)
df = pd.DataFrame(my_dict)
print(df)
# for key, column in df.items():
#     print(column)
x = 1
for index, row in df.iterrows():
    if x == 1:
        print(row.Marks)
        x += 1
