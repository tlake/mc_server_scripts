# mc\_server\_scripts
A small, easy-to-manage collection of Python3 scripts that make starting,
stopping, and backing up Minecraft servers a breeze. I'm a big fan of
[ATLauncher](https://www.atlauncher.com/) so the scripts are by default
tailored for an ATL-usage setup, but it should be easy enough to tweak
them for your own use case.

## Setup:
These scripts require the PyYaml package. Install it with:

```
pip install yaml
```

Minecraft servers are run in their own separate screen sessions. You
can get screen with:

```
sudo apt-get install screen
```

Beyond that, the rest of setup really only requires that you customize
the `config.yml` file to suit your system's architecture. Given an
example directory tree like this one:

```
/home/
└── <username>/
    └── Desktop/
        └── ATLauncher/
            ├── Backups/
            └── Servers/
                ├── server_0/
                │   │   LaunchServer.sh
                │   │   other-files-and-folders
                │   │   ...
                ├── server_1/
                │   │   LaunchServer.sh
                │   │   other-files-and-folders
                │   │   ...
```

The config file would look like this:

```
base_path: "/home/<username>/Desktop"
atlauncher_dir: "ATlauncher"
servers_dir: "Servers"
backups_dir: "Backups"
launch_command: "./LaunchServer.sh"

servers:
    - "server_1"
    - "server_2"
```

## To Use:
Each script can be executed with Python itself:

```
python3 start_server.py
```

For even more ease of use, you can make desktop icons or shortcuts that
execute these Python scripts just by clicking them. If you've put a virtualenv
inside the project directory, make sure that your shortcut activates the env
before running the script. For example, my desktop shortcuts contain a line
like this:

```
EXEC sh -c "cd /home/tanner/scripts/mc_server_scripts; . env/bin/activate; ./start_server.py"
```