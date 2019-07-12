#!/usr/bin/env python

__author__ = "Mordoit"
__version__ = "1.1.0"
__email__ = "mordoit@protonmail.com"

# Import
import re
import pyperclip

input("Copy the text than you want to use\n\nPress Enter to continue...")

# Create variable from the pyperclip
text = pyperclip.paste()

# Get all IP in a list
ips = re.findall(r'[0-9]+(?:\.[0-9]+){3}', text)

for ip in ips:
    new_ip += 11
    # Replace ip frome the list to the new ip
    text = text.replace(ip, str(new_ip) + "." + str(new_ip) +
                        "." + str(new_ip) + "." + str(new_ip))


print("backup:\n\n" + pyperclip.paste())

print("\n--------------------\nModified data is in your pyperclip")
pyperclip.copy(text)
