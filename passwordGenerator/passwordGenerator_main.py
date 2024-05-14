from src import passwordGenerator_functions as passwordGenerator


def main():
    # print instructions
    passwordGenerator.instructions()
    # confirm permissions, 'ok' to acknowledge and continue, 'q' to quit, loop while entry is invalid
    confirmation = input(
        "Please type 'ok' to acknowledge that you have read the instructions and desire to continue, or type 'q' to quit. "
    )
    permission = passwordGenerator.permissions(confirmation)
    while permission is None:
        confirmation = input(
            "Invalid input. Please ensure that your entry contains only 'ok' or 'q'. "
        )
        permission = passwordGenerator.permissions(confirmation)
    if permission is False:
        print("Exiting program.")
        return
    # pick a password length on a scale from 1-4, convert response to integer, loop while entry is invalid
    wordLimit = input(
        "Pick a password length from 1 word to 4 words. "
    )
    wordLimit = passwordGenerator.wordLimitFunction(wordLimit)
    while wordLimit is None:
        wordLimit = input(
            "Invalid input. Please ensure that your entry contains only digits, no words. "
        )
        wordLimit = passwordGenerator.wordLimitFunction(wordLimit)
    # are numbers prohibited? loop while entry is invalid
    # are special characters prohibited? loop while entry is invalid
    # are spaces prohibited? loop while entry is invalid
    limitedFeatures = {}
    limitations = {
        "Are numbers prohibited from being used? (y/n) ": "limitedNumbers",
        "Are special characters prohibited from being used? (y/n) ": "limitedSpecialCharacters",
        "Are spaces prohibited from being used? (y/n) ": "limitedSpaces",
    }
    for limitation, limitedFeature in limitations.items():
        limit = input(limitation)
        evaluation = passwordGenerator.limitFunction(limit)
        while evaluation is None:
            limit = input(
                "Invalid input. Please ensure that your entry contains only 'y' or 'n'. "
            )
        limitedFeatures[limitedFeature] = passwordGenerator.limitFunction(limit)
    # prompt for a word, check the word validity, append word, loop until word limit reached
    wordCount = 0
    password = ""
    prompts = [
        "Word 1 (i.e., something related to your favorite hobby): ",
        "Word 2 (i.e., something related to your favorite song): ",
        "Word 3 (i.e., something related to your favorite book): ",
        "Word 4 (i.e., something related to your favorite athlete): ",
    ]
    for prompt in prompts:
        if wordCount >= wordLimit:
            break
        else:
            word = input(prompt)
            word = passwordGenerator.validifyWord(word)
            while word is None:
                word = input(
                    "Invalid input. Please ensure that your entry is at least 4 letters long. "
                )
                word = passwordGenerator.validifyWord(word)
            password += word
            wordCount += 1
    # encrypt to numbers when allowed, encrypt to special characters when allowed, encrypt to spaces when allowed
    encryptedPassword = passwordGenerator.encryptPassword(password, limitedFeatures)
    # print password
    print(f'Your password is: "{encryptedPassword}".')


if __name__ == "__main__":
    main()
