import random

import pytest

# test1
# input -> hero name
# output -> 5 suggestions to pick
from dotabuff_scrapper import get_suggestions

MAX_HERO_NUMBER = 5
HERO_NAMES = ["Ancient Apparation", "Zeus"]


@pytest.xfail
@pytest.mark.parametrize("hero", HERO_NAMES)
def test_hero_suggestions(hero):
    result = get_suggestions([hero])
    # assert isinstance(result, list)
    assert len(result) == 5
    assert all(item in HERO_NAMES for item in result)


# test2
# input -> multiple heroes (random.choice)
# output -> suggestions to pick
def test_multiple_heroes_suggestions():
    get_suggestions()


@pytest.xfail
@pytest.mark.parametrize("number", range(2, 6))
def test_multiple_heroes_suggestions(number):
    input_heroes = random.sample(HERO_NAMES, number)
    result = get_suggestions(input_heroes)
    heroes_list_assert(result)


def is_a_hero_name(name):
    return name in HERO_NAMES


# TODO: figure out how to assert and return at the same time
@pytest.fixture
def hero_name_assert(name):
    assert is_a_hero_name(name)


@pytest.fixture
def heroes_list_assert(heroes):
    assert all(is_a_hero_name(name) for name in heroes)
