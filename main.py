# import winreg as reg
#
#
# def addToReg():
#     key = reg.OpenKey(reg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run", 0, reg.KEY_ALL_ACCESS)
#
#     # Specify the full path to your Python executable and your script
#     python_executable = "C:\\Pythons\\Python3.11\\pythonw.exe"
#     script_path = "C:\\Users\\kiril\\PycharmProjects\\pythonProject\\proga.py"
#
#     # Combine the Python executable and script path
#     command = f'"{python_executable}" "{script_path}"'
#
#     # Change the value of the Shell key to the Python executable
#     reg.SetValueEx(key, "my_reg", 0, reg.REG_SZ, command)
#
#
# addToReg()
import winreg as reg


def add_to_reg(key_name, python_executable, script_path):
    key = reg.OpenKey(reg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Run", 0, reg.KEY_ALL_ACCESS)

    # Combine the Python executable and script path
    command = f'"{python_executable}" "{script_path}"'

    # Change the value of the specified key to the Python executable
    reg.SetValueEx(key, key_name, 0, reg.REG_SZ, command)


# Add multiple scripts to run at startup
add_to_reg("script1", "C:\\Pythons\\Python3.11\\pythonw.exe",
           "C:\\Users\\kiril\\PycharmProjects\\pythonProject\\proga.py")
add_to_reg("script2", "C:\\Pythons\\Python3.11\\pythonw.exe",
           "C:\\Users\\kiril\\PycharmProjects\\pythonProject\\progav2.py")
