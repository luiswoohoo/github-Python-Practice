# Define custom exception
class StudentInfoError(Exception):
    def __init__(self, message):
        self.message = message  # Initialize the exception message


def find_ID(name, info):
    if name not in info:
        raise StudentInfoError('Student ID not found for {}'.format(name))
    id = info[name]
    return id


def find_name(ID, info):
    if ID not in info.values():
        raise StudentInfoError('Student name not found for {}'.format(ID))

    for key, value in info.items():
        if ID == value:
            return key


if __name__ == '__main__':
    # Dictionary of student names and IDs
    student_info = {
        'Reagan': 'rebradshaw835',
        'Ryley': 'rbarber894',
        'Peyton': 'pstott885',
        'Tyrese': 'tmayo945',
        'Caius': 'ccharlton329'
    }

    userChoice = input()  # Read search option from user. 0: find_ID(), 1: find_name()

    # FIXME: find_ID() and find_name() may throw an Exception.
    #        Insert a try/except statement to catch the exception and output any exception message.
    try:
        if userChoice == "0":
            name = input()
            result = find_ID(name, student_info)
        else:
            ID = input()
            result = find_name(ID, student_info)
        print(result)

    except StudentInfoError as exception:
        print(exception)
