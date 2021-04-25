import re
import sys

class MagicString:
    def __init__(self, text):
        self.__MagicString = text

    def removeVowels(self):
        self.__MagicString = re.sub(r'[aeiyouAEIYOU]', "", self.__MagicString)

    def doubleConsonants(self):
        self.__MagicString = re.sub(r'([^aeiyouAEIYOU])', r'\1\1', self.__MagicString)

    def aspirate(self):
        self.__MagicString = re.sub(r'([aeiyouAEIYOU])', r'h\1', self.__MagicString)

    def get(self):
        return self.__MagicString


def test(did_pass):
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def test_suite():
    string = MagicString("ahoj")
    test(string.get() == "ahoj")
    string.doubleConsonants()
    test(string.get() == "ahhojj")
    string.aspirate()
    test(string.get() == "hahhhojj")
    string.removeVowels()
    test(string.get() == "hhhhjj")
    string.doubleConsonants()
    test(string.get() == "hhhhhhhhjjjj")
    
    string = MagicString("kytka")
    string.doubleConsonants()
    test(string.get() == "kkyttkka")
    string.removeVowels()
    test(string.get() == "kkttkk")
    string.aspirate()
    test(string.get() == "kkttkk")

    string = MagicString("popokatepetl")
    string.aspirate()
    test(string.get() == "phophokhathephetl")
    string.doubleConsonants()
    test(string.get() == "pphhopphhokkhhatthhepphhettll")
    string.removeVowels()
    test(string.get() == "pphhpphhkkhhtthhpphhttll")

    string = MagicString("vlak")
    string.aspirate()
    test(string.get() == "vlhak")
    string.removeVowels()
    test(string.get() == "vlhk")
    string.doubleConsonants()
    test(string.get() == "vvllhhkk")

    string = MagicString("aaaeeeiiiooo")
    string.removeVowels()
    test(string.get() == "")

    string = MagicString("ale")
    string.aspirate()
    test(string.get() == "halhe")
    string.removeVowels()
    test(string.get() == "hlh")

    string = MagicString("vlk")
    string.removeVowels()
    test(string.get() == "vlk")
    string.doubleConsonants()
    test(string.get() == "vvllkk")


test_suite()
