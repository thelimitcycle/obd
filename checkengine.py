import obd
connection = obd.OBD()
r = connection.query(obd.commands.GET_DTC) #Get the Diagnostic Trouble Codes
print(r.value)

#c = connection.query(obd.commands.CLEAR_DTC) #turn off the engine light
