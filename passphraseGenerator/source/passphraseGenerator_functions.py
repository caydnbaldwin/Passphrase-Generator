def instructions():
    # print instructions
    print(
        "\nWrite one word per prompt that represents a subject that is significant to you.\n"
        "\n"
        "Once all prompts are answered, a passphrase will be generated for you.\n"
        "\n"
        "Disclaimer: Word inputs and password outputs are NOT stored or recorded.\n"
    )


def permissions(confirmation):
    # confirm permissions, 'ok' to acknowledge and continue, 'q' to quit, loop while entry is invalid
    confirmation = confirmation.strip().lower()
    if confirmation == "":
        return True
    elif confirmation == "q":
        return False
    else:
        return None


def limitFunction(limit):
    # are numbers prohibited? loop while entry is invalid
    # are special characters prohibited? loop while entry is invalid
    # are spaces prohibited? loop while entry is invalid
    limit = limit.strip().lower()
    if limit == "y":
        return True
    elif limit == "n":
        return False
    else:
        return None


def wordLimitFunction(wordLimit):
    # what is the maximum length? loop while entry is invalid
    wordLimit = wordLimit.strip()
    if wordLimit.isdigit() and int(wordLimit) >= 1 and int(wordLimit) <= 4:
        return int(wordLimit)
    else:
        return None


def validifyWord(word):
    if len(word) < 4:
        return None
    else:
        return word.lower().title().strip().replace(" ", "") + " "


def encryptPassword(password, limitedFeatures):
    # encrypt to numbers when allowed
    if limitedFeatures["limitedNumbers"] == False:
        password = (
            password.replace("b", "8")
            .replace("e", "3")
            .replace("g", "9")
            .replace("l", "1")
            .replace("o", "0")
            .replace("t", "7")
            .replace("B", "8")
            .replace("E", "3")
            .replace("G", "9")
            .replace("L", "1")
            .replace("O", "0")
            .replace("T", "7")
        )
    # encrypt to special characters when allowed
    if limitedFeatures["limitedSpecialCharacters"] == False:
        password = (
            password.replace("a", "@")
            .replace("h", "#")
            .replace("i", "!")
            .replace("s", "$")
            .replace("A", "@")
            .replace("H", "#")
            .replace("I", "!")
            .replace("S", "$")
        )
    # encrypt to spaces when allowed
    if limitedFeatures["limitedSpaces"] == True:
        password = password.replace(" ", "")
    return password
