class StringManipulator:
    def getString(self):
        self.s = input("Enter a string: ")

    def printString(self):
        print(self.s.upper())

# Example
string_obj = StringManipulator()
string_obj.getString()
string_obj.printString()