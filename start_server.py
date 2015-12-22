#!/usr/bin/env python

if __name__ == "__main__":

    import subprocess, os
    from time import sleep
    from datetime import datetime

    screen_name = os.environ.get('MC_SCREEN_NAME')
    servers_dir = os.environ.get('MC_SERVERS_DIR')
    server_name = os.environ.get('MC_SERVER_NAME')

    server_loc = os.path.join(servers_dir, server_name)
    launch_command = "./LaunchServer.sh"

    daemonize_screen = "screen -dmS " + screen_name

    stuffing = "'cd " + server_loc + " && " + launch_command + "\n'"
    stuff_screen = "screen -S " + screen_name + " -X stuff " + stuffing

    bash_command = daemonize_screen + " && " + stuff_screen

    logfile = os.path.join(server_loc, "logs", "latest.log")


    sleep(1)
    print("The script's up! Excellent news!\nLet's get this party started.")
    sleep(1)
    print("Running command:\n" + bash_command)
    print("This may take a few minutes. Be patient, please!")
    sleep(1)
    subprocess.Popen(['bash', '-c', bash_command])

    finished = -1
    time_counter = 0
    while finished == -1:
        sleep(0.25)
        time_counter += 0.25

        if time_counter % 10 == 0:
            print("Waiting for server... (%ss)" % time_counter)
        
        with open(logfile, "r") as fh:
            data = fh.read()
            now = datetime.now().strftime("%H:%M:%S")
            finished = data.find("[" + now + "] [Server thread/INFO]: Done (")


    print("Server's up and running!")
    sleep(1)
    print("Have fun!")
    sleep(4)