import sqlite3
import json

class DB:
    def __init__(self):
        self.con = sqlite3.connect("PythonTutorialBot.db")
        self.c = self.con.cursor()
        
    #*/ MAIN DB */#        
    # Schema: user_id, username, user_type, score, language
    def check_user(self, user_id):
        self.c.execute("SELECT user_id FROM users")
        result = self.c.fetchall()
        for user in result:
            if str(user_id) == user[0]:
                return True
        return False
        
    def add_user(self, user_id, username, user_type, language):
        self.c.execute('INSERT INTO users VALUES (?,?,?,?,?)', [str(user_id), username, user_type, "0", language])
        if user_type.lower() == "group":
            self.c.execute("INSERT INTO settings VALUES (?,?,?)", [str(user_id), username, "off"])
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
        
    #*/ Group Settings DB */#
    # Schema: 1- group_user, 2-group id, 3-priavte_send
    def get_settings(self, group_id):
        self.c.execute('SELECT private_send FROM settings WHERE group_id=(?)', [str(group_id)])
        return self.c.fetchall()[0][0]
        

    def update_settings(self, group_id, status):
        self.c.execute("UPDATE settings SET private_send = (?) WHERE group_id = (?)", [status, str(group_id)])
        self.con.commit()