import winreg as reg


def addToReg():
    key = reg.OpenKey(reg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run", 0, reg.KEY_ALL_ACCESS)

    python_executable = "C:\\Pythons\\Python3.11\\pythonw.exe"
    script_path = "C:\\Users\\kiril\\PycharmProjects\\pythonProject\\proga.py"

    command = f'"{python_executable}" "{script_path}"'

    reg.SetValueEx(key, "my_reg2", 0, reg.REG_SZ, command)


addToReg()
