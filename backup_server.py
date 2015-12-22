#!/usr/bin/env python

if __name__ == "__main__":

    import subprocess, os
    from time import sleep
    from datetime import datetime
    from shutil import make_archive

    server_name = os.environ.get('MC_SERVER_NAME')
    servers_dir = os.environ.get('MC_SERVERS_DIR')
    backups_dir = os.environ.get('MC_BACKUPS_DIR')
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    archive_title = timestamp + "_" + server_name
    archive_name = os.path.join(backups_dir, archive_title)

    root_dir = servers_dir
    base_dir = server_name

    print("In the mood for some protection, eh?")
    sleep(1)
    print("That's smart. Safety first!")
    sleep(1)
    print("Here we go!\nRunning commmand:")
    print(
        "make_archive("
        + archive_name
        + ", 'gztar', "
        + root_dir
        + ", "
        + base_dir
        + ")"
    )
    print("(This might take a minute...)")
    make_archive(archive_name, 'gztar', root_dir, base_dir)
    sleep(1)
    print("Alrighty! You should now have a backup at:\n" + archive_name)
    sleep(1)
    print("Until next time!")
    sleep(2)
