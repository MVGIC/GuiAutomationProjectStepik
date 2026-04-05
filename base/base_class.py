

class Base:
    """Базовый класс, содержащий универсальные методы"""

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        """Метод проверки url"""
        current_url = self.driver.current_url
        print(f"Current url - {current_url}")

    def assert_word(self, word, result):
        """Проверка значения текста"""
        word_value = word.text
        assert word_value == result
        print("Correct word")
