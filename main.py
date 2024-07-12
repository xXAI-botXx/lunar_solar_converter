from typing import Union, List
import sys

from lunarcalendar import Converter, Solar, Lunar
import datetime

def check_exit(text_to_check):
    if any([text_to_check.strip().lower() == exit_keyword for exit_keyword in ["q", "quit", "exit"]]):
        print("\nExiting software. Go with the sun and sleep with the moon!")
        sys.exit(0)

def get_input(text_for_user:str, datatype, union=None):
    """
    Gets an input from the user with an specific datatype.

    text_for_user: str
    datatype: any datatype
    union: Union[List[str], None]
    """
    while True:
        user_input = input(text_for_user).strip().lower()

        check_exit(user_input)

        # try to convert
        try:
            result = datatype(user_input)
        except Exception as e:
            print(f"Your input '{user_input}' can not converted to '{datatype}'.")
            if input("Do you want to try again? (yes/no)").strip().lower() == "no":
                continue
            else:
                raise ValueError("Input is wrong.")

        if union is not None:
            if result not in union:
                print(f"Your input '{user_input}' is not in '{union}'")
                if input("Do you want to try again? (yes/no)").strip().lower() == "no":
                    continue
                else:
                    raise ValueError("Input is wrong.")

        return result

def get_a_date():
    """
    Gets a date from the user.

    Returns day, month, year as int
    """
    day = get_input(f"Enter the day: ", int)
    month = get_input(f"Enter the month (as number): ", int)
    year = get_input(f"Enter the year: ", int)
    return day, month, year

def solar_to_lunar():
    print("Enter the Solar date:")
    day, month, year = get_a_date()
    solar_date = Solar(year, month, day)
    lunar_date = Converter.Solar2Lunar(solar_date)
    print(f"The corresponding Lunar date is:\n    - day: {lunar_date.day}\n    - month: {lunar_date.month}\n    - year: {lunar_date.year}\n")

def lunar_to_solar():
    print("Enter the Lunar date:")
    day, month, year = get_a_date()
    lunar_date = Lunar(year, month, day)
    solar_date = Converter.Lunar2Solar(lunar_date)
    print(f"The corresponding Solar date is:\n    - day: {solar_date.day}\n    - month: {solar_date.month}\n    - year: {solar_date.year}\n")

def console_asking():
    print("☀️ Welcome!🌔\nUse this software to convert dates from ☀️ solar calendar to -> 🌔lunar calendar\n and also dates from 🌔lunar calendar to -> ☀️ solar calendar.\n\n")
    while True:
        conversion_type = input("Is your input date Solar (to Lunar) or Lunar (to Solar)? (Enter 'solar' or 'lunar'): ").strip().lower()
        check_exit(conversion_type)
        try:
            if conversion_type == 'solar':
                solar_to_lunar()
            elif conversion_type == 'lunar':
                lunar_to_solar()
            else:
                print("Invalid input. Please enter 'solar' or 'lunar'.")
                continue
        except ValueError:
            print("Restarting...\n")
            continue

        again = input("Do you want to perform another conversion? (yes/no): ").strip().lower()
        if again != 'yes':
            print("\nExiting software. Go with the sun and sleep with the moon!")
            break

if __name__ == "__main__":
    console_asking()

