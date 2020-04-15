import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=KHURAM\SQLEXPRESS;'
                      'Database=FYP;'
                      'Trusted_connection=yes;')


def add_camera(c_id, name, loc, x_cord, y_cord):
    cam_id = int(c_id)
    cursor = conn.cursor()
    cursor.execute("select * from camera")
    rows = cursor.fetchall()
    for row in rows:
        val = row.camera_id
        if val == cam_id:
            return 0

    cursor.execute("insert into camera(camera_id, camera_name, camera_location, x_coordinate, y_coordinate) "
                   "values(?, ?, ?, ?, ?)", (int(cam_id), name, loc, x_cord, y_cord))
    cursor.commit()
    return 1


def login_check(usr, pswd):
    # abc = 'khuram'
    cursor = conn.cursor()
    cursor.execute("select * from [user] where user_name =? and password =?", (usr, pswd))
    rows = cursor.fetchall()

    if len(rows) > 0:
        return 1
    else:
        return 0


def add_rule(r_id, name, finee):
    rl_id = int(r_id)
    fine = int(finee)
    cursor = conn.cursor()
    cursor.execute("select * from [rule]")
    rows = cursor.fetchall()
    for row in rows:
        val = row.rule_id
        if val == rl_id:
            return 0

    cursor.execute("insert into [rule](rule_id, rule_name, fine) values(?, ?, ?)", (int(r_id), name, int(finee)))
    cursor.commit()
    return 1


def add_vehicle(vh_id, v_name, v_color, l_nmbr, owner):
    v_id = int(vh_id)

    cursor = conn.cursor()
    cursor.execute("select * from vehicle")
    rows = cursor.fetchall()
    for row in rows:
        val = row.vehicle_id
        if val == v_id:
            return 0

    cursor.execute("insert into vehicle(vehicle_id, vehicle_name, vehicle_color, licence_number, vehicle_owner) "
                   "values(?, ?, ?, ?, ?)", (int(v_id), v_name, v_color, l_nmbr, owner))
    cursor.commit()
    return 1


def delete_camera(c_id):
    cam_id = int(c_id)

    cursor = conn.cursor()
    cursor.execute("select * from camera where camera_id = ?", (int(cam_id)))
    rows = cursor.fetchall()
    # print(rows)
    if len(rows) == 0:
        return 0

    cursor.execute("delete from camera where camera_id = ?", (int(cam_id)))
    cursor.commit()
    return 1


def delete_rule(r_id):
    rule_id = int(r_id)

    cursor = conn.cursor()
    cursor.execute("select * from [rule] where rule_id = ?", (int(rule_id)))
    rows = cursor.fetchall()
    # print(rows)
    if len(rows) == 0:
        return 0

    cursor.execute("delete from [rule] where rule_id = ?", (int(rule_id)))
    cursor.commit()
    return 1


def delete_vehicle(v_id):
    vh_id = int(v_id)

    cursor = conn.cursor()
    cursor.execute("select * from vehicle where vehicle_id = ?", (int(vh_id)))
    rows = cursor.fetchall()
    # print(rows)
    if len(rows) == 0:
        return 0

    cursor.execute("delete from vehicle where vehicle_id = ?", (int(vh_id)))
    cursor.commit()
    return 1


def fetch_vehicles_edit(v_id):
    vh_id = int(v_id)

    cursor = conn.cursor()
    cursor.execute("select * from vehicle where vehicle_id = ?", (int(vh_id)))
    rows = cursor.fetchall()
    return rows


def edit_vehicle(id, name, color, l_nmbr, owner):
    v_id = int(id)
    #print(v_id)
    cursor = conn.cursor()

    cursor.execute("update vehicle set vehicle_name = ?, vehicle_color = ?, licence_number = ?, vehicle_owner = ? where"
                   " vehicle_id = ?", (name, color, l_nmbr, owner, int(v_id)))
    cursor.commit()
    return 1

def fetch_rule_edit(r_id):
    ru_id = int(r_id)

    cursor = conn.cursor()
    cursor.execute("select * from [rule] where rule_id = ?", (int(ru_id)))
    rows = cursor.fetchall()
    return rows


def edit_rule(id, r_name, fine):
    r_id = int(id)
    print(r_id)
    cursor = conn.cursor()

    cursor.execute("update [rule] set rule_name = ?, fine = ? where"
                   " rule_id = ?", (r_name, fine, int(r_id)))
    cursor.commit()
    return 1

def camera_search(c_id):
    cam_id = int(c_id)

    cursor = conn.cursor()
    cursor.execute("select * from camera where camera_id = ?", (int(cam_id)))
    rows = cursor.fetchall()
    return rows

def change_pass(c_pass, n_pass):

    cursor = conn.cursor()
    cursor.execute("select * from [user] where password = ?", c_pass)
    rows = cursor.fetchall()
    if len(rows) == 0:
        return 0
    else:
        id = rows[0][0]
        print(id)
    cursor.execute("update [user] set password = ? where user_id = ?", (n_pass, id))
    cursor.commit()
    return 1