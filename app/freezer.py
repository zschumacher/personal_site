from flask_frozen import Freezer
from app import app
import shutil
import os
import pathlib
freezer = Freezer(app)

if __name__ == '__main__':
    work_dir = pathlib.Path(__file__).parent
    root = str(work_dir.parent)
    build_dir = pathlib.Path(work_dir, "build")
    freezer.freeze()
    shutil.rmtree(str(pathlib.Path(root, "static")), ignore_errors=True)
    shutil.move(str(pathlib.Path(build_dir, "index")), str(pathlib.Path(root, "index.html")))
    shutil.move(str(pathlib.Path(work_dir, "build", "static")), str(pathlib.Path(root)))
    shutil.rmtree(build_dir)
