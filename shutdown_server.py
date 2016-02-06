#!/usr/bin/env python

import subprocess
from time import sleep
import yaml


class ShutdownMinion:
    def __init__(self, conf_file='config.yml'):
        with open(conf_file, 'r') as f:
            conf = yaml.safe_load(f)
        self.servers = conf['servers']

    def _shutdown(self, server):
        screen_title = 'mc_' + server
        stuff_screen = "screen -S " + screen_title + " -X stuff "

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

    def shutdown(self, these_servers='all'):
        if these_servers == 'all':
            for server in self.servers:
                self._shutdown(server)
        elif isinstance(these_servers, list):
            for server in these_servers:
                if server in self.servers:
                    self._shutdown(server)
        elif isinstance(these_servers, int):
            self._shutdown(self.servers[these_servers])
        else:
            print("Invalid choice. Supply either a server name that exists,"
                  + "or the index of a server in the config.yml list. "
                  + "Or just leave blank to start every server in the config.")


if __name__ == "__main__":
    minion = ShutdownMinion()
    minion.shutdown()
