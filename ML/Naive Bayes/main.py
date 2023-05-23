# Formulate Question -> Gather Data from a Website -> Clean Data

from os import walk
from os.path import join

import pandas as pd

ex_file = 'SpamData/01_Processing/practice_email.txt'
spam_1_path = 'SpamData/01_Processing/spam_assassin_corpus/spam_1'
spam_2_path = 'SpamData/01_Processing/spam_assassin_corpus/spam_2'
easy_nonspam_1_path = 'SpamData/01_Processing/spam_assassin_corpus/easy_ham_1'
easy_nonspam_2_path = 'SpamData/01_Processing/spam_assassin_corpus/easy_ham_2'


# Reading the file

# stream = open(ex_file, "r")
# is_body = False
# f = open("demofile.txt", "r")

# email_txt = stream.read()
# print(email_txt)
# print(stream.readlines())
# lines = []
# for text in stream:
#     if is_body:
#         lines.append(text)
#     elif text == '\n':
#         is_body = True
#
# email_body = '\n'.join(lines)


# print(email_body)

def generate_square(n):
    for number in range(n):
        yield number ** 2


# for i in generate_square(5):
#     print(i, end=' -> ')

def email_body_generator(path):
    for root, dir_names, filenames in walk(path):
        for file_name in filenames:
            filepath = join(root, file_name)
            stream = open(filepath, encoding='latin-1')

            is_body = False
            lines = []

            for line in stream:
                if is_body:
                    lines.append(line)
                elif line == '\n':
                    is_body = True

            stream.close()

            email_body = '\n'.join(lines)
            yield file_name, email_body


def df_from_directory(path, classification):
    rows = []
    row_names = []
    for file_name, email_body in email_body_generator(path):
        rows.append({'message': email_body, "category": classification})
        row_names.append(file_name)

    return pd.DataFrame(rows, index=row_names)


spam_emails = df_from_directory(spam_1_path, 1)
spam_emails = spam_emails._append(df_from_directory(spam_2_path, 1))
nonspam = df_from_directory(easy_nonspam_1_path, 0)
nonspam = nonspam._append(df_from_directory(easy_nonspam_2_path, 0))
# print(spam_emails.shape)
# print(nonspam.shape)

data = pd.concat([spam_emails, nonspam])
# print(data.shape)

# Checking if there is null values in my dataset.
# print(data["message"].isnull().sum())
# print((data["message"].str.len() == 0).sum())
# print(data["message"].isnull().values())
# print(len(data["message"]))

# Removing emails that has no messages.
# for i in range(len(data)):
#     if len(data["message"][i]) == 0:
#         data = data.drop(index=i)
#
# print(data.shape)

data = data[~(data["message"].str.len() == 0)]
# print(data.shape)

document_ids = range(0, len(data.index))
data["id"] = document_ids
data['file_name'] = data.index
data.set_index('id', inplace=True)
print(data.head())
