from selenium import webdriver

DOTABUFF_COM_HEROES = "https://www.dotabuff.com/heroes"

driver = webdriver.Chrome()


def get_heroes_names(driver):
    driver.get(DOTABUFF_COM_HEROES)
    hero_grid = driver.find_element_by_xpath("//div[@class='hero-grid']")
    heroes = hero_grid.find_elements_by_class_name("hero")
    result = []
    for hero in heroes:
        result.append(hero.find_element_by_class_name("name").text)
    # print(driver.page_source)


print(get_heroes_names(driver))
driver.quit()
