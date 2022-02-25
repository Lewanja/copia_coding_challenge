import csv
import sqlite3
import requests

connect_to = sqlite3.connect("users.db")
conn = connect_to.cursor()


def create_user_table():
    conn.execute(
        '''
        CREATE TABLE IF NOT EXISTS USERS
        ([first_name] TEXT, [second_name] TEXT, [Age] INTEGER, [response] TEXT)
        '''
    )


def insert_record_into_user_table(first_name, last_name, age, response):
    conn.execute(" INSERT INTO users VALUES (?,?,?,?)", [first_name, last_name, age, response])


def read_all_users_from_db():
    query = "SELECT * from users;"
    conn.execute(query)
    return conn.fetchall()


def get_data_from_csv_file(file_path):
    with open(file_path, 'r') as users_file:
        csvreader = csv.reader(users_file)
        header = []
        header = next(csvreader)
        print(header)

        rows = []
        for row in csvreader:
            rows.append(row)
        return header, rows


def main():
    create_user_table()
    users_file = 'users.csv'
    user_headers, user_rows = get_data_from_csv_file(users_file)
    for row in user_rows:
        zip_object = zip(user_headers, row)
        dict_row = dict(zip_object)
        print(dict_row)
        response = requests.post("http://httpbin.org/post", data=dict_row)
        #print(response.text)
        insert_record_into_user_table(dict_row['first_name'], dict_row['second_name'], dict_row['Age'], response.text)

    connect_to.commit()
    users_from_db = read_all_users_from_db()
    connect_to.close()
    # read from db to confirm successful insert
    print(users_from_db)


if __name__ == "__main__":
    main()
