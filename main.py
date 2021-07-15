import app
import db_worker
import settings

# print(sys.argv)

if __name__ == "__main__":
	app.start()
	db_worker.add_information(101, "mar", "123", "customer")