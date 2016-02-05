import obd

connection = obd.OBD()

ra = connection.query(obd.commands.PIDS_A) # returns the response from the car
rb = connection.query(obd.commands.PIDS_B) # returns the response from the car
rc = connection.query(obd.commands.PIDS_C) # returns the response from the car

if not ra.is_null():
    print("PIDS 1 - 20")
    print(ra.value)


if not rb.is_null():
    print("PIDS 21-40")
    print(rb.value)


if not rc.is_null():
    print("PIDS 41-60")
    print(rc.value)
