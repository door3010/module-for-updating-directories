# UpdateFolders
Utility for copying files from local directory and transfering it to remote directory on remote machine.

credentials.json - contains credentials needed to connect to remote-machine
### format:
```
{
    "hostname": "000.000.000.000",
    "port": 0,
    "username": "username",
    "password": "password",
    "target_os": "target_os"
}
```

localpath_to_targetpath.json - contains pairs of paths(must be paths to folders)
### format:
```
{
    "localpath1":"targetpath1",
    "localpath2":"targetpath2"
}
```

## Usage example:
```
from UpdateFolders import UpdateFolders

example = UpdateFolders("credentials.json")
example.update("localpath_to_targetpath.json")

example.connection_close()
```
