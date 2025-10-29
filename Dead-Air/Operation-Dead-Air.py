channel = 0
data: List[str] = []  # Variable Declarations
newWord = ""
found = ""
# ONLY WORKS ON MAKECODE MICRO:BIT
def on_forever(): # Radio Scanning
    global channel
    radio.set_group(channel)
    channel += 1
    if channel > 255:
        channel = 0
    basic.pause(1500)
    print(channel)
basic.forever(on_forever)

def on_received_string(receivedString):
    global data
    global newWord
    newWord = ""
    found = receivedString
    matches = 0
    if receivedString not in data:
        data.append(receivedString) # Checks to see if you already have found it and if not it marks it as found
        for i in range(0, len(found)):  # Decodes Encrypted Message
            character = found[i]
            if character.charCodeAt(0) >= 97 and character.charCodeAt(0) <= 122:
                ASCIIValue = character.charCodeAt(0)
                newRangeValue = ASCIIValue - 97
                introduceShift = newRangeValue + 13
                solveWrapAround = (introduceShift % 26)
                newASCIIValue = solveWrapAround + 97
                decodedCharacter = String.from_char_code(newASCIIValue)
                newWord = newWord + decodedCharacter
            else:
                newWord = newWord + character
        print("Encoded Word: " + found)
        print("Decoded Word: " + newWord)
        basic.show_string(newWord)
    else:
        print("Already Found!")
        basic.show_icon(IconNames.NO)
radio.on_received_string(on_received_string)
