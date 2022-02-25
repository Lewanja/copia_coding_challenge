# USERS DATABASE

## Exercise

 *Write a program that will take the users.csv file attached as an argument and send post requests to the URL: <http://httpbin.org/post> for all users, with parameter first_name, second_name and age. The program should also persist all the records in the file to a Relational database table including the response from the URL.*

## Solution

Libraries used:
  
1. [Requests](https://pypi.org/project/requests/) `pip install requests`.
  
  This library is used when working with REST APIs(GET, POST, PUT DELETE) in python

2. Sqlite .

  This is an inbuilt python library to create, read, update and delete sqlite3 data using python

3. CSV.

  This is an inbuilt library is used to manipulate CSV files.

#### To run

`python users_urls_db.py`

#### Expected output

```sh
[('Lucy Kimani', 'Mary', 10, '{\n  "args": {}, \n  "data": "", \n  "files": {}, \n  "form": {\n    "Age": "10", \n    "first_name": "Lucy Kimani", \n    "second_name": "Mary"\n  }, \n  "headers": {\n    "Accept": "*/*", \n    "Accept-Encoding": "gzip, deflate", \n    "Content-Length": "46", \n    "Content-Type": "application/x-www-form-urlencoded", \n    "Host": "httpbin.org", \n    "User-Agent": "python-requests/2.27.1", \n    "X-Amzn-Trace-Id": "Root=1-6217f96b-69629c3c1d9884076a749e57"\n  }, \n  "json": null, \n  "origin": "105.163.0.201", \n  "url": "http://httpbin.org/post"\n}\n'), ('Catherine', 'Cate', 80, '{\n  "args": {}, \n  "data": "", \n  "files": {}, \n  "form": {\n    "Age": "80", \n    "first_name": "Catherine", \n    "second_name": "Cate"\n  }, \n  "headers": {\n    "Accept": "*/*", \n    "Accept-Encoding": "gzip, deflate", \n    "Content-Length": "44", \n    "Content-Type": "application/x-www-form-urlencoded", \n    "Host": "httpbin.org", \n    "User-Agent": "python-requests/2.27.1", \n    "X-Amzn-Trace-Id": "Root=1-6217f96c-52cbf17b04bce07f1653002c"\n  }, \n  "json": null, \n  "origin": "105.163.0.201", \n  "url": "http://httpbin.org/post"\n}\n'), ('Japheth', 'Doe', 45, '{\n  "args": {}, \n  "data": "", \n  "files": {}, \n  "form": 
{\n    "Age": "45", \n    "first_name": "Japheth", \n    "second_name": "Doe"\n  }, \n  "headers": {\n    "Accept": "*/*", \n    "Accept-Encoding": "gzip, deflate", \n    "Content-Length": "41", \n    "Content-Type": "application/x-www-form-urlencoded", \n    "Host": "httpbin.org", \n    "User-Agent": "python-requests/2.27.1", \n    "X-Amzn-Trace-Id": "Root=1-6217f96c-51acdf3473270269641ecf04"\n  }, \n  "json": null, \n  "origin": "105.163.0.201", \n  "url": "http://httpbin.org/post"\n}\n'), ('Peter', 'Van', 31, '{\n  "args": {}, \n  "data": "", \n  "files": {}, \n  "form": {\n    "Age": "31", \n    "first_name": "Peter", \n    "second_name": "Van"\n  }, \n  "headers": {\n    "Accept": "*/*", \n 
   "Accept-Encoding": "gzip, deflate", \n    "Content-Length": "39", \n    "Content-Type": "application/x-www-form-urlencoded", \n    "Host": "httpbin.org", \n    "User-Agent": "python-requests/2.27.1", \n    "X-Amzn-Trace-Id": "Root=1-6217f96d-37ba5ba375cb6e60527b589b"\n  }, \n  "json": null, \n  "origin": "105.163.0.201", \n  "url": "http://httpbin.org/post"\n}\n'), ('Benson', 'Ben', 50, '{\n  "args": {}, \n  "data": 
"", \n  "files": {}, \n  "form": {\n    "Age": "50", \n    "first_name": "Benson", \n    "second_name": "Ben"\n  }, \n  "headers": {\n    "Accept": "*/*", \n    "Accept-Encoding": "gzip, deflate", \n    "Content-Length": "40", \n    "Content-Type": "application/x-www-form-urlencoded", \n    "Host": "httpbin.org", \n    "User-Agent": "python-requests/2.27.1", \n    "X-Amzn-Trace-Id": "Root=1-6217f96d-64a122a84acd7e337b09dfc1"\n  }, \n  "json": null, \n  "origin": "105.163.0.201", \n  "url": "http://httpbin.org/post"\n}\n'), ('Dennis', 'Johnson', 67, '{\n  "args": {}, \n  "data": "", \n  "files": {}, \n  "form": {\n    "Age": "67", \n    "first_name": "Dennis", \n    "second_name": "Johnson"\n  }, 
\n  "headers": {\n    "Accept": "*/*", \n    "Accept-Encoding": "gzip, deflate", \n    "Content-Length": "44", \n    "Content-Type": "application/x-www-form-urlencoded", \n    "Host": "httpbin.org", \n    "User-Agent": "python-requests/2.27.1", \n    "X-Amzn-Trace-Id": "Root=1-6217f96e-6a3396db65ad79cb184d37c6"\n  }, \n  "json": null, \n  "origin": "105.163.0.201", \n  "url": "http://httpbin.org/post"\n}\n'), ('Dominic', 'Denis', 33, '{\n  "args": {}, \n  "data": "", \n  "files": {}, \n  "form": {\n    "Age": "33", \n    "first_name": "Dominic", \n    "second_name": "Denis"\n  }, \n  "headers": {\n    "Accept": "*/*", \n    "Accept-Encoding": "gzip, deflate", \n    "Content-Length": "43", \n    "Content-Type": "application/x-www-form-urlencoded", \n    "Host": "httpbin.org", \n    "User-Agent": "python-requests/2.27.1", \n    "X-Amzn-Trace-Id": "Root=1-6217f96e-2a1743f254043c1532cdd3c3"\n  }, \n  "json": null, \n  "origin": "105.163.0.201", \n  "url": "http://httpbin.org/post"\n}\n'), ('Susan', 'Willams', 48, '{\n  "args": {}, \n  "data": "", \n  "files": {}, \n  "form": {\n    "Age": "48", \n    "first_name": 
"Susan", \n    "second_name": "Willams"\n  }, \n  "headers": {\n    "Accept": "*/*", \n    "Accept-Encoding": "gzip, deflate", \n    "Content-Length": "43", \n    "Content-Type": "application/x-www-form-urlencoded", \n    "Host": "httpbin.org", \n    "User-Agent": "python-requests/2.27.1", \n    "X-Amzn-Trace-Id": "Root=1-6217f96f-690483ad5e14d9f758992065"\n  }, \n  "json": null, \n  "origin": "105.163.0.201", \n  "url": "http://httpbin.org/post"\n}\n'), ('Veronica', 'Walen', 54, '{\n  "args": {}, \n  "data": "", \n  "files": {}, \n  "form": {\n    "Age": "54", \n    "first_name": "Veronica", \n    "second_name": "Walen"\n  }, \n  "headers": {\n    "Accept": "*/*", \n    "Accept-Encoding": "gzip, deflate", \n    "Content-Length": "44", \n    "Content-Type": "application/x-www-form-urlencoded", \n    "Host": "httpbin.org", \n    "User-Agent": "python-requests/2.27.1", \n    "X-Amzn-Trace-Id": "Root=1-6217f96f-73419bf00c40116a0ea0753a"\n  }, \n  "json": null, \n  "origin": "105.163.0.201", \n  "url": "http://httpbin.org/post"\n}\n'), ('Lucy Kimani', 'Mary', 10, '{\n  "args": {}, \n  "data": "", \n  "files": {}, \n  "form": {\n    "Age": "10", \n    "first_name": "Lucy Kimani", \n    "second_name": "Mary"\n  }, \n  "headers": {\n    "Accept": "*/*", \n    "Accept-Encoding": "gzip, deflate", \n    "Content-Length": "46", \n    "Content-Type": "application/x-www-form-urlencoded", \n    "Host": "httpbin.org", \n    "User-Agent": "python-requests/2.27.1", \n    "X-Amzn-Trace-Id": "Root=1-6217f977-7ae89c864677b9e97ca539fa"\n  }, \n  
"json": null, \n  "origin": "105.163.0.201", \n  "url": "http://httpbin.org/post"\n}\n'), ('Catherine', 'Cate', 80, '{\n  "args": {}, \n  "data": "", \n  "files": {}, \n  "form": {\n    "Age": "80", \n    "first_name": "Catherine", \n    "second_name": "Cate"\n  }, \n  "headers": {\n    "Accept": "*/*", \n    "Accept-Encoding": "gzip, deflate", \n    "Content-Length": "44", \n    "Content-Type": "application/x-www-form-urlencoded", \n    "Host": "httpbin.org", \n    "User-Agent": "python-requests/2.27.1", \n    "X-Amzn-Trace-Id": "Root=1-6217f978-122cc0f452b0f4c118f3de62"\n  }, \n  "json": null, \n  "origin": "105.163.0.201", \n  "url": "http://httpbin.org/post"\n}\n'), ('Japheth', 'Doe', 45, '{\n  "args": {}, \n  "data": "", \n  "files": {}, \n  "form": {\n    "Age": "45", \n    "first_name": "Japheth", \n    "second_name": "Doe"\n  
}, \n  "headers": {\n    "Accept": "*/*", \n    "Accept-Encoding": "gzip, deflate", \n    "Content-Length": "41", \n    "Content-Type": "application/x-www-form-urlencoded", \n    "Host": "httpbin.org", \n    "User-Agent": "python-requests/2.27.1", \n    "X-Amzn-Trace-Id": "Root=1-6217f978-6d92f3ed4cb4fb8479a5a400"\n  }, \n  "json": null, \n  "origin": "105.163.0.201", \n  "url": "http://httpbin.org/post"\n}\n'), ('Peter', 'Van', 31, '{\n  "args": {}, \n  "data": "", \n  "files": {}, \n  "form": {\n    "Age": "31", \n    "first_name": "Peter", \n    "second_name": "Van"\n  }, \n  "headers": {\n    "Accept": "*/*", \n    "Accept-Encoding": "gzip, deflate", \n    "Content-Length": "39", \n    "Content-Type": "application/x-www-form-urlencoded", \n    "Host": "httpbin.org", \n    "User-Agent": "python-requests/2.27.1", \n    "X-Amzn-Trace-Id": "Root=1-6217f979-09cf0fd72c4eb37a6bddc270"\n  }, \n  "json": null, \n  "origin": "105.163.0.201", \n  "url": "http://httpbin.org/post"\n}\n'), ('Benson', 'Ben', 50, '{\n  "args": {}, \n  "data": "", \n  "files": {}, \n  "form": {\n    "Age": "50", \n    "first_name": "Benson", \n    "second_name": "Ben"\n  }, \n  "headers": {\n    "Accept": "*/*", \n    "Accept-Encoding": "gzip, deflate", \n    "Content-Length": "40", \n    "Content-Type": "application/x-www-form-urlencoded", \n    "Host": "httpbin.org", \n    "User-Agent": "python-requests/2.27.1", \n    "X-Amzn-Trace-Id": "Root=1-6217f979-18087cfa75ec4149583f7476"\n  }, \n  "json": null, \n  "origin": "105.163.0.201", \n  "url": "http://httpbin.org/post"\n}\n'), ('Dennis', 'Johnson', 67, '{\n  "args": {}, \n  "data": "", \n  "files": {}, \n  "form": {\n    "Age": "67", \n    "first_name": "Dennis", \n    "second_name": "Johnson"\n  }, \n  "headers": {\n    "Accept": "*/*", \n    "Accept-Encoding": "gzip, deflate", 
\n    "Content-Length": "44", \n    "Content-Type": "application/x-www-form-urlencoded", \n    "Host": "httpbin.org", \n    "User-Agent": "python-requests/2.27.1", \n    "X-Amzn-Trace-Id": "Root=1-6217f97a-1be2bff42a8d8e6e2da8a0a9"\n  }, \n  "json": null, \n  "origin": "105.163.0.201", \n  "url": "http://httpbin.org/post"\n}\n'), ('Dominic', 'Denis', 33, '{\n  "args": {}, \n  "data": "", \n  "files": {}, \n  "form": {\n    "Age": "33", \n    "first_name": "Dominic", \n    "second_name": "Denis"\n  }, \n  "headers": {\n    "Accept": "*/*", \n    "Accept-Encoding": "gzip, deflate", \n    "Content-Length": "43", \n    "Content-Type": "application/x-www-form-urlencoded", \n    "Host": "httpbin.org", 
\n    "User-Agent": "python-requests/2.27.1", \n    "X-Amzn-Trace-Id": "Root=1-6217f97a-11a277be43ed20904bf512a6"\n  }, \n  "json": null, \n 
 "origin": "105.163.0.201", \n  "url": "http://httpbin.org/post"\n}\n'), ('Susan', 'Willams', 48, '{\n  "args": {}, \n  "data": "", \n  "files": {}, \n  "form": {\n    "Age": "48", \n    "first_name": "Susan", \n    "second_name": "Willams"\n  }, \n  "headers": {\n    "Accept": "*/*", \n    "Accept-Encoding": "gzip, deflate", \n    "Content-Length": "43", \n    "Content-Type": "application/x-www-form-urlencoded", \n    
"Host": "httpbin.org", \n    "User-Agent": "python-requests/2.27.1", \n    "X-Amzn-Trace-Id": "Root=1-6217f97b-01f2f34f57b5b04a7c8a0d58"\n  }, \n  "json": null, \n  "origin": "105.163.0.201", \n  "url": "http://httpbin.org/post"\n}\n'), ('Veronica', 'Walen', 54, '{\n  "args": {}, \n  "data": "", \n  "files": {}, \n  "form": {\n    "Age": "54", \n    "first_name": "Veronica", \n    "second_name": "Walen"\n  }, \n  "headers": {\n    "Accept": "*/*", \n    "Accept-Encoding": "gzip, deflate", \n    "Content-Length": "44", \n    "Content-Type": "application/x-www-form-urlencoded", \n    "Host": "httpbin.org", \n    "User-Agent": "python-requests/2.27.1", \n    "X-Amzn-Trace-Id": "Root=1-6217f97b-6303e3cf3c15560a23ecd09c"\n  }, \n  "json": null, \n  "origin": "105.163.0.201", \n  "url": "http://httpbin.org/post"\n}\n')]
```


### Procedure

Steps followed while carrying out the task:

##### Reading csv file

To access an external file, the `with open('filename', 'r') as f:`  the 'r' field shows that read operation will bbe performed. To write into the file, substitute 'r' with 'w'. The `csv.reader()` iterates over items in a csv file and returns a string each time it is `next()`. The header values of the csv file are stored inside header array while the rows are stored inside the rows array.

```python
def get_data_from_csv_file(file_path):
    with open(file_path, 'r') as users_file:
        csvreader = csv.reader(users_file)
        header = []
        header = next(csvreader)
        print(header)

        rows = []
        for row in csvreader:
            rows.append(row)
        return header, 
```

The header data and row data are paired using `zip()` function and then converted into dictionary `dict()`. The output is sent to [response](http://httpbin.org/post) url.

```python
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
```

##### Creating a relational database

To create a database and connect to it, `connect_to = sqlite3.connect("users.db")` is used where the name of the database is passed inside the parantheses. In this case, **'users.db'** is the name of the database.
Once a connection has been established, a Cursor object is created and  `execute()`  is called to perform SQL commands. To create a table, the CREATE command is used and to insert values into it, the INSERT command is used.

```python
connect_to = sqlite3.connect("users.db")
conn = connect_to.cursor()


def create_user_table():
  conn.execute(
    '''
    CREATE TABLE IF NOT EXISTS USERS
    ([first_name] TEXT, [second_name] TEXT, [Age] INTEGER, [response] TEXT)
    '''
  )

  connect_to.commit()
  users_from_db = read_all_users_from_db()
  connect_to.close()
  # read from db to confirm successful insert
  print(users_from_db)
```

The `.commit()` helps visualize what is in the database while `.close()` closes the database connection. When you close the database without `commit()`, changes made are lost.

- Adding the CSV values into the database.

```python
def insert_record_into_user_table(first_name, last_name, age, response):
    conn.execute(" INSERT INTO users VALUES (?,?,?,?)", [first_name, last_name, age, response])
```

To retrieve data after executing a SELECT statement, call `fetchall()` to get a list of the matching rows.

```python
def read_all_users_from_db():
    query = "SELECT * from users;"
    conn.execute(query)
    return conn.fetchall()
```

