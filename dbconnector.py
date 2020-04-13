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
