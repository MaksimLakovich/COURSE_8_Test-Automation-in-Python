import pytest
from string_utils import StringUtils


"""
1. Юнит-тесты для CAPITILIZE: принимает на вход текст, делает первую букву заглавной и возвращает этот же текст. Пример: "skypro" -> "Skypro"
"""
@pytest.mark.parametrize("text, result",
                        [
                            ("hello", "Hello"),                                        # не пустая строка (латиница)
                            ("привет", "Привет"),                                      # не пустая строка (кирилица)
                            ("Тест", "Тест"),                                          # начало с заглавной
                            ("юнит тест 1 для", "Юнит тест 1 для"),                    # текст с пробелами
                            ("тест Ивана", "Тест Ивана"),                              # два слова, второе с заглавной
                            ("ТЕСТ", "ТЕСТ"),                                          # все заглавные
                            ("123", "123"),                                            # числа как строка
                            (" описание", " Описание"),                                # начало с пробела
                            ("@!- ?;", "@!- ?;"),                                      # только спецсимволы
                            ("20-мая-2024", "20-мая-2024")                             # текст без пробела с разным набором символов (спец, буквы, цифры)
                        ]
                        )
def positive_test_capitilize(text, result):
    x = StringUtils()
    res = x.capitilize(text)
    assert res == result


@pytest.mark.parametrize("text, result",
                        [
                            ("", ""),                                                  # пустая строка
                            (" ", " "),                                                # строка с пробелом
                            ("!@#abc", "!@#abc"),                                      # специальные символы в начале не изменяются
                            (None, None),                                              # None
                            ("....abc", "....abc")                                     # точки в начале не изменяются
                        ]
                        )
def negative_test_capitilize(text, result):
    x = StringUtils()
    res = x.capitilize(text)
    assert res == result


"""
2. Юнит-тесты для TRIM: принимает на вход текст и удаляет пробелы в начале, если они есть. Пример: "   skypro" -> "skypro"
"""
@pytest.mark.parametrize("text, result",
                        [
                            (" текст", "текст"),                                       # не пустая строка с 1 пробелом в начале (кирилица)
                            (" text", "text"),                                         # не пустая строка с 1 пробелом в начале (латиница)
                            (" 1. Текст", "1. Текст"),                                 # после пробела текст начинается с цифры
                            ("   ", ""),                                               # строка с пробелами
                            (" ! текст", "! текст"),                                   # после пробела текст начинается со спец символа
                            ("       Текст", "Текст"),                                 # множество пробелов в начале
                            (" Текст. Текст, текст", "Текст. Текст, текст"),           # пробел в начале текста (слова с пробелами между ними)
                            (" текст ", "текст "),                                     # текст заканчиваятся пробелом
                            (" текст   ", "текст   "),                                 # текст заканчиваятся множеством пробелов 
                            ("Текст", "Текст")                                         # текст без пробелов в начале
                        ]
                        )
def positive_test_trim(text, result):
    x = StringUtils()
    res = x.trim(text)
    assert res == result


@pytest.mark.parametrize("text, result",
                        [
                            ("", ""),                                                  # пустая строка
                            ("  Текст", "   Текст"),                                   # начинается с пробела и табуляции
                            (None, None),                                              # None
                        ]
                        )
def negative_test_trim(text, result):
    x = StringUtils()
    res = x.trim(text)
    assert res == result


"""
3. Юнит-тесты для TO_LIST: принимает на вход текст с разделителем и возвращает список строк.
Параметры:
    `string` - строка для обработки
    `delimeter` - разделитель строк. По умолчанию запятая (",")
Пример 1: `to_list("a,b,c,d") -> ["a", "b", "c", "d"]`
Пример 2: `to_list("1:2:3", ":") -> ["1", "2", "3"]`
"""
@pytest.mark.parametrize("lst, result",
                        [
                            ("п.1,п.2,п.3", ["п.1", "п.2", "п.3"])                     # разделитель не задан (проверка настройки delimeter по умолчанию)
                        ]
                        )
def standart_positive_test_to_list(lst, result):
    x = StringUtils()
    res = x.to_list(lst)
    assert res == result


@pytest.mark.parametrize("lst, dlm, result",
                        [
                            ("Сразу...;Потом ;И еще №", ";", ["Сразу...", "Потом ", "И еще №"]),           # задан разделитель (спецсимвол)
                            ("Сразу...;Потом ;И еще п.№", "П", ["Сразу...;", "отом ;И еще п.№"]),          # задан разделитель (заглавная буква)
                            ("Сразу...;пПотом ;И еще п.№", "п", ["Сразу...;", "Потом ;И еще ", ".№"]),     # задан разделитель (маленькая буква)
                            ("ф ф ф", " ", ["ф", "ф", "ф"]),                                               # задан разделитель (пробел)
                            ("1---2---3", "---", ["1", "2", "3"])                                          # множество символов в разделителе
                        ]
                        )
