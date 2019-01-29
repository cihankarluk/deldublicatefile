"""
This code is used for finding and removing duplication of files in a given
directory. But does not handle, content duplications. It is only check for
file names in that directory. After removing duplications, logs the removed
files paths.
"""

import os
import logging

file_list_name = []
logging.basicConfig(filename='test.log', format='%(asctime)s - %(message)s',
                    level=logging.INFO)


def duplicate_to_remove(user_path_input):
    """
    This function search for duplicated files in directory and removes
    the duplicate one.
    """
    logging.info("Started to search")
    if os.path.exists(user_path_input) and os.path.isdir(user_path_input):
        for root, _, files in os.walk(user_path_input):  # _ for dir
            for filename in files:
                if filename not in file_list_name:
                    file_list_name.append(filename)
                else:
                    file_path = os.path.join(root, filename)
                    print(file_path + "\nDo you want to delete this file? [y/n]")
                    user_check = input()
                    if user_check == 'y':
                        try:
                            os.remove(file_path)
                            logging.info("%s is removed from %s",
                                         filename, file_path)
                        except OSError:
                            logging.error("%s can not be removed from %s",
                                          filename, file_path)
                    else:
                        continue
    else:
        logging.getLogger().addHandler(logging.StreamHandler())
        logging.error("An error occurred given path.")


if __name__ == "__main__":
    logging.info("Program executed.")
    path_input = input("Please enter the path for search: ")
    duplicate_to_remove(os.path.expanduser(path_input))
