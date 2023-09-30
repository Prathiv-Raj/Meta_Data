import os

filename="/home/cyber-bot/Documents/vscode/image.txt"

stats=os.stat(filename)

print("File creation time     :",os.path.getctime(filename))

print("file size              :",stats.st_size,"kb")
print("file last modifed time :",stats.st_mtime)
print("File user id           :",stats.st_uid)
print("File group id          :",stats.st_gid)
print("File device id         :",stats.st_dev)