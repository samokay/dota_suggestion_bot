from collections import Counter
from typing import Sequence

from driver import Driver

DOTABUFF_COM = "https://www.dotabuff.com"
DOTABUFF_COM_HEROES = f"{DOTABUFF_COM}/heroes"


def get_heroes_names(driver=Driver.get_instance()):
    driver.get(DOTABUFF_COM_HEROES)
    hero_grid = driver.find_element_by_xpath("//div[@class='hero-grid']")
    heroes = hero_grid.find_elements_by_class_name("hero")
    result = []
    for hero in heroes:
        result.append(hero.find_element_by_class_name("name").text)
    return result


def get_url_by_hero_name(name: str):
    hero_href = "/" + name.strip().replace(" ", "-").lower()
    return DOTABUFF_COM_HEROES + hero_href


def get_suggestions(
    names: Sequence[str], bans: Sequence[str] = (), web_driver=Driver.get_instance()
):
    assert len(set(names)) == len(
        names
    ), f"Passed non-unique hero names. {names=} {len(set(names))=}"
    found_worst_versus = []
    for name in names:
        web_driver.get(get_url_by_hero_name(name))
        worst_versus_elements = web_driver.find_elements_by_xpath(
            "//section/header[text()='Worst Versus']/following-sibling::article//a[@class='link-type-hero']"
        )
        found_worst_versus.extend([a.text for a in worst_versus_elements])
    heroes_counter = Counter(hero for hero in found_worst_versus if hero not in bans)

    return heroes_counter.most_common(5)


def get_heroes_spells(name: str, web_driver=Driver.get_instance()):
    hero_abilities_url = f"{get_url_by_hero_name(name)}/abilities"
    web_driver.get(hero_abilities_url)
    spells_names = web_driver.find_elements_by_xpath(
        "//div[@class='skill-tooltip reborn-tooltip']/ancestor::article/preceding-sibling::header"
    )
    spells_stats = web_driver.find_elements_by_xpath(
        "//div[@class='skill-tooltip reborn-tooltip']/div[@class='stats']"
    )

    return zip(
        [make_text_bold(spell.text) for spell in spells_names],
        [stat.text for stat in spells_stats],
    )


def make_text_bold(text):
    return f"**{text}**"
