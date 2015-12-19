#!/usr/bin/env python

if __name__ == "__main__":

    import subprocess
    import os
    from time import sleep

    screen_name = "minecraft_server"

    # Be sure to populate with the actual path to the server directory:
    server_loc = "PATH/TO/DIRECTORY/CONTAINING/THE/SERVER/"
    launch_command = "./LaunchServer.sh"

    daemonize_screen = "screen -dmS " + screen_name

    stuffing = "'cd " + server_loc + " && " + launch_command + "\n'"
    stuff_screen = "screen -S " + screen_name + " -X stuff " + stuffing

    bash_command = daemonize_screen + " && " + stuff_screen

    logfile = os.path.join(server_loc, "logs", "latest.log")


    sleep(1)
    print("It started up! Excellent news!\nHang on a sec.")
    sleep(1)
    print("Running command: " + bash_command)
    sleep(1)
    subprocess.Popen(['bash', '-c', bash_command])
    sleep(1)


    time_counter = 0
    finished = -1
    while finished == -1:
        print("Waiting for server to be ready... (%ss)" % time_counter)
        time_counter += 10
        sleep(10)
        
        with open(logfile, "r") as fh:
            data = fh.read()
            finished = data.find("] [Server thread/INFO]: Done (")


    print("Server running!")
    sleep(1)
    print("Process completed. Bye!")
    sleep(2)