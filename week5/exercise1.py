# -*- coding: UTF-8 -*-
"""Refactoring.

This excercise is very similar to week 2, exercise 2. It contains a complete
and working example, but it's very poorly written.

Your job is to go through it and make it as good as you can.

That means making it self-documenting wherever possible, adding comments where
it isn't. Take repeated code and make it into a function. Also use functions
to encapsulate concepts. If something is done many times, maybe a map or a loop
is called for. Etc.

The resulting file should feel as close to english as possible.
It must also pass the linter.

This is the first file that will be run against the pydocstyle checker. If
you've run the week5_system_prep.sh file you should be getting blue linter dots
that show you where lintere errors are. If they aren't working, you should be
getting the errors in the test output.

Some functions will have directions as external comments, once you think you
are on top of it, take these comments out. Others won't have comments and
you'll need to figure out for yourself what to do.
"""

from __future__ import division
from __future__ import print_function
# It should say something different in the last message.


def countdown(message, start, stop, completion_message):
    """Printer coundown message."""
    cntdwn_list = []
    if start > stop:
        step = -1
    elif start == stop:
        return(completion_message)
    else:
        step = 1
    for i in range(start, stop, step):
        cntdwn_list.append(message + " {}".format(i))
    cntdwn_list.append(completion_message)
    return(cntdwn_list)


# TRIANGLES

# This should be a series of functions that are ultimatly used by
# triangle_master
# It should eventually return a dictionary of triangle facts. It should
# optionally print information as a nicely formatted string. Make printing
# turned off by default but turned on with an optional argument.
# The stub functions are made for you, and each one is tested, so this should
# hand hold quite nicely.
def calculate_hypotenuse(base, height):
    """Calculator hypothenuse by using the math fomula."""
    hypotenuse = math.sqrt(base**2 + height**2)
    return(hypotenuse)


def calculate_area(base, height):
    """Calculator area by using the formula."""
    area = (base*height)/2
    return area


def calculate_perimeter(base, height):
    """Calculator perimeter."""
    perimeter = base + height + calculate_hypotenuse(base, height)
    return perimeter


def calculate_aspect(base, height):
    """Calculator aspect."""
    if height > base:
        return "tall"
    elif height == base:
        return "equal"
    else:
        return "wide"


# Make sure you reuse the functions you've already got
# Don't reinvent the wheel
def get_triangle_facts(base, height, units="mm"):
    """Helper Triangle facts."""
    return {"area": calculate_area(base, height),
            "perimeter": calculate_perimeter(base, height),
            "height": height,
            "base": base,
            "hypotenuse": calculate_hypotenuse(base, height),
            "aspect": calculate_aspect(base, height),
            "units": units}


# this should return a multi line string that looks a bit like this:
#
# 15
# |
# |     |\
# |____>| \  17.0
#       |  \
#       |   \
#       ------
#       8
# This triangle is 60.0mm²
# It has a perimeter of 40.0mm
# This is a tall triangle.
#
# but with the values and shape that relate to the specific
# triangle we care about.
def tell_me_about_this_right_triangle(facts_dictionary):
    """Return a dictionary used for facts."""
    tall = """
            {height}
            |
            |     |\\
            |____>| \\  {hypotenuse}
                  |  \\
                  |   \\
                  ------
                  {base}"""
    wide = """
            {hypotenuse}
             ↓         ∕ |
                   ∕     | <-{height}
               ∕         |
            ∕------------|
              {base}"""
    equal = """
            {height}
            |
            |     |⋱
            |____>|  ⋱ <-{hypotenuse}
                  |____⋱
                  {base}"""

    pattern = ("This triangle is {area}{units}²\n"
               "It has a perimeter of {perimeter}{units}\n"
               "This is a {aspect} triangle.\n")

    facts = pattern.format(**facts_dictionary)

    height = facts_dictionary["height"]
    base = facts_dictionary["base"]

    if height > base:
        show = tall.format(**facts_dictionary)
    elif height == base:
        show = equal.format(**facts_dictionary)
    else:
        show = wide.format(**facts_dictionary)

    show = show + "\n" + facts
    return show


def triangle_master(base,
                    height,
                    return_diagram=False,
                    return_dictionary=False):
    """Return a dict, diagram, or dict and diagram."""
    dictionary = get_triangle_facts(base, height, units="mm")
    diagram = tell_me_about_this_right_triangle(dictionary)
    if return_diagram and return_dictionary:
        return {"diagram": diagram, "facts": dictionary}
    elif return_diagram:
        return diagram
    elif return_dictionary:
        return {"facts": dictionary}
    else:
        print("You're an odd one, you don't want anything!")


def wordy_pyramid():
    """Helper Pyramid lists."""
    pyramid_list = list_of_words_with_lengths(range(3, 21, 2))
    pyramid_list = list_of_words_with_lengths(range(20, 3, -2))


def get_a_word_of_length_n(length):
    """Getter for a word of length from an URL."""
    import requests
    baseURL = "http://www.setgetgo.com/randomword/get.php?len="
    if length == 0:
        return(None)
    elif type(length) != int:
        return(None)
    else:
        url = baseURL + str(length)
    r = requests.get(url)
    message = r.text
    return(message)


def list_of_words_with_lengths(list_of_lengths):
    """Looper for list of words with lenghts."""
    words_list = []
    for length in list_of_lengths:
        words_list.append(get_a_word_of_length_n(length))
    return words_list


if __name__ == "__main__":
    pass
