from testproject.lib import call_teacher

def test_call_teacher():
    assert type(call_teacher()) == str