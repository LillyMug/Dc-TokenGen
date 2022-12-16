import subprocess
import os

test_process = subprocess.Popen(["python", "main.py"])
test_process.wait()

if test_process.returncode == 0:
    print("The Code is Starting up pls wait")
else:
    print("failed with error code: {}".format(test_process.returncode))


os.chdir("src")