import pyfiglet
from colorama import init
from termcolor import colored
 
# use Colorama to make Termcolor work on Windows too
init()

valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")
msg = input("What is the message you would like to print? ")
color = input("Which color would be the message in? ")
if color not in valid_colors:
	color = "magenta"

ascii_art = pyfiglet.figlet_format(msg)
colored_ascii = colored(ascii_art, color)
print(colored_ascii)