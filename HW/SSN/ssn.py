# Search for the SSN using for loop
def ssn_search(text):
    ssn_list = []
    for index in range(11, len(text)):
        ssn_format = text[(index-11) : (index)]
        if ((ssn_format[3:4] == "-") and (ssn_format[6:7] == "-")):
            if ((ssn_format[0:3].isdigit()) and (ssn_format[4:6].isdigit()) and (ssn_format[7:10].isdigit())):
                ssn_list.append(ssn_format)
    return ssn_list

# Open file and read its content
def read_txt(directory):
    with open(directory) as file:
        return file.read()

# Open and append ssn into file
def add_txt(directory, text):
    with open(directory, "a") as file:
        file.write(text + "\n")

# Main
def main():
    text = read_txt('info.txt')
    ssn_list = ssn_search(text)
    for ssn in ssn_list:
        add_txt('ssn.txt', ssn)

# Run
main()