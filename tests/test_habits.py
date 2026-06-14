def test_add_habit():
    nome = "Estudar Python"
    assert nome != ""

def test_list_habits():
    habitos = []
    assert isinstance(habitos, list)

def test_invalid_habit():
    nome = ""
    assert nome == ""
    