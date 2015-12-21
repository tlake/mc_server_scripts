#!/usr/bin/env python

if __name__ == "__main__":

    import subprocess
    import os
    from time import sleep
    import datetime
    from shutil import make_archive

    # PERSONALIZE IN THREE PLACES:

    # HERE
    server_name = "SERVER_NAME_HERE"
    servers_dir = os.path.expanduser(
        # HERE
        os.path.join("~", "YOUR", "CONTENT", "HERE")
    )
    backups_dir = os.path.expanduser(
        # AND HERE
        os.path.join("~", "YOUR", "CONTENT", "HERE")
    )
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
    archive_title = timestamp + "_" + server_name
    archive_name = os.path.join(backups_dir, archive_title)

    root_dir = servers_dir
    base_dir = server_name

    print("In the mood for some protection, eh?")
    sleep(1)
    print("That's smart. Safety first!")
    sleep(1)
    print("Here we go...")
    make_archive(archive_name, 'gztar', root_dir, base_dir)
    sleep(1)
    print("Alrighty, that should do it.")
    print("You should now have a backup at '" + archive_name + "'!")
    sleep(1)
    print("Until next time!")
    sleep(2)
