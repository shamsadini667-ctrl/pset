def playback():
    user_input = str(input("enter your input:"))
    user_input = user_input.replace(" ", "...")

    return user_input

text = playback()
print(text)