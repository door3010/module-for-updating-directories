# UpdateFolders

Copy local directories to a remote machine over SFTP.

## Install

```
pip install -r requirements.txt
```

## Configuration

`credentials.json` — how to reach the remote machine:

```json
{
    "hostname": "000.000.000.000",
    "port": 22,
    "username": "username",
    "password": "password"
}
```

`localpath_to_targetpath.json` — pairs of folders to copy (local path -> remote path):

```json
{
    "/home/me/project": "/srv/project",
    "/home/me/assets": "/srv/assets"
}
```

Remote paths always use `/`, whichever OS the remote machine runs.

## Usage

```python
from UpdateFolders import UpdateFolders

with UpdateFolders("credentials.json") as updater:
    updater.update("localpath_to_targetpath.json")
```

The connection is closed automatically when the `with` block exits. Without
`with`, call `close()` yourself:

```python
updater = UpdateFolders("credentials.json")
try:
    updater.update("localpath_to_targetpath.json")
finally:
    updater.close()
```

Directories that do not exist on the remote machine are created, including any
missing parents. Files that already exist are overwritten.

## Layout

```
UpdateFolders.py   the whole implementation
__init__.py        exports UpdateFolders
example/           sample configuration and script
```
