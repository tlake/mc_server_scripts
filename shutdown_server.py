#!/usr/bin/env python

if __name__ == "__main__":

    import subprocess
    import os
    from time import sleep

    screen_name = "minecraft_server"
    stuff_screen = "screen -S " + screen_name + " -X stuff "

    cmd_save = stuff_screen + "'save-all\n'"
    cmd_shutdown = stuff_screen + "'stop\n'"
    cmd_kill_screen = stuff_screen + "'exit\n'"

    sleep(1)
    print("Alright server, it's time to go to sleep!")
    sleep(1)
    print("Let's save the world first.")
    sleep(1)
    subprocess.Popen(['bash', '-c', cmd_save])
    sleep(1)
    print("Done.")
    sleep(1)
    print("We can switch it off now.")
    sleep(1)
    subprocess.Popen(['bash', '-c', cmd_shutdown])
    sleep(2)
    print("One last loose end - let's terminate that screen session.")
    sleep(1)
    subprocess.Popen(['bash', '-c', cmd_kill_screen])
    sleep(1)
    print("That should do it. Sleep tight!")
    sleep(2)
