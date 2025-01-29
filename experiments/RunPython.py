# import subprocess
# subprocess.run(["python3", "Run_Scorer_1.py "])

# filename = "Run_Scorer_1.py"
# with open(filename) as file:
#     exec(file.read())

# import Run_Scorer_1
# output = "Please reboot the server by following the instructions. Thank you!"
# expected = "Follow the instructions to reboot the server."
# print(Run_Scorer_1.main(input="prompt query", output=output, expected=expected))
# print(eval("Run_Scorer_1.main")("prompt query", output, expected))

import importlib
import importlib.util
import sys
from pathlib import Path
from typing import TYPE_CHECKING
from Generic_Scorer import Score

if TYPE_CHECKING:
    import types

def import_source_file(fname: str | Path, modname: str) -> "types.ModuleType":
    """
        Import a Python source file and return the loaded module.

        Args:
            fname: The full path to the source file.  It may container characters like `.`
                or `-`.
            modname: The name for the loaded module.  It may contain `.` and even characters
                that would normally not be allowed (e.g., `-`).
        Return:
            The imported module

        Raises:
            ImportError: If the file cannot be imported (e.g, if it's not a `.py` file or if
                it does not exist).
            Exception: Any exception that is raised while executing the module (e.g.,
                :exc:`SyntaxError).  These are errors made by the author of the module!
    """
    spec = importlib.util.spec_from_file_location(modname, fname)
    if spec is None:
        raise ImportError(f"Could not load spec for module '{modname}' at: {fname}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[modname] = module
    try:
        spec.loader.exec_module(module)
    except FileNotFoundError as e:
        raise ImportError(f"{e.strerror}: {fname}") from e
    return module

rs = import_source_file(Path("/Users/I050385/GitHub/Custom_Scorer/experiments/Run_Scorer_2024-10-23 13:59:47_434444.py"), "GenericScorer")
score =  rs.main(
    input="prompt query", 
    output="Please reboot the server by following the instructions. Thank you!", 
    expected="Follow the instructions to reboot the server.")
print(score.name, score.score)

