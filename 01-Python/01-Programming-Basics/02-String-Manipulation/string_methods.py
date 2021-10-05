# pylint: disable=missing-docstring

# Warning:
# - One line of code for each method
# - Just look in the doc for the right method of the String class!

def add_comma(a_string):
    """
    returns a copy of the string with every word separated by a comma
    example: add_comma("John Peter Jude") => "John, Peter, Jude"
    """
    return a_string.replace(" ", ", ")
    # YOUR CODE HERE

def belongs_to(a_string, a_word):
    """
    returns True if a_string contains a_word
    example: belongs_to("hey jude", "jude") => True
    """
    # YOUR CODE HERE
    return a_word in a_string

def count_repetition(a_string, a_substring):
    """
    returns how many times a_substring occurs in a_string
    example: count_repetition("000123000123", "0") => 6
    """
    # YOUR CODE HERE
    return a_substring.count in a_string

def is_a_question(a_string):
    """
    returns True if a_string ends with a "?"
    example: is_a_question("How are you?") => True
    """
    return a_string.endswith("?")

    # YOUR CODE HERE

def remove_surrounding_whitespaces(a_string):
    """
    returns a copy of the string with leading and trailing whitespaces removed
    example: delete_surrounding_whitespaces("  hey yo  ") => "hey yo"
    """
    return a_string.strip()
    # YOUR CODE HERE

def replace(initial_string, old_letter, new_letter):
    """
    returns a copy of the string with the new letter replacing the old one
    example: replace("casanova", "a", "o") => "cosonovo"
    """
    return initial_string.replace(old_letter, new_letter)
    # YOUR CODE HERE

def full_description_concatenation(first_name, last_name, age):
    """
    returns a sentence with the first_name and the last_name capitalized and
     the age using concatenation
    example: full_description_concatenation("john", "doe", 33) => "John Doe is 33"
    """
    return {first_name.capitalize} + " " + {last_name.capitalize}+" "+ 'is' + {age}
    # YOUR CODE HERE

def full_description_formatting(first_name, last_name, age):
    """
    returns a sentence with the first_name and the last_name capitalized and
     the age using formatting
    example: full_description_formatting("john", "doe", 33) => "John Doe is 33"
    """
    return f'{first_name.capitalize()} {last_name.capitalize()} is {age}'

    # YOUR CODE HERE
