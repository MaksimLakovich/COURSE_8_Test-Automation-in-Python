# Bug 1: При использовании функции CAPITILIZE после первой буквы в ПРЕДЛОЖЕНИИ автоматически становятся прописными и все последующие буквы данного предложения, а не только первая.

**1. Описание:**  
Согласно описания функции capitilize в файле "string_utils.py", данная функция принимает на вход текст, делает первую букву заглавной и возвращает этот же текст. Т.е. явно зафиксировано "ПЕРВУЮ БУКВУ" и ничего не сказано про все последующие, а следовательно остальной текст не должен менятся, так как данное редактирование может привести к ошибкам в Именах, Названиях или отображению нового предложения после точки.
  
**2. Ожидаемый результат:**  
Менятся только первая буква в String --> ("тест Ивана", "Тест Ивана").
  
**3. Фактический результат:**  
Меняется первая буква на заглавную, но и все последующие становятся прописными.
  
### Фрагмент ошибки:
E       AssertionError: assert 'Тест ивана' == 'Тест Ивана'  
E         - Тест Ивана    
E         + Тест ивана

### Фрагмент кода:
```python
@pytest.mark.parametrize("text, result",
                        [
                            ("тест Ивана", "Тест Ивана")
                        ]
                        )
def positive_test_capitilize(text, result):
    x = StringUtils()
    res = x.capitilize(text)
    assert res == result
```


---


# Bug 2: При использовании функции CAPITILIZE после первой буквы в СЛОВЕ автоматически становятся прописными все последующие буквы данного слова, а не только первая.

**1. Описание:**  
Согласно описания функции capitilize в файле "string_utils.py", данная функция принимает на вход текст, делает первую букву заглавной и возвращает этот же текст. Т.е. явно зафиксировано "ПЕРВУЮ БУКВУ" и ничего не сказано про все последующие, а следовательно последующие не должны меняться.
  
**2. Ожидаемый результат:**  
В данном тесте первая буква уже была заглавная (как и остальные). Поэтому ожидалось, что первая буква так и останется заглавной какой и была, а все последующие останутся без изменения  -->  ("ТЕСТ", "ТЕСТ").
  
**3. Фактический результат:**  
Первая буква осталась заглавной, но автоматически прописными стали все последующие.
  
### Фрагмент ошибки:
E       AssertionError: assert 'Тест' == 'ТЕСТ'  
E         - ТЕСТ  
E         + Тест  

### Фрагмент кода:
```python
@pytest.mark.parametrize("text, result",
                        [
                            ("ТЕСТ", "ТЕСТ")
                        ]
                        )
def positive_test_capitilize(text, result):
    x = StringUtils()
    res = x.capitilize(text)
    assert res == result
```


---


# Bug 3: При использовании функции CAPITILIZE первая буква не становится заглавной, если перед ней стоит пробел/спец.символ.

**1. Описание:**  
Согласно описания функции capitilize в файле "string_utils.py", данная функция принимает на вход текст, делает первую букву заглавной и возвращает этот же текст. Т.е. явно зафиксировано "БУКВУ" и можно сделать вывод, что если первым встречается спец символ, цифра или пробел, то функция должна перейти к порядковому номер 2, потом 3 и т.д., пока не будет найдена "ПЕРВАЯ БУКВА".
  
**2. Ожидаемый результат:**  
Менятся только первая буква в String --> (" описание", " Описание").
  
**3. Фактический результат:**  
Первая буква не меняется. Функция смотрит только на первый порядковый номер и если это не буква, а например пробел, то дальше поиск первой буквы не выполняется.
  
### Фрагмент ошибки:
E       AssertionError: assert ' описание' == ' Описание'  
E         -  Описание  
E         +  описание  

### Фрагмент кода:
```python
@pytest.mark.parametrize("text, result",
                        [
                            (" описание", " Описание")
                        ]
                        )
def positive_test_capitilize(text, result):
    x = StringUtils()
    res = x.capitilize(text)
    assert res == result
```


---


# Bug 4: Функция CAPITILIZE не обрабатывает случай, когда входное значение = None (ошибка AttributeError).

**1. Описание:**  
Использование None в @pytest.mark.parametrize для тестирования негативных сценариев — это правильный подход. Таким образом, мы должны проверить, как функция реагирует на недопустимые входные данные.
  
