# update_allow_list.py
import_file = 'allow_list.txt'
remove_list = ['192.168.1.2', '192.168.1.3']  # Example remove list

# Open and read the allow list file
with open(import_file, 'r') as file:
    ip_addresses = file.read()

# Convert the string into a list
ip_addresses = ip_addresses.split()

# Iterate through the remove list and remove the IP addresses
for element in remove_list:
    if element in ip_addresses:
        ip_addresses.remove(element)

# Update the file with the revised list of IP addresses
with open(import_file, 'w') as file:
    file.write('\n'.join(ip_addresses))
