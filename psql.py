import psycopg2

con=psycopg2.connect('dbname=job_advertisement user=postgres host=localhost port=5432 password=Murad2004')

cur=con.cursor()

query="""
CREATE TABLE jobs(
    id SERIAL PRIMARY KEY,
    title VARCHAR(30),
    gain INT,
    expiration_date DATE,
    lang  BOOLEAN,
    city VARCHAR(20)
)
"""

info_list = [
    # basliq, sirket, maas, bitme tarixi, xarici dil telebi
    ('iOS developer', 'A2Z Technologies', 3500, '2022-07-18', True),
    ('Tender uzre mutexessis', 'A2Z Technologies', 1500, '2022-06-11', False),
    ('Melumat bazasi uzre inzibatci', 'ABB ASC', 1500, '2022-07-12', True),
    ('Database Administrator', 'A2Z Technologies', 2500, '2022-07-14', True),
    ('Front-End Developer', 'AzeriMed QSC', 1500, '2022-07-23', False),
    ('Proqram teminatinin testlesdirilmesi uzre muhendis',
     'ABB ASC', 1500, '2022-08-10', False),
    ('Back-end uzre proqramci', 'ABB ASC', 4100, '2022-07-11', True),
    ('Biznes analitika uzre Bas mutexessis ', 'ABB ASC', 2200, '2022-07-03', True),
    ('Android proqramci', 'ABB ASC', 1300, '2022-07-22', True),
    ('Front-end uzre proqramci', 'ABB ASC', 3200, '2022-07-06', True),
    ('Full stack PHP proqramci', 'AzeriMed QSC', 2400, '2022-07-17', False),
    ('Avtomatlasdirilmis emeliyyat sistemi uzre proqramci',
     'ABB ASC', 2700, '2022-07-15', True),
    ('Proqram teminati uzre muhendis', 'Kontakt Home', 2700, '2022-07-13', False),
    ('Huquqsunas', 'Kontakt Home', 1500, '2022-07-03', False),
    ('catdirilma xidmetleri uzre fehle', 'Kontakt Home', 500, '2022-07-15', True),
    ('PHP developer', 'ARIS', 1500, '2022-07-11', True),
    ('Mehsul uzre menecer', 'Kontakt Home', 2800, '2022-07-05', True),
    ('Proqram teminati uzre aparici muhendis',
     'Kontakt Home', 2500, '2022-07-02', False),
    ('IT senedlesmesi uzrə mutexessis', 'Azericard', 1500, '2022-07-25', True),
    ('Information Security Specialist', 'DEFSCOPE LLC', 2500, '2022-07-03', False),
    ('IT Helpdesk', 'Azericard', 1500, '2022-07-30', True),
    ('Cybersecurity Business Development Internship',
     'DEFSCOPE LLC', 2900, '2022-07-19', False),
    ('Vue.js developer', 'ARIS', 1500, '2022-07-29', True),
]


def show(cursor):
    cur.execute(query)
    length = 20
    print(*[desc[0].ljust(20) for desc in cursor.description], sep='')
    print('-'*140)
    result = cur.fetchall()
    for row in result:
        for col in row:
            print(str(col).ljust(length)[:17], end='')
        print()

query='ALTER TABLE jobs DROP COLUMN city'

query='ALTER TABLE jobs RENAME COLUMN gain TO salary'
query='ALTER TABLE jobs ADD COLUMN company VARCHAR(30)'

query="""INSERT INTO jobs(title,company,salary,expiration_date,lang) VALUES(%s,%s,%s,%s,%s)
"""
for i in info_list:
    cur.execute(query,(i[0],i[1],i[2],i[3],i[4]))


query="SELECT * FROM jobs WHERE company='ABB ASC'"

query="SELECT * FROM jobs WHERE company='ABB ASC' and salary<2000"

query="SELECT * FROM jobs WHERE company='Kontakt Home' and expiration_date<'2022-07-20' "
query="SELECT * FROM jobs WHERE lang='false' and salary>2500"
query="SELECT * FROM jobs WHERE title LIKE '%proqramci' "
query="SELECT * FROM jobs WHERE NOT title LIKE '%end%' "

query="SELECT * FROM jobs WHERE title LIKE 'IT%' "
query="SELECT * FROM jobs WHERE lang='True' ORDER BY salary DESC "
query="SELECT * FROM jobs WHERE salary=(SELECT MAX(salary) FROM jobs) "

query="SELECT * FROM jobs WHERE expiration_date>'2022-07-20' ORDER BY expiration_date OFFSET 1 LIMIT 3   "

# query="SELECT * FROM jobs WHERE title ~ 'developer|proqramci' "

# query="SELECT * FROM jobs WHERE salary BETWEEN 2500 AND 3000 and (company='Kontakt Home' or company='AzeriMed QSC' or company='A2Z Technologies')"

# query="SELECT * FROM jobs WHERE company='ABB ASC' and expiration_date<'2022-07-20' "

# query="SELECT * FROM jobs WHERE salary=(SELECT MAX(salary) FROM jobs WHERE lang='False' )   " 

# query="SELECT * FROM jobs WHERE salary=(SELECT MIN(salary) FROM jobs WHERE lang='True' )   " 
# query="SELECT AVG(salary) FROM jobs WHERE title ~ 'proqramci|developer'  " 

query="SELECT SUM(salary) FROM jobs WHERE (company='Kontakt Home' or company='AzeriMed QSC' or company='A2Z Technologies')   " 


query="SELECT * FROM jobs WHERE title~'PHP' "


query="UPDATE jobs SET salary=salary*1.15 WHERE salary<2000 and expiration_date>'2022-07-10' "

query="SELECT * FROM jobs WHERE expiration_date>'2022-07-10' and salary>2000  "

query="SELECT company,SUM(salary) FROM jobs WHERE expiration_date>'2022-07-10' GROUP BY company HAVING AVG(salary)>2000;   "

query=""

query="SELECT * FROM jobs"

cur.execute(query)
con.commit()
show(cur)






