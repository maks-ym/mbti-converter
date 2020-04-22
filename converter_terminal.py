#!/usr/bin/env python3

import os
import time
from typing import List
import logic as lg


def clear_screen():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def print_explained(func_list: List[str]):
    for c_fun in func_list:
        print(f"[{c_fun.capitalize()}] - {lg.explain_cogn_function(c_fun)}")

def decode_mbti():
    user_input = input("Enter type here: ")
    if not lg.mbti_type_correct(user_input.upper()):
        print("Input error LOOOOL")
    else:
        cogn_functions = lg.mbti2cf(user_input)
        print_explained(cogn_functions)

def print_all_mbti_types():
    print("MBTI types with Cognitive Functions:")
    for mbti_type in lg.generate_all_mbti_types():
        print(f"{mbti_type} | {' '.join(lg.mbti2cf(mbti_type))}")

def print_all_cognitive_functions():
    print("Cognitive Functions:")
    print_explained(lg.POSSIBLE_VALUES)


def do_action(user_input):
    EXIT_FLAG = False
    if user_input not in ['0', '1', '2', '3']:
        print("Incorrect option")
    elif user_input == '0':
        EXIT_FLAG = True
    elif user_input == '1':
        decode_mbti()
    elif user_input == '2':
        print_all_mbti_types()
    elif user_input == '3':
        print_all_cognitive_functions()
    input("\nPress Enter")
    return EXIT_FLAG


def print_menu():
    print(
"""Personality types converter
========================================================================
    1) Decode 4-letter MBTI type
    2) MBTI types with Cognitive Functions
    3) Cognitive Functions list
    0) Quit
""")


def main_loop():
    while(True):
        clear_screen()
        print_menu()
        break_flag = do_action(input("Provide menu number: "))
        if break_flag:
            return


if __name__ == "__main__":
    main_loop()
