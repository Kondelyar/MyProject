class Calculator:
    def add(self,a,b): # Помилка E231 (немає пробілів після ком)
        return a+b # Помилка E225 (немає пробілів навколо +)
    def divide(self, a, b): # Помилка E302 (має бути 2 порожніх рядки перед методом)
        if b==0: # Помилка E225 (немає пробілів навколо ==)
            raise ValueError('Division by zero!') # Black порадить змінити одинарні лапки на подвійні
        return a/b