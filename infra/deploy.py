from pyinfra.operations import apt, pip, files, server, systemd
from pathlib import Path

# INSTALLS
apt.key(keyserver="hkp://keyserver.ubuntu.com:80", keyid="8919F6BD2B48D754")
add_apt_repo = apt.repo(src="deb https://packages.clickhouse.com/deb stable main")
apt.packages(
    packages=["clickhouse-server", "clickhouse-client", "nginx", "python3-pip"]
)
pip.packages(["tornado", "pytest-playwright"])
server.shell(["playwright install"])

# COPY FILES
files.rsync("server", "/root/server")
files.rsync("scrap", "scrap")

# SCHEDULE SCRAP
server.crontab(
    "cd /root/scrap && python3 scrap.py",
    minute=0,
)

# MAKE A SERVICE FOR SERVER
sd = files.put(Path(__file__).parent / "mpserver.service", "/etc/systemd/system/")
systemd.service("mpserver", running=True, enabled=True, restarted=True)

#NGINX
nginconf = files.put(Path(__file__).parent / "nginx.conf", "/etc/nginx/")