**2. Ожидаемый результат:**  
Функция обрабатывает кейсы с данными = None.
  
**3. Фактический результат:**  
Функция не обрабатывает случай, когда входной строкой является None.
  
### Фрагмент ошибки:
AttributeError: 'NoneType' object has no attribute 'capitalize' 

### Фрагмент кода:
```python
@pytest.mark.parametrize("text, result",
                        [
                            (None, None)
                        ]
                        )
def negative_test_capitilize(text, result):
    x = StringUtils()
    res = x.capitilize(text)
    assert res == result
```


---


# Bug 5: Функция TRIM не обрабатывает табуляцию.

**1. Описание:**  
Функция принимает на вход текст и удаляет пробелы в начале, если они есть. Ожидаемо, что табуляцию (для текста это равносильно пробелам) данна функция также должна отрабатывать
  
**2. Ожидаемый результат:**  
Функия удаляет стандартные пробелы и пробелы созданные табуляцией в начале текста.
  
**3. Фактический результат:**  
Функция не удаляет табуляцию в начале текста.
  
### Фрагмент ошибки:
E       AssertionError: assert 'Текст' == '   Текст'  
E         -    Текст  
E         + Текст   

### Фрагмент кода:
```python
@pytest.mark.parametrize("text, result",
                        [
                            ("  Текст", "   Текст")
                        ]
                        )
def negative_test_trim(text, result):
    x = StringUtils()
    res = x.trim(text)
    assert res == result
```


---


# Bug 6: Функция TRIM не обрабатывает случай, когда входное значение = None (ошибка AttributeError).

**1. Описание:**  
Использование None в @pytest.mark.parametrize для тестирования негативных сценариев — это правильный подход. Таким образом, мы должны проверить, как функция реагирует на недопустимые входные данные.
  
**2. Ожидаемый результат:**  
Функция обрабатывает кейсы с данными = None.
  
**3. Фактический результат:**  
Функция не обрабатывает случай, когда входной строкой является None.
  
### Фрагмент ошибки:
AttributeError: 'NoneType' object has no attribute 'startswith' 

### Фрагмент кода:
```python
@pytest.mark.parametrize("text, result",
                        [
                            (None, None)
                        ]
                        )
def negative_test_trim(text, result):
    x = StringUtils()
    res = x.trim(text)
    assert res == result
```


---


# Bug 7: Функция TO_LIST не обрабатывает случай, когда входное значение = None (ошибка AttributeError).

**1. Описание:**  
Использование None в @pytest.mark.parametrize для тестирования негативных сценариев — это правильный подход. Таким образом, мы должны проверить, как функция реагирует на недопустимые входные данные.
  
**2. Ожидаемый результат:**  
Функция обрабатывает кейсы с данными = None.
  
**3. Фактический результат:**  
Функция не обрабатывает случай, когда входной строкой является None.
  
### Фрагмент ошибки:
AttributeError: 'NoneType' object has no attribute 'startswith'  

### Фрагмент кода:
```python
@pytest.mark.parametrize("lst, dlm, result",
                        [
                            (None, "-", None)
                        ]
                        )
def negative_test_to_list(lst, dlm, result):
    x = StringUtils()
    res = x.to_list(lst, dlm)
    assert res == result
```


---


# Bug 8: Функция CONTAINS не возвращает False если "symbol" = "пусто", но при этом "string" заполнено данными.

**1. Описание:**  
Если заполнить параметр "string" данными, но "symbol" оставить "пусто", то функция не возвращает ничего - ни `True`, ни `False`.
  
**2. Ожидаемый результат:**  
Функция с заполненым параметром "string" должна проверить, что параметр не равно пусто (symbol = пусто, т.е. мы явно проверяем string пустов или нет).
  
**3. Фактический результат:**  
Фунция возвращает ошибку с "symbol = пусто".
  
### Фрагмент ошибки:
 assert True == False 

### Фрагмент кода:
```python
@pytest.mark.parametrize("text, simbol, result",
                        [
                            ("Text текст для test", "", False)
                        ]
                        )
def negative_test_contains(text, simbol, result):
    x = StringUtils()
    res = x.contains(text, simbol)
    assert res == result
```


---


