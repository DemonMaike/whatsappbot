# <----------NOW DB.py NOT USED!!!!------------>

import sqlite3
# Create con and cur for job's be database  
#conn = sqlite3.connect('database.db')
#cur = conn.cursor()

# select name birthday man's 

def name(dt):
    '''This function return name birthday man's, need write a date'''
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    end = []
    result = [x for x in cur.execute('SELECT Name FROM Human WHERE date = "{}"'.format(dt))]
    for x in result:
        end.append(x[0])

    return ', '.join(end)





# create table
# cur.execute("""CREATE TABLE Human (Name text, date text)""")

# Write information of humans
# Human = [('Первый', '2, 13'), ('Второй', '2, 13'), ('Третий', '2, 13')]

# delete information
# cur.execute("DELETE FROM Human WHERE Date = '2 13'" )
# con.commit()

# Update data from database
#cur.execute('UPDATE Human SET date = "2, 15" WHERE date = "2, 13" ')
#conn.commit()