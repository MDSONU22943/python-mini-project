from src.pass_gen import password_generator


if __name__ == "__main__":
    print(password_generator(min_length=8,number=False,special_character=False))