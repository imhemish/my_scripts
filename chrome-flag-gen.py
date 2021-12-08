#!/usr/bin/env python3

flags = ["password-store=basic"]

from os import environ
from os.path import expanduser as exp
from os.path import join
from os import remove

# Remove if chrome-flags.conf exists
try:
    remove(join(exp("~"), ".config", "chrome-flags.conf"))
except:
    pass # Pass if doesn't exist
'''
environment = environ["XDG_SESSION_TYPE"]
if environment == "wayland":
	flags.append("enable-features=UseOzonePlatform")
	flags.append("ozone-platform=wayland")
'''
with open(join(exp("~"), ".config", "chrome-flags.conf"), "a") as file:
	for item in flags:
		file.write("--"+item+"\n")
