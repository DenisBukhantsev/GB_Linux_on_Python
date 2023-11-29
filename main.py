import subprocess


result = subprocess.run("cat /etc/os-release", shell=True, stdout=subprocess.PIPE, encoding="utf=8")
#print(result)
#out = result.stdout
#print(out)

def test_func(*args):
    result = subprocess.run(args, shell=True, stdout=subprocess.PIPE, encoding="utf=8")
    outt = result.stdout
    if result.returncode == 0:
        if "22.04" in outt and "jammy" in outt:
            return True
        else:
            return False

print(test_func("cat /etc/os-release"))