# Bug 9: Функция CONTAINS не обрабатывает случай, когда входное значение = None в параметре "string" (ошибка AttributeError).

**1. Описание:**  
Использование None в @pytest.mark.parametrize для тестирования негативных сценариев — это правильный подход. Таким образом, мы должны проверить, как функция реагирует на недопустимые входные данные.
  
**2. Ожидаемый результат:**  
Функция обрабатывает кейсы с данными в параметре "string" = None.
  
**3. Фактический результат:**  
Функция не обрабатывает случай, когда входной строкой в параметре "string" является None.
  
### Фрагмент ошибки:
 AttributeError: 'NoneType' object has no attribute 'index' 

### Фрагмент кода:
```python
@pytest.mark.parametrize("text, simbol, result",
                        [
                            (None, "-", None)
                        ]
                        )
def negative_test_contains(text, simbol, result):
    x = StringUtils()
    res = x.contains(text, simbol)
    assert res == result
```


---


# Bug 10: Функция CONTAINS не обрабатывает случай, когда входное значение = None в параметре "symbol" (ошибка TypeError).

**1. Описание:**  
Использование None в @pytest.mark.parametrize для тестирования негативных сценариев — это правильный подход. Таким образом, мы должны проверить, как функция реагирует на недопустимые входные данные.
  
**2. Ожидаемый результат:**  
Функция обрабатывает кейсы с данными в параметре "symbol" = None.
  
**3. Фактический результат:**  
Функция не обрабатывает случай, когда входной строкой является None в параметре "symbol".
  
### Фрагмент ошибки:
TypeError: must be str, not NoneType 

### Фрагмент кода:
```python
@pytest.mark.parametrize("text, simbol, result",
                        [
                            ("Text текст для test", None, False)
                        ]
                        )
def negative_test_contains(text, simbol, result):
    x = StringUtils()
    res = x.contains(text, simbol)
    assert res == result
```


---


# Bug 11: Функция DELETE_SYMBOL не обрабатывает случай, когда входное значение = None в параметре "string" (ошибка AttributeError).

**1. Описание:**  
Использование None в @pytest.mark.parametrize для тестирования негативных сценариев — это правильный подход. Таким образом, мы должны проверить, как функция реагирует на недопустимые входные данные.
  
**2. Ожидаемый результат:**  
Функция обрабатывает кейсы с данными в параметре "string" = None.
  
**3. Фактический результат:**  
Функция не обрабатывает случай, когда входной строкой в параметре "string" является None.
  
### Фрагмент ошибки:
 AttributeError: 'NoneType' object has no attribute 'index' 

### Фрагмент кода:
```python
@pytest.mark.parametrize("text_1, text_2, result",
                        [
                            (None, "-", None)
                        ]
                        )
def negative_test_delete_symbol(text_1, text_2, result):
    x = StringUtils()
    res = x.delete_symbol(text_1, text_2)
    assert res == result
```


---


# Bug 12: Функция DELETE_SYMBOL не обрабатывает случай, когда входное значение = None в параметре "symbol" (ошибка TypeError).

**1. Описание:**  
Использование None в @pytest.mark.parametrize для тестирования негативных сценариев — это правильный подход. Таким образом, мы должны проверить, как функция реагирует на недопустимые входные данные.
  
**2. Ожидаемый результат:**  
Функция обрабатывает кейсы с данными в параметре "symbol" = None.
  
**3. Фактический результат:**  
Функция не обрабатывает случай, когда входной строкой является None в параметре "symbol".
  
### Фрагмент ошибки:
TypeError: must be str, not NoneType 

### Фрагмент кода:
```python
@pytest.mark.parametrize("text_1, text_2, result",
                        [
                            ("Text текст для test", None, "Text текст для test")
                        ]
                        )
def negative_test_delete_symbol(text_1, text_2, result):
    x = StringUtils()
    res = x.delete_symbol(text_1, text_2)
    assert res == result
```


---


# Bug 13: Функция STARTS_WITH не возвращает False если "symbol" = "пусто", но при этом "string" заполнено данными.

**1. Описание:**  
Если заполнить параметр "string" данными, но "symbol" оставить "пусто", то функция не возвращает ничего - ни `True`, ни `False`.
  
