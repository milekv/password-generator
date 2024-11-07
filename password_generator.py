import random
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_special=True):
    """
    Funkcja generująca losowe hasło.
    
    Parameters:
    - length (int): Długość hasła.
    - use_upper (bool): Czy w haśle mają występować wielkie litery.
    - use_digits (bool): Czy w haśle mają występować cyfry.
    - use_special (bool): Czy w haśle mają występować znaki specjalne.
    
    Returns:
    - str: Wygenerowane hasło.
    """
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    all_characters = lowercase
    
    if use_upper:
        all_characters += uppercase
    if use_digits:
        all_characters += digits
    if use_special:
        all_characters += special_characters

    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password


def main():
    print("Generator haseł - Wybierz opcje:")
    length = int(input("Podaj długość hasła: "))
    use_upper = input("Czy używać wielkich liter? (tak/nie): ").lower() == 'tak'
    use_digits = input("Czy używać cyfr? (tak/nie): ").lower() == 'tak'
    use_special = input("Czy używać znaków specjalnych? (tak/nie): ").lower() == 'tak'
    
    password = generate_password(length, use_upper, use_digits, use_special)
    
    print("\nWygenerowane hasło:", password)


if __name__ == "__main__":
    main()
