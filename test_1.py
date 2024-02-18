import pytest
import yaml
from HW_1 import chek_func

with open('config.yaml') as f:
    data = yaml.safe_load(f)

def test_step1():
    assert chek_func(f"cd {data["folder_in"]}; 7z a {data["folder_out"]}/archive_1",  "Everything is Ok")

def test_step2():
    assert chek_func(f"cd {data["folder_out"]}; 7z d archive_1", "Everything is Ok")

def test_step3():
    assert chek_func(f"cd {data["folder_out"]}; 7z x {data["folder_out"]}",  "Everything is Ok")
#def test_step4():
    #assert chek_func(f"cd {folder_out}; 7z i {folder_ex}",  "Everything is Ok")
if __name__ == '__main__':
    pytest.main(["-vv"])
