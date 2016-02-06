#!/usr/bin/env python

import os
from time import sleep
from datetime import datetime
from shutil import make_archive
import yaml


class BackupMinion:
    def __init__(self, conf_file='config.yml'):
        with open(conf_file, 'r') as f:
            conf = yaml.safe_load(f)
        self.servers_path = os.path.join(
            conf['base_path'],
            conf['atlauncher_dir'],
            conf['servers_dir'],
        )
        self.backups_path = os.path.join(
            conf['base_path'],
            conf['atlauncher_dir'],
            conf['backups_dir'],
        )
        self.servers = conf['servers']

    def _backup(self, server):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
        archive_title = timestamp + "_" + server
        new_archive = os.path.join(self.backups_path, archive_title)

        root_dir = self.servers_path
        base_dir = server

        print("In the mood for some protection, eh?")
        sleep(1)
        print("That's smart. Safety first!")
        sleep(1)
        print("Here we go!\nRunning commmand:")
        print(
            "make_archive("
            + new_archive
            + ", 'gztar', "
            + root_dir
            + ", "
            + base_dir
            + ")"
        )
        print("(This might take a minute...)")
        make_archive(new_archive, 'gztar', root_dir, base_dir)
        sleep(1)
        print("Alrighty! You should now have a backup at:\n" + new_archive)
        sleep(1)
        print("Until next time!")
        sleep(2)

    def backup(self, these_servers='all'):
        if these_servers == 'all':
            for server in self.servers:
                self._backup(server)
        elif isinstance(these_servers, list):
            for server in these_servers:
                if server in self.servers:
                    self._backup(server)
        elif isinstance(these_servers, int):
            self._backup(self.servers[these_servers])
        else:
            print("Invalid choice. Supply either a server name that exists,"
                  + "or the index of a server in the config.yml list. "
                  "Or just leave blank to start every server in the config.")


if __name__ == "__main__":
    minion = BackupMinion()
    minion.backup()
