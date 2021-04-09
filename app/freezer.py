from flask_frozen import Freezer
from app import app
import shutil
import os
from pathlib import Path

freezer = Freezer(app)

if __name__ == '__main__':
    cwd = Path(__file__).parent
    build_dir = str(Path(cwd, "build"))
    root = cwd.parent
    freezer.freeze()
    for item in os.listdir(Path(cwd, "build")):
        file_path = str(Path(cwd, "build", item))
        if item == "index":
            # fix weird frozen flask bug
            item = "index.html"
        destination = str(Path(root, item))
        shutil.move(file_path, destination)

    shutil.rmtree(build_dir)
