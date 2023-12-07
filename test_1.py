import pytest
from HW_1 import chek_func
folder_in = "/home/user/folder_in"
folder_out = "/home/user/folder_out"
folder_ex = "/home/user/folder_ex"
def test_step1():
    assert chek_func(f"cd {folder_in}; 7z a {folder_out}/archive_1",  "Everything is Ok")

def test_step2():
    assert chek_func(f"cd {folder_out}; 7z d archive_1", "Everything is Ok")

def test_step3():
    assert chek_func(f"cd {folder_out}; 7z x {folder_out}",  "Everything is Ok")
#def test_step4():
    #assert chek_func(f"cd {folder_out}; 7z i {folder_ex}",  "Everything is Ok")
if __name__ == '__main__':
    pytest.main(["-vv"])