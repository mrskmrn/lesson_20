import csv
import settings

columns = [
	"id",
	"login",
	"password",
	"role",
]

def get_data() -> list:
	with open(settings.file_name, "r") as f:
		data = list(csv.reader(f))
		print(data)
	return data[1:]

def get_id_next() -> int:
	return int(get_data()[-2][0]) + 1 if get_data() else 100

def add_information(id_const: int, login_inp: str, password_inp: str, role_inp: str):
	with open(settings.file_name, "a") as f:
		csv_obj = csv.writer(f)
		csv_obj.writerow([get_id_next(), login_inp, password_inp, role_inp])


# f = open("db.csv", "w")

# csv_obj = csv.writer(f)
# csv_obj.writerow(columns)

# f.close()
