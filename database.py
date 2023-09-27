import sqlite3
import json

class DB:
    def __init__(self):
        self.con = sqlite3.connect("PythonTutorialBot.db")
        self.c = self.con.cursor()
        
    #*/ MAIN DB */#        
        
    def check_user(self, user_id):
        self.c.execute("SELECT user_id FROM users")
        result = self.c.fetchall()
        for user in result:
            if str(user_id) == user[0]:
                return True
        return False
        
    def add_user(self, user_id, username, user_type, language):
        self.c.execute('INSERT INTO users VALUES (?,?,?,?,?)', [str(user_id), username, user_type, "0", language])
        self.con.commit()
        
    def get_lang(self, user_id):
        self.c.execute('SELECT lang FROM users WHERE user_id = (?)', [str(user_id)])
        return self.c.fetchall()[0][0]
        
    def get_type(self, user_id):
        self.c.execute('SELECT user_type FROM users WHERE user_id = (?)', [str(user_id)])
        return self.c.fetchall()[0][0]        
        
    def update_lang(self, user_id, new_lang):
        self.c.execute("UPDATE users SET lang = (?) WHERE user_id = (?)", [new_lang, str(user_id)])
        self.con.commit()
        

               
      
