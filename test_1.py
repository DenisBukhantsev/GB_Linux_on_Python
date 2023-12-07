import pytest

from HW_1 import test_func
def test_step1():

    assert test_func("cd /home/user/folder_in; 7z a /home/user/folder_out/archive_1",  "ever is ok")

def test_step2():
    assert test_func("cd /home/user/folder_out; 7z d archive_1", "ever is ok")
if __name__ == '__main__':
    pytest.main(["-vv"])