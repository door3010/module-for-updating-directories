from Update_folders import UpdateFolders

example = UpdateFolders("credentials.json")
example.update("localpath_to_targetpath.json")
example.connection_close()