def specific_positive_test_to_list(lst, dlm, result):
    x = StringUtils()
    res = x.to_list(lst, dlm)
    assert res == result


@pytest.mark.parametrize("lst, dlm, result",
                        [
                            ("", ":", []),                                             # нет данных в строке с заданным разделителем
                            (None, "-", None),                                         # None
                            ("1-2-3", None, ["1-2-3"]),                                # delimeter не задан (явно указано = None)
                            ("1,2,3,4", ":", ["1,2,3,4"]),                             # заданный разделитель ниразу не встретился
                            (":::", ":", ["", "", "", ""])                             # строка состоит только из разделителей
                        ]
                        )
def negative_test_to_list(lst, dlm, result):
    x = StringUtils()
    res = x.to_list(lst, dlm)
    assert res == result


"""
4. Юнит-тесты для CONTAINS: возвращает `True`, если строка содержит искомый символ и `False` - если нет
Параметры:
    `string` - строка для обработки
    `symbol` - искомый символ
Пример 1: `contains("SkyPro", "S") -> True`
Пример 2: `contains("SkyPro", "U") -> False`
"""
@pytest.mark.parametrize("text, simbol, result",
                        [
                            ("Текст", "к", True),                                      # содержит (буква), 1 слово, кирилица
                            ("text", "x", True),                                       # содержит (буква), 1 слово, латиница
                            ("Text текст для test", " ", True),                        # содержит (пробел), много слов через пробел
                            ("-Text текст для test", "-", True),                       # содержит (спец символ), много слов со спец символом
                            ("-Text текст для test", "-Text", True),                   # symbol содержит множество символов, много слов со спец символом
                            ("?№!7№%:)(*)", "7", True),                                # содержит (цифра), только спец символы
                            ("Текст", "а", False),                                     # не содержит (буква), 1 слово, кирилица
                            ("text", "g", False),                                      # не содержит (буква), 1 слово, латиница
                            ("TextTекстДляTest", " ", False),                          # не содержит (пробел), много слов
                            ("Text текст для test", "-текст", False),                  # symbol содержит множество символов + спец символ, много слов
                            ("?№!№%:(*", "7", False)                                   # не содержит (цифра), только спец символы
                        ]
                        )
def positive_test_contains(text, simbol, result):
    x = StringUtils()
    res = x.contains(text, simbol)
    assert res == result


@pytest.mark.parametrize("text, simbol, result",
                        [
                            ("Text текст для test", "", False),                        # пусто в параметре "symbol"
                            ("", "", True),                                            # пусто в параметрах "string" и "symbol"
                            (None, "-", None),                                         # None в параметре "string"
                            ("Text текст для test", None, False),                      # None в параметре "symbol"
                            ("  ", ":", False)                                         # строка без символов (пробелы только)
                        ]
                        )
def negative_test_contains(text, simbol, result):
    x = StringUtils()
    res = x.contains(text, simbol)
    assert res == result


"""
5. Юнит-тесты для DELETE_SYMBOL: удаляет все подстроки из переданной строки.
Параметры:
    `string` - строка для обработки
    `symbol` - искомый символ для удаления
Пример 1: `delete_symbol("SkyPro", "k") -> "SyPro"`
Пример 2: `delete_symbol("SkyPro", "Pro") -> "Sky"`
"""
@pytest.mark.parametrize("text_1, text_2, result",
                        [
                            ("Тестирование", "т", "Тесирование"),                      # 1 строчный символ для удаления, 1 слово, кирилица
                            ("Testing", "T", "esting"),                                # 1 заглавный символ для удаления, 1 слово, латиница
                            ("Text текст для test", " ", "Textтекстдляtest"),          # 1 пробел для удаления, много слов через пробел
                            ("Text текст$для test", "$", "Text текстдля test"),        # 1 спец символ для удалений, много слов
                            ("?№!7№%:)(*)", "7", "?№!№%:)(*)"),                        # 1 цифра для удалени, только спец символы
                            ("Тестирование", "ес", "Ттирование"),                      # множество символов для удаления, 1 слово, кирилица
                            ("Testing", "Tes", "ting"),                                # множество символов для удаления, 1 слово, латиница
                            ("Text текст для test", " текст", "Text для test"),        # множество символов с пробелом для удаления, много слов через пробел
                            ("Text текст$для test", "текст$", "Text для test"),        # множество символов со спец символом для удалений, много слов
                            ("?№!7№6%:)(*)", "7№6", "?№!%:)(*)")                       # множество символов с цифрами для удалени, только спец символы
                        ]
                        )
