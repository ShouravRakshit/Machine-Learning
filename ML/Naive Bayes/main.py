# Formulate Question -> Gather Data from a Website -> Clean Data

from os import walk
from os.path import join
import matplotlib.pyplot as plt
import nltk
import string
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup
import pandas as pd

ex_file = 'SpamData/01_Processing/practice_email.txt'
spam_1_path = 'SpamData/01_Processing/spam_assassin_corpus/spam_1'
spam_2_path = 'SpamData/01_Processing/spam_assassin_corpus/spam_2'
easy_nonspam_1_path = 'SpamData/01_Processing/spam_assassin_corpus/easy_ham_1'
easy_nonspam_2_path = 'SpamData/01_Processing/spam_assassin_corpus/easy_ham_2'
json_path = 'SpamData/01_Processing/email-text-data.json'


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
def clean_msg(msg):

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
# print(data.head())

spam_num = data["category"].value_counts()[1]
nonspam_num = data["category"].value_counts()[0]
# Creating pie chart with spam and non spam email data.
category_names = ["Spam", "Legit Email"]
sizes = [spam_num, nonspam_num]
plt.figure(figsize=(8, 6), dpi=100)
plt.pie(sizes, labels=category_names, textprops={'fontsize': 15}, autopct='%1.2f%%')
# nltk.download('punkt')
# nltk.download('stopwords')

# Filtering some Stop words
# Word Stems and Stemming
# Removing punctuations
stop_words = stopwords.words()
msg = "All work and no play makes Jack a dull boy. To be or not be".translate(str.maketrans('', '', string.punctuation))

words = word_tokenize(msg.lower())
stemmer = PorterStemmer()
filtered_words = []

for letter in range(len(words)):
    if words[letter] not in stop_words:
        stemmed_word = stemmer.stem(words[letter])
        filtered_words.append(stemmed_word)
print(filtered_words)

index = data.at[200, "message"]
soup = BeautifulSoup(index, 'html.parser')
# print(soup.prettify())
print(soup.get_text())


# print(index)
# plt.show()
