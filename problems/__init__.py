import sys

from common.practice import ensure_practice_files

# Do not write __pycache__ folders next to practice.py.
# The problem folder must only show practice.py, question.md, and _internal/.
sys.dont_write_bytecode = True

# Each problem imports practice.py, but git does not keep that file.
# Make the missing practice.py files before a problem is imported.
ensure_practice_files()