def positive_test_delete_symbol(text_1, text_2, result):
    x = StringUtils()
    res = x.delete_symbol(text_1, text_2)
    assert res == result


@pytest.mark.parametrize("text_1, text_2, result",
                        [
                            ("Text текст для test", "", "Text текст для test"),        # пусто в параметре "symbol"
                            ("", "Test", ""),                                          # пусто в параметре "string"
                            ("", "", ""),                                              # пусто в параметрах "string" и "symbol"
                            (None, "-", None),                                         # None в параметре "string"
                            ("Text текст для test", None, "Text текст для test")       # None в параметре "symbol"
                        ]
                        )
def negative_test_delete_symbol(text_1, text_2, result):
    x = StringUtils()
    res = x.delete_symbol(text_1, text_2)
    assert res == result


"""
6. Юнит-тесты для STARTS_WITH: возвращает `True`, если строка начинается с заданного символа и `False` - если нет
Параметры:
    `string` - строка для обработки
    `symbol` - искомый символ
Пример 1: `starts_with("SkyPro", "S") -> True`
Пример 2: `starts_with("SkyPro", "P") -> False`
"""
@pytest.mark.parametrize("text, simbol, result",
                        [
                            ("Текст", "Т", True),                                      # содержит (буква), 1 слово, кирилица
                            ("text", "t", True),                                       # содержит (буква), 1 слово, латиница
                            (" Text текст для test", " ", True),                       # содержит (пробел), много слов через пробел
                            ("-Text текст для test", "-", True),                       # содержит (спец символ), много слов со спец символом
                            ("-Text текст для test", "-Text", True),                   # symbol содержит множество символов, много слов со спец символом
                            ("7?№!№%:)(*)", "7", True),                                # содержит (цифра), только спец символы
                            ("Текст", "а", False),                                     # не содержит (буква), 1 слово, кирилица
                            ("text", "g", False),                                      # не содержит (буква), 1 слово, латиница
                            ("Text текст для Test", " ", False),                       # не содержит (пробел), много слов
                            ("Text текст для test", "-Text", False),                   # symbol содержит множество символов + спец символ, много слов
                            ("?№!7№%:(*", "7", False)                                  # не содержит (цифра), только спец символы
                        ]
                        )
def positive_test_starts_with(text, simbol, result):
      x = StringUtils()
      res = x.starts_with(text, simbol)
      assert res == result


@pytest.mark.parametrize("text, simbol, result",
                        [
                            ("Text текст для test", "", False),                        # пусто в параметре "symbol"
                            ("", "", True),                                            # пусто в параметрах "string" и "symbol"
                            (None, "-", None),                                         # None в параметре "string"
                            ("Text текст для test", None, "Text текст для test"),      # None в параметре "symbol"
                            ("Text текст для test", "test", False),                    # заканчивается, а не начинается, но в string есть совпадение с symbol
                            ("  ", ":", False)                                         # строка без символов (пробелы только)
                        ]
                        )
def negative_test_starts_with(text, simbol, result):
    x = StringUtils()
    res = x.starts_with(text, simbol)
    assert res == result


"""
7. Юнит-тесты для END_WITH: возвращает `True`, если строка заканчивается заданным символом и `False` - если нет
Параметры:
    `string` - строка для обработки
    `symbol` - искомый символ
Пример 1: `end_with("SkyPro", "o") -> True`
Пример 2: `end_with("SkyPro", "y") -> False`
"""
@pytest.mark.parametrize("text, simbol, result",
                        [
                            ("Текст", "т", True),                                      # содержит (буква), 1 слово, кирилица
                            ("testing", "g", True),                                    # содержит (буква), 1 слово, латиница
                            ("Text текст для test ", " ", True),                       # содержит (пробел), много слов через пробел
                            ("Text текст для test-", "-", True),                       # содержит (спец символ), много слов со спец символом
                            ("Text текст для test-", "test-", True),                   # symbol содержит множество символов, много слов со спец символом
                            ("?№!№%:)(*)7", "7", True),                                # содержит (цифра), только спец символы
                            ("Текст", "а", False),                                     # не содержит (буква), 1 слово, кирилица
                            ("text", "g", False),                                      # не содержит (буква), 1 слово, латиница
                            ("Text текст для Test", " ", False),                       # не содержит (пробел), много слов
                            ("Text текст для test", "-test", False),                   # symbol содержит множество символов + спец символ, много слов
                            ("7?№!7№%:(*", "7", False)                                 # не содержит (цифра), только спец символы
                        ]
                        )
