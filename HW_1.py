import subprocess




def chek_func(command, text):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding="utf=8")
    out = result.stdout
    if result.returncode == 0 and text in out:
        return True
    else:
        return False

def checkout_negative(command, text):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
    if result.returncode != 0 and (text in result.stderr or text in result.stdout):
        return True
    else:
        return False
