import sqlite3 as sl
import json
import time

con = sl.connect('polyclinic.db')


# Client_base
with con:
    con.execute("""
        CREATE TABLE IF NOT EXISTS Client_base (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            birthday DATE,
            telephone BIGINT,
            notes TEXT,
            UNIQUE(telephone)
        );
    """)

sql_insert = "INSERT INTO CLIENT_BASE (name, birthday, telephone, notes) values(?, ?, ?, ?)"

test = [("Иванов Пётр", '26.07.1967', '+375 666 66 66', 'bad client'),
       ("Озерова Анастасия", '24.04.2001', '+375 456 66 6623', 'good client'),
       ("Киселёв Александр", '12.09.1982', '+375 324 66 662', 'crazy and lazy client'),
       ("Норманн Давид", '26.07.2000', '+375 666 78 66', 'normal client'),
       ("Jason Statham", '26.07.1967', '+375 56 66 55', 'sometimes crazy client'),
       ("Jason Born", '26.07.1967', '+375 455 66 66', 'crazy client')]
try:
    with con:
        con.executemany(sql_insert, test)



    def json_notes():
        client = con.execute("SELECT id, notes FROM Client_base")

        dt1 = time.time()

        x = client.fetchall()
        for val in x:
            with open(f"client_id_{val[0]}.json", 'w', encoding='utf-8') as f:
                to_json = {str(dt1): val[1]}
                json.dump(to_json, f, ensure_ascii=False, indent=2)
    json_notes()


    # добавление примечаний
    # def add_notes():
    #     change_notes = int(input("Введите id: "))
    #     new_notes = input("Введите примечание: ")
    #
    #     dt2 = time.time()
    #
    #     notes = {str(dt2): new_notes}
    #
    #     with open(f"client_id_{change_notes}.json", encoding='utf-8') as f:
    #         data = json.load(f)
    #         print(data)
    #         for k,v in data.items():
    #             notes[k] = v
    #             print(notes)
    #
    #
    #     with open(f"client_id_{change_notes}.json", 'w', encoding='utf-8') as file:
    #         json.dump(notes, file, ensure_ascii=False, indent=2)
    #
    # add_notes()


    # with con:
    #     data = con.execute("SELECT * FROM Client_base")
    #     print(data.fetchall())








    # Employees
    with con:
        con.execute("""
            CREATE TABLE IF NOT EXISTS Employees (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                birthday DATE,
                telephone BIGINT,
                job_title INTEGER,
                UNIQUE(telephone), 
                FOREIGN KEY (job_title) REFERENCES Job_title (job_id)
            );
        """)

    sql_insert = "INSERT INTO Employees (name, birthday, telephone, job_title) values(?, ?, ?, ?)"

    test2 = [("Jason Statham", '26.07.1967', '+365 777 77 77', 2),
           ("Герчик Александр", '23.12.1996', '+365 123 43 772', 1),
           ("Догоняеев Петр", '14.09.1990', '+365 444 34 77', 3),
           ("Давидович Дарья", '20.01.2000', '+365 123 77 77', 4),
           ("Соколов Максим", '16.05.1967', '+365 446 78 77', 3)]
    try:
        with con:
            con.executemany(sql_insert, test2)




        # with con:
        #     data2 = con.execute("SELECT * FROM Employees")
        #     print(data2.fetchall())





        # Job_title
        with con:
            con.execute("""
                CREATE TABLE IF NOT EXISTS Job_title (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    salary INTEGER,
                    cabinet INTEGER
                );
            """)

        sql_insert = "INSERT INTO Job_title (name, salary, cabinet) values(?, ?, ?)"

        test3 = [('хирург', 1000, 122),
                 ('стоматолог', 2500, 234),
                 ('окулист', 1250, 311),
                 ('лор', 900, 410),
                 ('стоматолог', 3000, 216)]


        with con:
            con.executemany(sql_insert, test3)



        # with con:
        #     data3 = con.execute("SELECT * FROM Job_title")
        #     print(data3.fetchall())








        # Services
        with con:
            con.execute("""
                CREATE TABLE IF NOT EXISTS Services (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    service_name TEXT,
                    job_title INTEGER,
                    price INTEGER,
                    start_time DATETIME,
                    FOREIGN KEY (job_title) REFERENCES Job_title (job_id)
                );
            """)

        sql_insert = "INSERT INTO Services (service_name, job_title, price, start_time) values(?, ?, ?, ?)"

        test4 = [('чистка зубов', 1, 1000, '2020-01-08T13:00:00.000Z'),
                 ('проверка зрения', 3, 200, '2020-12-08T11:00:00.000Z'),
                 ('анализ крови', 4, 300, '2022-11-08T16:00:00.000Z'),
                 ('измерение давления', 2, 250, '2022-09-08T14:00:00.000Z'),
                 ('проверка слуха', 1, 700, '2022-07-08T17:00:00.000Z'),
                 ('консультация', 2, 500, '2022-07-08T17:00:00.000Z'),
                 ('пересадка почки', 1, 7400, '2022-07-08T17:00:00.000Z'),
                 ('ДНК тест', 5, 300, '2022-07-08T17:00:00.000Z')]

        with con:
            con.executemany(sql_insert, test4)



        # with con:
        #     data4 = con.execute("SELECT * FROM Services")
        #     print(data4.fetchall())






        # Orders

        with con:
            con.execute("""
                CREATE TABLE IF NOT EXISTS Orders (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    employee_id INT,
                    service_id INT,
                    client_id INT,
                    start_time DATETIME,
                    end_time DATETIME,
                    FOREIGN KEY (client_id) REFERENCES Client_base (client_id),
                    FOREIGN KEY (service_id) REFERENCES Services (service_id),
                    FOREIGN KEY (employee_id) REFERENCES Employees (employee_id)
                );
            """)

        sql_insert = "INSERT INTO Orders (client_id, service_id, employee_id, start_time, end_time) values(?, ?, ?, ?, ?)"

        test5 = [(1, 2322, 1, '2020-01-08T13:00:00.000Z', '2020-01-08T14:00:00.000Z'),
                 (2, 1157, 2, '2020-09-08T10:00:00.000Z', '2020-09-08T11:00:00.000Z'),
                 (3, 133, 3, '2022-06-08T10:00:00.000Z', '2022-06-08T11:00:00.000Z'),
                 (4, 115347, 4, '2022-03-08T10:00:00.000Z', '2022-03-08T11:00:00.000Z'),
                 (5, 234, 5, '2022-04-08T10:00:00.000Z', '2022-04-08T11:00:00.000Z'),
                 (6, 1155357, 6, '2022-05-08T10:00:00.000Z', '2022-05-08T11:00:00.000Z')]

        with con:
            con.executemany(sql_insert, test5)

        # with con:
        #     data5 = con.execute("SELECT * FROM Orders")
        #     print(data5.fetchall())


    except:
        print("Такой номер уже занят")
except:
    print("Такой номер уже занят")

con.execute