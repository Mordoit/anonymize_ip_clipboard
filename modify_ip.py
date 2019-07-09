#!/usr/bin/env python

__author__ = "Mordoit"
__version__ = "1.0.0"
__email__ = "mordoit@protonmail.com"

# Import
import re
import clipboard

input("Copy the text than you want to use\n\nPress Enter to continue...")

# Create variable from the clipboard
text = clipboard.paste()

# Get all IP in a list
ips = re.findall(r'[0-9]+(?:\.[0-9]+){3}', text)

# define the first number for the new address
newip = 11

for ip in ips:
    # Replace ip frome the list to the new ip
    text = text.replace(ip, str(newip) + "." + str(newip) + "." + str(newip) + "." + str(newip) )
    newip += 11


print("backup:\n\n" + clipboard.paste())

print("\n--------------------\nModified data is in your clipboard")
clipboard.copy(text)