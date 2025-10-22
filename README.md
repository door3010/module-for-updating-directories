# Update_folders
Files and utilities for managing remote server. Utilities are based on paramiko, json, platform, os - python packages

credentials.json - contains credentials needed to connect to remote-machine
format:
```
{
    "hostname": "000.000.000.000",
    "port": 0,
    "username": "username",
    "password": "password"
}
```

localpath_to_targetpath.json - contains pairs of pathes
format:
```
{
    "localpath1":"targetpath1",
    "localpath2":"targetpath2"
}
```

Update_folders.py - main module. 
Class `UpdateFolders` gets path to json credentials file, `update()` method gets path to json localpath_to_targetpath file

## Usage example:
```
from Update_folders import UpdateFolders

example = UpdateFolders("credentials.json") # create an instance
example.update("localpath_to_targetpath.json")  # call update method with path/to/file.json

example.connection_close() # Importantly recall close connection function
```
