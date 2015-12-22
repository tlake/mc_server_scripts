# mc\_server\_scripts
A couple of simple scripts written in Python to automate and make easier
several aspects of running a Minecraft server. These were written for a setup
that uses ATLauncher and only a single server, but they should be somewhat
flexible for certain cases.

## Requirements:
 - `Python3`
 - `screen`

## To Use:
You'll need to define a few environment variables for these scripts to work:
 - `export MC_SCREEN_NAME="some_title_for_a_screen_session"`
 - `export MC_SERVERS_DIR="/path/of/directory/containing/server/directory/"`
 - `export MC_SERVER_NAME="name_of_server_directory"`
 - `export MC_BACKUPS_DIR="/path/of/directory/containing/backups/"`

#### Make sure these variables are stored at least at the session level!
I load them via the `.profile` file; otherwise, the
scripts won't be able to see them (if, for instance, they're loaded
though the `.bashrc` file).

Additionally, the startup script assumes that you have a `LaunchServer.sh`
file that starts up your server. This is the configuration that ATL uses,
anyway. It's easy enough to change to something else.