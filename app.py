import sys
import settings


def start() -> None:
	# Checks login and password and prints greeting to the first parametr from the console
	list_of_args = sys.argv[1:]
	if list_of_args[0] == settings.administrator.get("login") and list_of_args[1] == settings.administrator.get("password"):
		print(f"Good evening, {sys.argv[1]}, nice to see you!")
	else:
		print("Invalid login or password")
