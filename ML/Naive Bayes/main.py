ex_file = 'SpamData/01_Processing/practice_email.txt'

# Reading the file

stream = open(ex_file, "r")
is_body = False
# f = open("demofile.txt", "r")

# email_txt = stream.read()
# print(email_txt)
# print(stream.readlines())
lines = []
for text in stream:
    if is_body:
        lines.append(text)
    elif text == '\n':
        is_body = True

print(lines)
stream.close()
