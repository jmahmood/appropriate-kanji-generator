#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# My wife mentioned the local nonprofit needed something to allow them to generate different kanji docs depending
# on the age of the child.

import logging

from default_kanji_grade import default_kanji_grade

# text = "吾(わが)輩(はい)は猫(ねこ)である。名(な)前(まえ)はまだ無(な)い。"


def find_reading(kanji: str, text_input: str, i: int):
    end_range = i
    for j in range(i, len(text_input)):
        if text_input[j] == ")":
            end_range = j
            break
    try:
        reading, grade_level = (text_input[i + 2:end_range].split("|"))
    except ValueError:
        reading, grade_level = text_input[i + 2:end_range], default_kanji_grade(kanji)
    return reading, int(grade_level), end_range + 1


def basic_text(text_input: str, grade: int) -> str:
    def default_format_fn(reading_level, grade, kanji, hiragana):
        return kanji if reading_level <= grade else hiragana
    return set_appropriate_kanji(text_input, grade, default_format_fn)


def furigana_html(text_input: str, grade: int) -> str:
    def ruby_html_format_fn(reading_level, grade, kanji, hiragana):
        return kanji if reading_level <= grade else "<ruby>{}<rt>{}</rt></ruby>".format(kanji, hiragana)
    return set_appropriate_kanji(text_input, grade, ruby_html_format_fn)


def set_appropriate_kanji(text_input: str, grade: int, format_fn) -> str:
    if grade == "all":
        grade = 100
    ret = ""
    i = 0
    while i < len(text_input):
        next_index = i + 1
        has_more_characters = next_index < len(text_input)
        is_kanji = has_more_characters and text_input[next_index] == "("
        c = text_input[i]

        if is_kanji:
            hiragana, reading_level, next_index = find_reading(c, text_input, i)
            c = format_fn(reading_level, grade, c, hiragana)
        ret += c
        i = next_index
    return ret
#
# print(furigana_html(text, 1))
# print(basic_text(text, 2))
# print(basic_text(text, 3))
# print(basic_text(text, 4))
# print(basic_text(text, 5))
# print(basic_text(text, 6))
# print(basic_text(text, 9))
# print(basic_text(text, "all"))
