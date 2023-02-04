import mysql.connector

cnx = mysql.connector.connect(user='root', 
                              password = 'rOot..0203',
                              database= 'dogdog')
cursor = cnx.cursor()

class Users():
    def __init__(self, userId, name, email, password, pic):
        self.id = userId
        self.name = name
        self.email = email
        self.pswd = password
        self.bio = ""
        self.pic = pic # profile picture
        # self.loc = loc # location
        self.moments = [] # empty list, cuz no mements when creating account
        
        
    def updateProfile(self, user, updateVar, updateVal):
        inpt = f"UPDATE user SET {updateVar} = {updateVal} WHERE {self.id} == {user.id}"
        cnx.commit()
     
def createAccount(userId, name, email, password, pic):
    newUser = Users(userId, name, email, password, pic)
    inpt = (f"INSERT INTO user VALUES ({newUser.id}, '{newUser.name}', '{newUser.email}', '{newUser.pswd}', '{newUser.bio}');")
    print("inpt:", inpt)
    cursor.execute(inpt)
    cnx.commit() # otherwise the process won't be saved