**2. Ожидаемый результат:**  
Функция с заполненым параметром "string" должна проверить, что параметр не начинается с ПУСТО  (symbol = пусто, т.е. мы явно проверяем string начинается с пусто или нет).
  
**3. Фактический результат:**  
Фунция возвращает ошибку с "symbol = пусто".
  
### Фрагмент ошибки:
assert True == False 

### Фрагмент кода:
```python
@pytest.mark.parametrize("text, simbol, result",
                        [
                            ("Text текст для test", "", False)
                        ]
                        )
def negative_test_starts_with(text, simbol, result):
    x = StringUtils()
    res = x.starts_with(text, simbol)
    assert res == result
```


---


# Bug 14: Функция STARTS_WITH не обрабатывает случай, когда входное значение = None в параметре "string" (ошибка AttributeError).

**1. Описание:**  
Использование None в @pytest.mark.parametrize для тестирования негативных сценариев — это правильный подход. Таким образом, мы должны проверить, как функция реагирует на недопустимые входные данные.
  
**2. Ожидаемый результат:**  
Функция обрабатывает кейсы с данными в параметре "string" = None.
  
**3. Фактический результат:**  
Функция не обрабатывает случай, когда входной строкой в параметре "string" является None.
  
### Фрагмент ошибки:
AttributeError: 'NoneType' object has no attribute 'startswith' 

### Фрагмент кода:
```python
@pytest.mark.parametrize("text, simbol, result",
                        [
                            (None, "-", None)
                        ]
                        )
def negative_test_starts_with(text, simbol, result):
    x = StringUtils()
    res = x.starts_with(text, simbol)
    assert res == result
```


---


# Bug 15: Функция STARTS_WITH не обрабатывает случай, когда входное значение = None в параметре "symbol" (ошибка TypeError).

**1. Описание:**  
Использование None в @pytest.mark.parametrize для тестирования негативных сценариев — это правильный подход. Таким образом, мы должны проверить, как функция реагирует на недопустимые входные данные.
  
**2. Ожидаемый результат:**  
Функция обрабатывает кейсы с данными в параметре "symbol" = None.
  
**3. Фактический результат:**  
Функция не обрабатывает случай, когда входной строкой является None в параметре "symbol".
  
### Фрагмент ошибки:
TypeError: startswith first arg must be str or a tuple of str, not NoneType 

### Фрагмент кода:
```python
@pytest.mark.parametrize("text, simbol, result",
                        [
                            ("Text текст для test", None, "Text текст для test")
                        ]
                        )
def negative_test_starts_with(text, simbol, result):
    x = StringUtils()
    res = x.starts_with(text, simbol)
    assert res == result
```


---


# Bug 16: Функция END_WITH не возвращает False если "symbol" = "пусто", но при этом "string" заполнено данными.

**1. Описание:**  
Если заполнить параметр "string" данными, но "symbol" оставить "пусто", то функция не возвращает ничего - ни `True`, ни `False`.
  
**2. Ожидаемый результат:**  
Функция с заполненым параметром "string" должна проверить, что параметр не начинается с ПУСТО  (symbol = пусто, т.е. мы явно проверяем string начинается с пусто или нет).
  
**3. Фактический результат:**  
Фунция возвращает ошибку с "symbol = пусто".
  
### Фрагмент ошибки:
assert True == False 

### Фрагмент кода:
```python
@pytest.mark.parametrize("text, simbol, result",
                        [
                            ("Text текст для test", "", False)
                        ]
                        )
def negative_test_end_with(text, simbol, result):
    x = StringUtils()
    res = x.end_with(text, simbol)
    assert res == result
```


---


# Bug 17: Функция END_WITH не обрабатывает случай, когда входное значение = None в параметре "string" (ошибка AttributeError).

**1. Описание:**  
Использование None в @pytest.mark.parametrize для тестирования негативных сценариев — это правильный подход. Таким образом, мы должны проверить, как функция реагирует на недопустимые входные данные.
  
**2. Ожидаемый результат:**  
Функция обрабатывает кейсы с данными в параметре "string" = None.
  
**3. Фактический результат:**  
Функция не обрабатывает случай, когда входной строкой в параметре "string" является None.
  
### Фрагмент ошибки:
AttributeError: 'NoneType' object has no attribute 'endswith' 

