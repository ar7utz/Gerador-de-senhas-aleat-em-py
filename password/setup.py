import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"], "includes": ["tkinter"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Gerador de Senhas aleatórias",
    version="0.1",
    description="my GUI application",
    options={"build_exe": build_exe_options},
    executables=[Executable("password/gerador_de_senha.py", base=base)]
)
