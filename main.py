import winreg as reg


def addToReg():
    key = reg.OpenKey(reg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run", 0, reg.KEY_ALL_ACCESS)

    # Specify the full path to your Python executable and your script
    python_executable = "C:\\Pythons\\Python3.11\\pythonw.exe"
    script_path = "C:\\Users\\kiril\\PycharmProjects\\pythonProject\\proga.py"

    # Combine the Python executable and script path
    command = f'"{python_executable}" "{script_path}"'

    # Change the value of the Shell key to the Python executable
    reg.SetValueEx(key, "my_reg", 0, reg.REG_SZ, command)


addToReg()
