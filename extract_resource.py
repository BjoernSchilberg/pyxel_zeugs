import zipfile
import tomllib
import pprint

with zipfile.ZipFile("my_resource.pyxres", "r") as zf:
    with zf.open("pyxel_resource.toml", "r") as f:
        b = f.read()

s = b.decode("utf-8")
tml = tomllib.loads(s)
pprint.pprint(tml)
