import re

#1: Palindrom
def is_palindrome(text: str) -> bool:
    cleaned_text = text.replace(" ", "").lower()
    return cleaned_text == cleaned_text[::-1]

#2: Fibonacci
def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Liczba nie może być ujemna")
    if n == 0: return 0
    if n == 1: return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

#3: Liczenie samogłosek
def count_vowels(text: str) -> int:
    vowels = "aeiouyąęó"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

#4: Zniżka
def calculate_discount(price: float, discount: float) -> float:
    if not (0 <= discount <= 1):
        raise ValueError("Zniżka musi być z zakresu 0-1")
    return price * (1 - discount)

#5: Spłaszczanie listy
def flatten_list(nested_list: list) -> list:
    flat = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat

#6: Częstość słów
def word_frequencies(text: str) -> dict:
    text = text.lower()
    words = re.findall(r'\b\w+\b', text)
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

#7: Liczba pierwsza
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
