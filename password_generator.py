import random
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_special=True):
   "DODAC OPCJE ZAPISYWANIA HASLA DO DANYCH "
    
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