def positive_test_end_with(text, simbol, result):
      x = StringUtils()
      res = x.end_with(text, simbol)
      assert res == result


@pytest.mark.parametrize("text, simbol, result",
                        [
                            ("Text текст для test", "", False),                        # пусто в параметре "symbol"
                            ("", "", True),                                            # пусто в параметрах "string" и "symbol"
                            (None, "-", None),                                         # None в параметре "string"
                            ("Text текст для test", None, "Text текст для test"),      # None в параметре "symbol"
                            ("Text текст для test", "Test", False),                    # начинается, а не заканчивается, но в string есть совпадение с symbol
                            ("  ", ":", False)                                         # строка без символов (пробелы только)
                        ]
                        )
def negative_test_end_with(text, simbol, result):
    x = StringUtils()
    res = x.end_with(text, simbol)
    assert res == result


"""
8. Юнит-тесты для IS_EMPTY: возвращает `True`, если строка пустая и `False` - если нет
Пример 1: `is_empty("") -> True`
Пример 2: `is_empty(" ") -> True`
Пример 3: `is_empty("SkyPro") -> False`
"""
@pytest.mark.parametrize("text, result",
                        [
                            ("", True),                                                # пусто в строке
                            (" ", True),                                               # 1 пробел в строке
                            ("    ", True),                                            # множество пробелов в строке
                            ("а", False),                                              # 1 буква в строке
                            (".", False),                                              # 1 спец символ в строке
                            ("7", False),                                              # 1 цифра в строке
                            ("Тестов 7 для ДЗ№4?", False)                              # множество символов в строке
                        ]
                        )
def positive_test_is_empty(text, result):
    x = StringUtils()
    res = x.is_empty(text)
    assert res == result


@pytest.mark.parametrize("text, result",
                        [
                            (" А", False),                                             # начинается с пробела
                            ("     А", False),                                         # начинается со множества пробелов
                            (None, False)                                              # None в параметре "string"
                        ]
                        )
def negative_test_is_empty(text, result):
    x = StringUtils()
    res = x.is_empty(text)
    assert res == result


"""
9. Юнит-тесты для LIST_TO_STRING: преобразует список элементов в строку с указанным разделителем
Параметры:
    `lst` - список элементов
    `joiner` - разделитель элементов в строке. По умолчанию запятая (", ")
Пример 1: `list_to_string([1,2,3,4]) -> "1, 2, 3, 4"`
Пример 2: `list_to_string(["Sky", "Pro"]) -> "Sky, Pro"`
Пример 3: `list_to_string(["Sky", "Pro"], "-") -> "Sky-Pro"`
"""
@pytest.mark.parametrize("lst, result",
                        [
                            ([1, 2, 3], ("1, 2, 3")),                                  # Numbers: объединяющий элемент не задан (проверка настройки joiner по умолчанию)
                            (["1", "2", "3"], ("1, 2, 3")),                            # Strings: объединяющий элемент не задан (проверка настройки joiner по умолчанию)
                            (["1", 2, "3"], ("1, 2, 3"))                               # Numbers+Strings
                        ]
                        )
def standart_positive_test_list_to_string(lst, result):
    x = StringUtils()
    res = x.list_to_string(lst)
    assert res == result


@pytest.mark.parametrize("lst, join, result",
                        [
                            (["Сразу...", "потом", "и еще №"], " ", "Сразу... потом и еще №"),             # Strings: задан объединяющий элемент (пробел)
                            ([1,2,3], "и", "1и2и3"),                                                       # Numbers: задан объединяющий элемент (буква)
                            ([1,"два",3], "", "1два3"),                                                    # Numbers+Strings: задан объединяющий элемент (пусто)
                            (["One", "Two"], "&", "One&Two"),                                              # задан объединяющий элемент (спецсимвол)
                            (["One", "Two", 3], " and ", "One and Two and 3")                              # множество символов в объединяющем элементе (пробелы + буквы)
                        ]
                        )
def specific_positive_test_list_to_string(lst, join, result):
    x = StringUtils()
    res = x.list_to_string(lst, join)
    assert res == result


@pytest.mark.parametrize("lst, join, result",
                        [
                            ([], ":", ""),                                             # нет данных в строке с заданным объединяющим элементом (спец символ)
                            (None, "-", None),                                         # None
                            ([1, 2, 3], None, "1, 2, 3"),                              # объединяющий элемент не задан (явно указано = None)
                            (["", "", "", ""], ":", ":::"),                            # список состоит из пустых значений
                            ([777], "+", "777")                                        # список состоит из 1 элемента
                        ]
                        )
def negative_test_list_to_string(lst, join, result):
    x = StringUtils()
    res = x.list_to_string(lst, join)
    assert res == result