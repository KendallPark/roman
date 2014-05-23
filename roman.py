import re

class RomanNumeralConverter:

  roman_to_decimal = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
  decimal_to_roman = { 1: 'I', 100: 'C', 5: 'V', 1000: 'M', 10: 'X', 50: 'L', 500: 'D' }

  @classmethod
  def to_roman(cls, decimal):
    decimal_to_roman = { 1: 'I', 100: 'C', 5: 'V', 1000: 'M', 10: 'X', 50: 'L', 500: 'D' }
    remainder = decimal
    roman_string = ""

    while remainder > 0:
      current_key = 1
      for key in sorted(decimal_to_roman.iterkeys()):
        print remainder, key
        if remainder >= key:
          current_key = key
        else:
          break

      roman_string += decimal_to_roman[current_key]
      remainder -= current_key

      print roman_string

    print "Before: " + roman_string

    roman_string = re.sub(r'CDDDD', 'CD', roman_string)
    roman_string = re.sub(r'CCCC', 'CD', roman_string)
    roman_string = re.sub(r'LXXXX', 'XC', roman_string)
    roman_string = re.sub(r'XXXX', 'XL', roman_string)
    roman_string = re.sub(r'VIIII', 'IX', roman_string)
    roman_string = re.sub(r'IIII', 'IV', roman_string)

    print "AFTER: " + roman_string
    return roman_string

  @classmethod
  def from_roman(cls, roman):
    print 'yo'

