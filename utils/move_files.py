from pathlib import Path
import shutil

path = Path("../../simple_hwr/data/prepare_IAM_Lines/lines")
dst = Path("../data/lines")
for f in path.rglob("*.png"):
	shutil.copy(str(f), str(dst))
