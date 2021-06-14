import sys
from cx_Freeze import setup, Executable
import math

base=None
if sys.platform == "win32":
	base = "win32GUI"
executables = [
        Executable("nome do programa.py",base=base)
]

buildOptions = dict(
	packages = []
	includes = ["math"]
	include_files = []
	excludes= []
)

setup(
	name = "nome do programa"
	version = "1.0",
	description = "define para que o prg"
	options = dict(build_exe = buildOptions),
	executables = excutables