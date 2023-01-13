
from pathlib import Path
rpath = Path(__file__).parent.parent / "requirements.txt"
print(rpath)
print(open(rpath).readlines())