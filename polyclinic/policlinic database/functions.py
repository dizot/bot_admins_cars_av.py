import polyclinic_db
import sqlite3 as sl
import json
import time

con = sl.connect('polyclinic.db')

# 1 - функция принимает в качестве аргумента название таблицы, возвращает ее полностью

# def all_table():
#     # Client_base
#     table_name = input("Введите название таблицы: ")
#     try:
#         with con:
#             client = con.execute(f"SELECT * FROM {table_name}")
#             print(client.fetchall())
#     except:
#         print("Название таблицы введено не верно")
#
# all_table()



# # Запись
# # 2 - Добавление доктора - функция принимает в качестве аргумента кортеж значений и имя таблицы,
# # возвращает TRUE при успехе или ошибку при ошибке

# def add_docktor():
#
#     table_name = input("Введите название таблицы: ")
#
#     if table_name == 'Employees':
#
#         doc_name = input("Введите ФИО: ")
#         doc_birthday = input("Введите дату рождения: ")
#         doc_telephone = input("Введите номер телефона: ")
#         doc_job_title = input("Введите должность: ")
#         doc_salary = input("Введите зарплату: ")
#         doc_cabinet = input("Введите номер кабинета: ")
#
#         try:
#             for_job_title = [(doc_job_title, doc_salary, doc_cabinet)]
#             sql_insert1 = """INSERT INTO Job_title (name, salary, cabinet) values(?, ?, ?)"""
#             with con:
#                 con.executemany(sql_insert1, for_job_title)
#                 doc_id = con.execute(f"SELECT id FROM Job_title")
#                 for id in doc_id.fetchall():
#                     job_id = id[0]
#
#             # Employees
#             for_employees = [(doc_name, doc_birthday, doc_telephone, job_id)]
#
#             sql_insert2 = f"""INSERT INTO {table_name} (name, birthday, telephone, job_title) values(?, ?, ?, ?)"""
#             with con:
#                 con.executemany(sql_insert2, for_employees)
#                 print("работник успешно добавлен")
#         except:
#             print('ошибка')
#     else:
#         pass
#
# add_docktor()





# # Изменение
# # 5 - функция принимает в качестве аргумента название таблицы, id изменяемого объекта и кортеж словарей или один общий словарь для изменения

# def change():
#     dict_change = {}
#
#     # Employees
#     # name
#     table_name2 = input("Введите название таблицы: ")
#     change_id = input("Введите id изменяемого объекта: ")
#
#     change_key = input("Введите название изменяемого столбца: ")
#     change_value = input("Введите значение изменяемого столбца: ")
#     dict_change[change_key] = change_value
#
#     for k ,v in dict_change.items():
#
#         sql_change = f"""UPDATE {table_name2} SET {k} = '{v}'
#         WHERE id = {change_id}"""
#
#         try:
#             with con:
#                 con.execute(sql_change)
#                 print("Объект успешно изменён")
#         except:
#             print('Ошибка ввода данных')
#
# change()





# # 6 - функция возвращающая 3 словаря id:name для таблиц Доктор, Услуга, Клиент

# dict_employees = {}
# dict_service = {}
# dict_client = {}
#
# def dictionary():
#
#
#     with con:
#         employees = con.execute(f"SELECT id, name FROM Employees")
#
#         for k, v in employees.fetchall():
#             dict_employees[k] = v
#         # print(dict_employees)
#
#     with con:
#         services = con.execute(f"SELECT id, service_name FROM Services")
#
#         for k, v in services.fetchall():
#             dict_service[k] = v
#         # print(dict_service)
#
#
#     with con:
#         client = con.execute(f"SELECT id, name FROM Client_base")
#
#         for k, v in client.fetchall():
#             dict_client[k] = v
#         # print(dict_client)
#
# dictionary()





# # 7 - функция принимает в качестве значений кортеж из id в таком порядке (доктор, услуга, клиент) , производит запись, возвращает TRUE при успехе или ошибку при ошибке

# def order():
#
#     new_order = [(2, 4, 4)]
#     with con:
#         sql_order = """INSERT INTO Orders (employee_id, service_id, client_id) values(?, ?, ?)"""
#
#     try:
#         with con:
#             con.executemany(sql_order, new_order)
#             print("запись успешно добавлена")
#     except:
#         print('ошибка')
#
#
# order()





# 8 - функция помошник(опц) принимает в качестве аргумента доктора - возвращает все свойственные ему услуги

# def ser_doctor():
#     # Jason Statham
#     # Герчик Александр
#     doc_name = input("Введите имя доктора: ")
#     if doc_name not in dict_employees.values():
#         print("Такого доктора нет")
#
#     with con:
#         service = con.execute(f"""SELECT service_name FROM Services WHERE job_title = (SELECT id FROM Employees WHERE name = '{doc_name}')""")
#         for k in service.fetchall():
#             print(k[0])
#
# ser_doctor()


# удаление записей
# def delete():
#
#     # Client_base
#     del_from = input("Введите название таблицы: ")
#     del_from2 = input("Введите название столбца: ")
#     del_what = input("Введите название удаляемого объекта: ")
#
#     try:
#         with con:
#             con.execute(f"""DELETE FROM {del_from} WHERE {del_from2} = {del_what}""")
#             print("Запись удалена")
#     except:
#         print("Ошибка удаления")
#
# delete()
