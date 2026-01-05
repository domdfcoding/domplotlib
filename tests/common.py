# stdlib
import sys

# 3rd party
import pytest
from domdf_python_tools.paths import PathPlus

if sys.version_info[:2] == (3, 7):
	baseline_dir = str(PathPlus(__file__).parent / "baseline_37")
else:
	baseline_dir = str(PathPlus(__file__).parent / "baseline")

check_images = pytest.mark.mpl_image_compare(
		baseline_dir=baseline_dir,
		savefig_kwargs={"dpi": 600},
		)
