from pyinfra.operations import apt

apt.key(keyserver="hkp://keyserver.ubuntu.com:80", keyid="8919F6BD2B48D754")
add_apt_repo = apt.repo(src="deb https://packages.clickhouse.com/deb stable main")
apt.packages(
    packages=["clickhouse-server", "clickhouse-client", "nginx"]
)
