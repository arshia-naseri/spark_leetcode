import sys

from common.practice import ensure_practice_files

# Do not write __pycache__ folders next to the practice files.
# The problem folder must only show the practice files, question.md, and _internal/.
sys.dont_write_bytecode = True

# Each problem imports its practice files, but git does not keep them.
# Make the missing practice files before a problem is imported.
ensure_practice_files()
