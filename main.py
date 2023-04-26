import mysql.connector


def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Mahirnuri1.',
            database='example1'
        )
        return connection
    except mysql.connector.Error as error:
        print(f"Failed to connect to MySQL database: {error}")
        return None






if __name__ == '__main__':
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM ZORT")
    for x in cursor:
        print(x)
    new_balance = 0
    balance1 = 0
    nam = input("Enter your name: ")
    pas = input("Create a password? ")
   


def create_account():
    confirm = input("Confirm your password: ")
    if confirm == pas:
        id1 = input("Enter id for the first time: ")
        balance1 = 0
        cursor.execute(
            "INSERT INTO zort (name, password, id, balance) VALUES (%s, %s, %s,%s)",
            (nam, pas, id1, balance1)
        )
        connection.commit()
        print("Your account is successfully created! Your new id is " + str(id1))
    else:
        print("Your passwords do not match! Try again")
        create_account()


def deposit():
    connection = connect_to_db()
    cursor = connection.cursor()
    amount = int(input("Enter the amount you want to deposit: "))
    acn = input("Enter id: ")
    a = 'select balance from zort where id = %s'
    data = (acn,)
    cursor.execute(a, data)
    result = cursor.fetchall()  
    if result is None or len(result) == 0:
        print(f"No data found for id {acn}")
    else:
        t = result[0][0] + amount
        sql = 'update zort set balance = %s where id = %s'
        d = (t, acn)
        cursor.execute(sql, d)
        connection.commit()
        cursor.execute('select balance from zort where id = %s', (acn,))
        result = cursor.fetchone()
        if result is None:
            print(f"No data found for id {acn}")
        else:
            print(f"Your current balance is: {result[0]}")
















def withdraw():
    connection = connect_to_db()
    cursor = connection.cursor()
    amount = int(input("Enter the amount you want to withdraw: "))
    acn = input("Enter id: ")
    a = 'select balance from zort where id = %s'
    data = (acn,)
    cursor.execute(a, data)
    result = cursor.fetchall()
    if result is None or len(result) == 0:
        print(f"No data found for id {acn}")
    else:
        t = result[0][0] - amount
        if t < 0:
            print("Insufficient balance")
        else:
            sql = 'update zort set balance = %s where id = %s'
            d = (t, acn)
            cursor.execute(sql, d)
            connection.commit()
            cursor.execute('select balance from zort where id = %s', (acn,))
            result = cursor.fetchone()
            if result is None:
                print(f"No data found for id {acn}")
            else:
                print(f"Current balance after withdrawal: {result[0]}")






       
def check_balance():
    connection = connect_to_db()
    cursor = connection.cursor()
    acn = input("Enter id: ")
    a = 'select balance from zort where id = %s'
    data = (acn,)
    cursor.execute(a, data)
    result = cursor.fetchone()
    if result is None:
        print(f"No data found for id {acn}")
    else:
        print(f"Current balance: {result[0]}")










print("Welcome to Fatih Banking")
while True:
    print("1/Create an account  2/Deposit   3/Withdraw    4/Account Information 5/Check balance Else/Exit")
    ans = int(input("Please choose one option: "))
    if ans == 1:
        print(create_account())
    elif ans == 2:
        deposit()
       
    elif ans == 3:
        withdraw()
    elif ans == 5:
        check_balance()
    elif ans == 4 :
        print("Your account informations are: \n" + "User Name: " + nam + "\nPassword: " + pas + "\nId:" + str(id1))
    else:
        print("See you!")
        exit()