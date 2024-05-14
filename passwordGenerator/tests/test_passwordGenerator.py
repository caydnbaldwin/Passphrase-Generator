from src import passwordGenerator_functions as passwordGenerator


def test_instructions():
    # Test printing instructions
    passwordGenerator.instructions()


def test_permissions():
    # Test permissions function
    assert passwordGenerator.permissions("ok") == True
    assert passwordGenerator.permissions("OK") == True
    assert passwordGenerator.permissions("o") == None
    assert passwordGenerator.permissions("k") == None
    assert passwordGenerator.permissions("q") == False
    assert passwordGenerator.permissions("Q") == False
    assert passwordGenerator.permissions("okq") == None
    assert passwordGenerator.permissions("OKQ") == None
    assert passwordGenerator.permissions("something else") == None


def test_limitFunction():
    # Test limitFunction
    assert passwordGenerator.limitFunction("y") == True
    assert passwordGenerator.limitFunction("Y") == True
    assert passwordGenerator.limitFunction("yes") == None
    assert passwordGenerator.limitFunction("YES") == None
    assert passwordGenerator.limitFunction("n") == False
    assert passwordGenerator.limitFunction("N") == False
    assert passwordGenerator.limitFunction("no") == None
    assert passwordGenerator.limitFunction("NO") == None
    assert passwordGenerator.limitFunction("something else") == None


def test_wordLimitFunction():
    # Test wordLimitFunction
    assert passwordGenerator.wordLimitFunction("0") == None
    assert passwordGenerator.wordLimitFunction("1") == 1
    assert passwordGenerator.wordLimitFunction("2") == 2
    assert passwordGenerator.wordLimitFunction("3") == 3
    assert passwordGenerator.wordLimitFunction("4") == 4
    assert passwordGenerator.wordLimitFunction("5") == None
    assert passwordGenerator.wordLimitFunction("zero") == None
    assert passwordGenerator.wordLimitFunction("one") == None
    assert passwordGenerator.wordLimitFunction("two") == None
    assert passwordGenerator.wordLimitFunction("three") == None
    assert passwordGenerator.wordLimitFunction("four") == None
    assert passwordGenerator.wordLimitFunction("five") == None
    assert passwordGenerator.wordLimitFunction("something else") == None


def test_validifyWord():
    # Test validifyWord
    assert passwordGenerator.validifyWord("I") == None
    assert passwordGenerator.validifyWord("Me") == None
    assert passwordGenerator.validifyWord("You") == None
    assert passwordGenerator.validifyWord("Four") == "Four "
    assert passwordGenerator.validifyWord("four") == "Four "
    assert passwordGenerator.validifyWord("1") == None
    assert passwordGenerator.validifyWord("name") == "Name "
    assert passwordGenerator.validifyWord("n4me") == "N4Me "
    assert passwordGenerator.validifyWord("1234") == "1234 "
    assert passwordGenerator.validifyWord(" word ") == "Word "
    assert passwordGenerator.validifyWord("The Eye of Minds") == "TheEyeOfMinds "


def test_encryptPassword():
    # Test encryptPassword
    limitedFeatures1 = {"limitedNumbers": False, "limitedSpecialCharacters": False, "limitedSpaces": False}
    assert passwordGenerator.encryptPassword("abcdefghijklmnopqrstuvwxyz password", limitedFeatures1) == "@8cd3f9#!jk1mn0pqr$7uvwxyz p@$$w0rd"

    limitedFeatures2 = {"limitedNumbers": True, "limitedSpecialCharacters": False, "limitedSpaces": False}
    assert passwordGenerator.encryptPassword("abcdefghijklmnopqrstuvwxyz password", limitedFeatures2) == "@bcdefg#!jklmnopqr$tuvwxyz p@$$word"

    limitedFeatures3 = {"limitedNumbers": False, "limitedSpecialCharacters": True, "limitedSpaces": False}
    assert passwordGenerator.encryptPassword("abcdefghijklmnopqrstuvwxyz password", limitedFeatures3) == "a8cd3f9hijk1mn0pqrs7uvwxyz passw0rd"

    limitedFeatures4 = {"limitedNumbers": False, "limitedSpecialCharacters": False, "limitedSpaces": True}
    assert passwordGenerator.encryptPassword("abcdefghijklmnopqrstuvwxyz password", limitedFeatures4) == "@8cd3f9#!jk1mn0pqr$7uvwxyzp@$$w0rd"

    limitedFeatures4 = {"limitedNumbers": True, "limitedSpecialCharacters": True, "limitedSpaces": False}
    assert passwordGenerator.encryptPassword("abcdefghijklmnopqrstuvwxyz password", limitedFeatures4) == "abcdefghijklmnopqrstuvwxyz password"

    limitedFeatures4 = {"limitedNumbers": True, "limitedSpecialCharacters": False, "limitedSpaces": True}
    assert passwordGenerator.encryptPassword("abcdefghijklmnopqrstuvwxyz password", limitedFeatures4) == "@bcdefg#!jklmnopqr$tuvwxyzp@$$word"

    limitedFeatures4 = {"limitedNumbers": False, "limitedSpecialCharacters": True, "limitedSpaces": True}
    assert passwordGenerator.encryptPassword("abcdefghijklmnopqrstuvwxyz password", limitedFeatures4) == "a8cd3f9hijk1mn0pqrs7uvwxyzpassw0rd"

    limitedFeatures4 = {"limitedNumbers": True, "limitedSpecialCharacters": True, "limitedSpaces": True}
    assert passwordGenerator.encryptPassword("abcdefghijklmnopqrstuvwxyz password", limitedFeatures4) == "abcdefghijklmnopqrstuvwxyzpassword"


if __name__ == "__main__":
    test_instructions()
    test_permissions()
    test_limitFunction()
    test_wordLimitFunction()
    test_validifyWord()
    test_encryptPassword()
    print("All tests passed successfully!")
