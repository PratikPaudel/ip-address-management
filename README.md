# IP Address Management

This project contains a Python script to update an allow list of IP addresses by removing IPs specified in a remove list.

## Project Description

At my organization, access to restricted content is controlled with an allow list of IP addresses. The `allow_list.txt` file identifies these IP addresses. A separate remove list identifies IP addresses that should no longer have access to this content. I created an algorithm to automate updating the `allow_list.txt` file and remove these IP addresses that should no longer have access.

## Algorithm Steps

1. **Open the allow list file**:
    - The `allow_list.txt` file is opened in read mode to read the IP addresses stored in it.

2. **Read the file contents**:
    - The contents of the file are read into a string format.

3. **Convert the string into a list**:
    - The string of IP addresses is converted into a list using the `.split()` method.

4. **Iterate through the remove list**:
    - A `for` loop is used to iterate through the IP addresses in the remove list.

5. **Remove IP addresses that are on the remove list**:
    - Each IP address found in the remove list is removed from the allow list using the `.remove()` method.

6. **Update the file with the revised list of IP addresses**:
    - The updated list of IP addresses is converted back into a string and written to the `allow_list.txt` file.

## How to Use

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/ip-address-management.git
    cd ip-address-management
    ```

2. Update the `remove_list` in `update_allow_list.py` with the IPs you want to remove.

3. Run the script:
    ```sh
    python update_allow_list.py
    ```

## License

This project is licensed under the MIT License.