### Фрагмент кода:
```python
@pytest.mark.parametrize("text, simbol, result",
                        [
                            (None, "-", None)
                        ]
                        )
def negative_test_end_with(text, simbol, result):
    x = StringUtils()
    res = x.end_with(text, simbol)
    assert res == result
```


---


# Bug 18: Функция END_WITH не обрабатывает случай, когда входное значение = None в параметре "symbol" (ошибка TypeError).

**1. Описание:**  
Использование None в @pytest.mark.parametrize для тестирования негативных сценариев — это правильный подход. Таким образом, мы должны проверить, как функция реагирует на недопустимые входные данные.
  
**2. Ожидаемый результат:**  
Функция обрабатывает кейсы с данными в параметре "symbol" = None.
  
**3. Фактический результат:**  
Функция не обрабатывает случай, когда входной строкой является None в параметре "symbol".
  
### Фрагмент ошибки:
TypeError: endswith first arg must be str or a tuple of str, not NoneType 

### Фрагмент кода:
```python
@pytest.mark.parametrize("text, simbol, result",
                        [
                            ("Text текст для test", None, "Text текст для test")
                        ]
                        )
def negative_test_end_with(text, simbol, result):
    x = StringUtils()
    res = x.end_with(text, simbol)
    assert res == result
```


---


# Bug 19: Функция IS_EMPTY не обрабатывает случай, когда входное значение = None в параметре "string" (ошибка AttributeError).

**1. Описание:**  
Использование None в @pytest.mark.parametrize для тестирования негативных сценариев — это правильный подход. Таким образом, мы должны проверить, как функция реагирует на недопустимые входные данные.
  
**2. Ожидаемый результат:**  
Функция обрабатывает кейсы с данными в параметре "string" = None.
  
**3. Фактический результат:**  
Функция не обрабатывает случай, когда входной строкой в параметре "string" является None.
  
### Фрагмент ошибки:
AttributeError: 'NoneType' object has no attribute 'endswith'  

### Фрагмент кода:
```python
@pytest.mark.parametrize("text, result",
                        [
                            (None, False)
                        ]
                        )
def negative_test_is_empty(text, result):
    x = StringUtils()
    res = x.is_empty(text)
    assert res == result
```


---


# Bug 20: Функция LIST_TO_STRING не обрабатывает случай, когда входное в LIST = None (ошибка TypeError).

**1. Описание:**  
Использование None в @pytest.mark.parametrize для тестирования негативных сценариев — это правильный подход. Таким образом, мы должны проверить, как функция реагирует на недопустимые входные данные.
  
**2. Ожидаемый результат:**  
Функция обрабатывает кейсы с данными, когда в параметр "list" поступает "None".
  
**3. Фактический результат:**  
Функция не обрабатывает случай, когда входным значением в параметр "list" поступает "None".
  
### Фрагмент ошибки:
TypeError: object of type 'NoneType' has no len() 

### Фрагмент кода:
```python
@pytest.mark.parametrize("lst, join, result",
                        [
                            (None, "-", None)
                        ]
                        )
def negative_test_list_to_string(lst, join, result):
    x = StringUtils()
    res = x.list_to_string(lst, join)
    assert res == result
```


---


# Bug 21: Функция LIST_TO_STRING не обрабатывает случай, когда объединяющий элемент JOINT = None (ошибка TypeError).

**1. Описание:**  
Использование None в @pytest.mark.parametrize для тестирования негативных сценариев — это правильный подход. Таким образом, мы должны проверить, как функция реагирует на недопустимые входные данные.
  
**2. Ожидаемый результат:**  
Функция обрабатывает кейсы с данными, когда в параметр "joint" поступает "None" и применяет объединяющий элемент заданный по умолчанию в функции (равен 'запятой').
  
**3. Фактический результат:**  
Функция не обрабатывает случай, когда входным значением объединяющего элемента в параметре "joint" является "None".
  
### Фрагмент ошибки:
TypeError: can only concatenate str (not "NoneType") to str 

### Фрагмент кода:
```python
@pytest.mark.parametrize("lst, join, result",
                        [
                            ([1, 2, 3], None, "1, 2, 3")
                        ]
                        )
def negative_test_list_to_string(lst, join, result):
    x = StringUtils()
    res = x.list_to_string(lst, join)
    assert res == result
```


---
