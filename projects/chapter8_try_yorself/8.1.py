
"""
8-1. Message: Write a function called display_message() that prints one sentence telling everyone what you are learning
about in this chapter. Call the function, and make sure the message displays correctly.
"""

def display_message(chapter):
    """
    This function tells what I am learning about in this chapter.
    :return:
    """
    if chapter == 1:
        print(f"In Chapter {chapter} of Python Crash Course I learned about the basics of the Python language.")
    elif chapter == 2:
        print(f"In Chapter {chapter} of Python Crash Course I learned about variable and simple data types.")
    elif chapter == 3:
        print(f"In Chapter {chapter} of Python Crash Course I learned about lists.")
    elif chapter == 4:
        print(f"In Chapter {chapter} of Python Crash Course I learned about working with functions.")
    elif chapter == 5:
        print(f"In Chapter {chapter} of Python Crash Course I learned about if statements.")
    elif chapter == 6:
        print(f"In Chapter {chapter} of Python Crash Course I learned about dictionaries.")
    elif chapter == 7:
        print(f"In Chapter {chapter} of Python Crash Course I learned about user input and while loops.")
    elif chapter == 8:
        print("In Chapter 8 of Python Crash Course I am learning about functions.")


display_message(8)

