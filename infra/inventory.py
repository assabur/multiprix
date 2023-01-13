conf = {"ssh_user": "root", "ssh_known_hosts_file": "known_hosts"}
try:
    open("id_rsa")
    conf["key"] = "id_rsa"
except:
    pass

multiprix = [("51.15.212.185", conf)]
