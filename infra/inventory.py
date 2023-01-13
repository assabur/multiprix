conf = {"ssh_user": "root"}
try:
    open("id_rsa")
    conf["key"] = "id_rsa"
except:
    pass

multiprix = [("51.15.212.185", conf)]
