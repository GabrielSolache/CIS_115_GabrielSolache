#create a dictionary with address information
#each key has a list of values (one for each person)
name_and_addresses = {
    'first_names': ['John', 'Jane', 'Jim'],
    'last_names': ['Doe', 'Smith', 'Beam'],
    'city': ['NY','LA','chicago'],
    'state': ['NY','CA','IL'],
    'zip_codes': ['10001','90001','60601'],
    'Phone_number': ['1234567890', '2345678901', '3456789012']
}
def print_dictionary(d):
    #print a title for clarity
    print("name and addresses dictionary")
    #print the entire  dictionary
    print(d)
#call the funtion to print the dictionary
print_dictionary(name_and_addresses)