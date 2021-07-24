
import sqlite3 as db
from . import db_file


class BankDatabase:
    def __init__(self,*args,**kwargs):
        self.connection = db.connect(db_file)
        self.db_cursor  = self.connection.cursor()
        
        #============================== create database ==================
        self.create_tables()
        
    #================= create tables structure here
    def create_tables(self):
        self.db_cursor.execute("""
                               CREATE TABLE IF NOT EXISTS administrators(
                                   id INTEGER PRIMARY KEY,
                                   full_name VARCHAR(50) NOT NULL,
                                   birth_date VARCHAR(50),
                                   username VARCHAR(25) NOT NULL,
                                   password VARCHAR(25) NOT NULL,
                                   secret_code INTEGER NOT NULL UNIQUE
                               );""")
        self.db_cursor.execute("""
                                CREATE TABLE IF NOT EXISTS bank(
                                    id INTEGER PRIMARY KEY ,
                                    bank_name VARCHAR(25) NOT NULL,
                                    branch_code VARCHAR(50) NOT NULL,
                                    bank_balance DECIMAL(18,2) DEFAULT 0.0,
                                    admin_id INTEGER REFERENCES administrators(id)
                                );""")
        self.db_cursor.execute("""
                                CREATE TABLE IF NOT EXISTS users(
                                    id INTEGER PRIMARY KEY,
                                    full_name VARCHAR (50) NOT NULL,
                                    gender VARCHAR(7) NOT NULL,
                                    phone VARCHAR(15) NOT NULL,
                                    date_of_birth VARCHAR(50) NOT NULL,
                                    occupation VARCHAR(25) NOT NULL,
                                    identity_number VARCHAR(25) NOT NULL,
                                    admin_id INTEGER REFERENCES administrators(id)
                                    );""")
        self.db_cursor.execute("""
                                CREATE TABLE IF NOT EXISTS users_account(
                                    id INTEGER PRIMARY KEY,
                                    account_number VARCHAR(15) NOT NULL UNIQUE,
                                    current_balance DECIMAL(18,2) DEFAULT 0.0,
                                    user_id INTEGER REFERENCES users(id),
                                    admin_id INTEGER REFERENCES administrators(id)
                                );""")
        self.db_cursor.execute("""
                                CREATE TABLE IF NOT EXISTS transactions(
                                    id INTEGER PRIMARY KEY,
                                    amount DECIMAL(18,2) DEFAULT 0.0,
                                    transaction_date VARCHAR(50) NOT NULL,
                                    transaction_type VARCHAR(25) NOT NULL,
                                    user_id INTEGER REFERENCES users(id),
                                    account_id VARCHAR(15) REFERENCES users_account(account_number)
                                    );
                               """)
    
    #======================= insert into table here ====================================
    def insert_administrator(self,full_name,dob,username,password,secret_code):
        "insert into administrator accounts"
        try:
            
            self.db_cursor.execute("""
                                INSERT INTO administrators VALUES 
                                (
                                    NULL, ?, ?, ?,?, ?
                                );
                                """,
                                (full_name,dob,username,password,secret_code)
                                )
            # commit transaction of database
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False
            
    
    def insert_bank(self,bank_name,branch_code,bank_balance,admin_id):
        "insert into bank table "
        try:
            
            self.db_cursor.execute("""
                                INSERT INTO bank VALUES
                                (
                                    NULL, ?, ?, ?,?
                                    );
                                """, 
                                (bank_name,branch_code,bank_balance,admin_id)
                                )
            #commit transaction to database
            self.connection.commit()
            return True
        except  Exception as e:
            print(e)
            return False
    
    def insert_users(self,full_name,gender,phone,dob,occupation,identity,admin_id):
        "Insert into users table"
        try:
            self.db_cursor.execute("""
                                INSERT INTO users VALUES
                                (
                                    NULL, ?,?, ?, ?, ?, ?, ?
                                    );
                                """,
                                (full_name,dob,gender,phone,dob,occupation,identity,admin_id)
                                )
            # save to database
            self.connection.commit()
            return True
        except  Exception as e:
            print(e)
            return False
    
    def insert_users_accounts(self,account_number,current_balance,user_id,admin_id):
        "Insert into users accounts table"
        try:
            
            self.db_cursor.execute("""
                                INSERT INTO users_account VALUES
                                (
                                    NULL, ?,?,?,?
                                    );
                                """,(account_number,current_balance,user_id,admin_id)
                                )
            # save to database
            self.connection.commit()
            return True
        except  Exception as e:
            print(e)
            return False
    
    def insert_users_transaction_table(self,amount,transaction_date,transaction_type,user_id,account_id):
        "insert into users transaction table"
        try:
            self.db_cursor.execute("""
                                INSERT INTO transactions VALUES
                                (
                                    NULL, ?,?, ?, ?,?
                                    );
                                """,
                                (amount,transaction_date,transaction_type,user_id,account_id)
                                )
            # save to database
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
    
    # query from database here using selection query =====================================================
    
    def select_for_admin_login(self,username,password):
        "select admin username and pass for login"
        self.db_cursor.execute("SELECT username,password FROM administrators WHERE username=? AND password=?",
                               (username,password))
        return self.db_cursor.fetchone()

    def select_for_admin_password_recovery(self,username,secret_code):
        "select admin username and secret code from administrators forget password"
        self.db_cursor.execute("SELECT username,secret_code,password FROM administrators WHERE username=? AND secret_code = ?",
                               (username,secret_code))
        return self.db_cursor.fetchone()
        
        

#========================== instantiate to be imported by other files ====================================
database_file = BankDatabase()