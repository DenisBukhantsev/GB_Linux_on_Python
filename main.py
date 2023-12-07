import subprocess


result = subprocess.run("cat /etc/os-release", shell=True, stdout=subprocess.PIPE, encoding="utf=8")
#print(result)
#out = result.stdout
#print(out)

def test_func(command, text):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding="utf=8")
    out = result.stdout
    if result.returncode == 0 and text in out:
        return True
    else:
        return False


print(test_func("cat /etc/os-release"))
