import subprocess
import os
from time import sleep
from datetime import datetime
import yaml


class StartupMinion:
    def __init__(self, conf_file='config.yml'):
        with open(conf_file, 'r') as f:
            conf = yaml.safe_load(f)
        self.servers_path = os.path.join(
            conf['base_path'],
            conf['atlauncher_dir'],
            conf['servers_dir'],
        )
        self.servers = conf['servers']
        self.launch_command = conf['launch_command']

    def _start(self, server):
        screen_title = 'mc_' + server
        server_loc = os.path.join(self.servers_path, server)
        daemonize_screen = "screen -dmS " + screen_title
        stuffing = "'cd " + server_loc + " && " + self.launch_command + "\n'"
        stuff_screen = "screen -S " + screen_title + " -X stuff " + stuffing
        bash_command = daemonize_screen + " && " + stuff_screen
        logfile = os.path.join(server_loc, "logs", "latest.log")

        sleep(1)
        print("Let's get this party started!")
        print("Starting party for: " + server)
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
                finished = data.find(
                    "[" + now + "] [Server thread/INFO]: Done ("
                )

        print("Server's up and running!")
        sleep(1)
        print("Have fun!")
        sleep(4)

    def start(self, these_servers='all'):
        if these_servers == 'all':
            for server in self.servers:
                self._start(server)
        elif isinstance(these_servers, list):
            for server in these_servers:
                if server in self.servers:
                    self._start(server)
        elif isinstance(these_servers, int):
            self._start(self.servers[these_servers])
        else:
            print("Invalid choice. Supply either a server name that exists,"
                  + "or the index of a server in the config.yml list. "
                  "Or just leave blank to start every server in the config.")


if __name__ == "__main__":
    minion = StartupMinion()
    minion.start()
