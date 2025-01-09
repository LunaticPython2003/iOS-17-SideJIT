import subprocess
import sys
import os
import pywintunx_pmd3
class InstallDeps:
    def __init__(self):
        command = [
            sys.executable,
            "-m",
            "pip",
            "install",
            "-r",
            "requirements.txt",
        ]
        subprocess.run(command)
        os.add_dll_directory(os.path.abspath("JIT/assets"))

    def install_drivers():
        pywintunx_pmd3.install_wetest_driver()

    def uninstall_driver():
        pywintunx_pmd3.uninstall_wetest_driver()
        pywintunx_pmd3.delete_driver()