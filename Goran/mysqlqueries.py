# create table
sql_create_example = "CREATE DATABASE IF NOT EXISTS thermodb"

sql_create_thermodb_tables = '''
    CREATE TABLE IF NOT EXISTS sensors2 (
    id int(11) AUTO_INCREMENT,
    sernum varchar(32) NOT NULL,
    name varchar(255) NOT NULL,
    active tinyint(4) NOT NULL,
    PRIMARY KEY (id)
    )
    
    CREATE TABLE IF NOT EXISTS templog2 (
    id int(11) AUTO_INCREMENT,
    sensor_id int(11) NOT NULL,
    date date NOT NULL,
    time time NOT NULL,
    temperature double NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (sensor_id) REFERENCES sensors2(id)
    )
'''

# insert new row into the table - example
sql_insert = "INSERT INTO sensors (sernum, name, active) VALUES ('28-0000034d2631', 'Remote sensor', 1)"
    
# select everything from the table
sql_select_all = "SELECT * FROM sensors"

# selsect conditionaly
sql_select = "SELECT * FROM sensors WHERE active != 0"

sql = "SELECT * FROM EMPLOYEE WHERE INCOME > '%d'" % (1000)

# update existing record/row
sql = "UPDATE sensors SET active = 0 WHERE sernum = '28-0000034d2631'"

# kind of works, although date/time columns are doubled
sql = '''select * from 
(select date, time, temperature as remtemp from templog where sensor_id = 4) as remote
join
(select date, time, temperature as toptemp from templog where sensor_id = 3) as top
on remote.date = top.date and remote.time = top.time;'''

# this one seems to work fro two sensors
# it's not perfect and wonder how it's going to do with more sensors???
sql = '''select remote.date, remote.time, remote.remtemp, top.toptemp from
(select date, time, temperature as remtemp from templog where sensor_id = 4) as remote,
(select date, time, temperature as toptemp from templog where sensor_id = 3) as top
where remote.date = top.date and remote.time = top.time;'''
