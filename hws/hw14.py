# 📌 На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень)
# 📌 Напишите 3-7 тестов pytest (или unittest на ваш выбор) для данного проекта
# 📌 ОБЯЗАТЕЛЬНО! Используйте фикстуры
from sem13 import User
import pytest 

@pytest.fixture()
def name():
    name = ['Мария', 'Марина526', 'Марьяна Касимова', 9]
    return name

@pytest.fixture()
def level():
    level = [0, 7, -6, "4"]
    return level

@pytest.fixture()
def id_():
    id = ['1243', '001111', 'сфе']
    return id

def test_name_type(name, level, id):
    with pytest.raises(ValueError, match=r'Имя должно быть текстового вида'):
        User(name[2], level[0], id[0])

def test_level(name, level, id):
    with pytest.raises(ValueError, match=r'Личный идентификатор должен быть целым числом'):
        User(name[0], level[1], id[0])


def test_level_1(name, level, id):
    with pytest.raises(ValueError, match=r'Уровень доступа должен быть целым числом от 1 до 7'):
        User(name[0], level[1], id[0])

def test_id(name, level, id):
    with pytest.raises(ValueError):
        User(name[0], level[2], id[1])

def test_eq(name, level, id_):
    user_1 =User(name[0], level[0], id_[0])
    user_2 = User(name[0], level[0], id_[0])
    assert user_1 == user_2

if __name__ == '__main__':
    pytest.main(['-v'])


