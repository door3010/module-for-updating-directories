from UpdateFolders import UpdateFolders

with UpdateFolders("credentials.json") as updater:
    updater.update("localpath_to_targetpath.json")
