from db import mydb

cur = mydb.cursor()

cur.execute('''
    INSERT INTO todos(todo_name)
    VALUES
        ("Play Football"),
        ("Learn Python"), 
        ("Make a Breakfast"), 
        ("Read books");
''')    

mydb.commit()
