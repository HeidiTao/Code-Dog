import mysql.connector

cnx = mysql.connector.connect(user='root', 
                              password = 'rOot..0203',
                              database= 'dogdog')
cursor = cnx.cursor()

# class Tables():
#     def __init__(self):

def orderby(columnVar, asc):
    if asc: # ascending order
        inpt = f"SELECT * FROM post ORDER BY {columnVar} ASC"
    else: # descending order
        inpt = f"SELECT * FROM post ORDER BY {columnVar} DESC"
    cursor.execute(inpt)
    
def dogFilter(var, varVal, loc, locVal):
    showL = []
    inpt = "SELECT * FROM post WHERE {var} == {varVal} AND {loc} = {locVal}"
    cursor.execute(inpt)
    for elem in cursor.fetchall():
        showL.append(elem)
        
    