"""Install client dependencies"""

from zipfile import ZipFile
from requests import get

print("Installing bootstrap")
bootstrap = get(
    "https://github.com/twbs/bootstrap/releases/download/v5.3.3/bootstrap-5.3.3-dist.zip",
    timeout=10,
)

print("Saving to disk")
with open("static/external/bootstrap-5.3.3-dist.zip", "wb") as f:
    f.write(bootstrap.content)

print("Extracting bootstrap")
with ZipFile("static/external/bootstrap-5.3.3-dist.zip") as zipfile:
    zipfile.extractall('static/external')
