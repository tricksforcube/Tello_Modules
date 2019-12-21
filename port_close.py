''''

If tello connectivity fails with the below error run the below code , this closes the existing connection.

Error Message : [WinError 10048] Only one usage of each socket address (protocol/network address/port) is normally permitted

Again Rerun the tello class :)

'''

import os

to_get_port_no=os.popen("netstat -ano|findstr 8889")

command_output=to_get_port_no.read()

strip_command_output=command_output.strip()

port_no_to_terminate=""

for i in range(69,int(len(strip_command_output))):
    
    port_no_to_terminate+=strip_command_output[i]

commad_to_kill_port="taskkill /F /PID "+ port_no_to_terminate

kill_port=os.popen(commad_to_kill_port)
