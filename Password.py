password_length = 12
        characters = string.ascii_letters + string.digits
        password = ""
        for index in range(password_length):
            password = password + random.choice(characters)
        return password