from pages.food_diary_page import FoodDiaryPage
import allure


@allure.feature('Check food diary page')
@allure.story('Check food diary page is open')
def test_food_diary_page(driver):
    with allure.step('Open Food diary page'):
        food_diary_page = FoodDiaryPage(driver)
        food_diary_page.open()
    with allure.step('Food diary page is open'):
        assert food_diary_page.present_url() == food_diary_page.page_url


@allure.feature('Check food diary page')
@allure.story('Check create recipe - name alert')
def test_create_new_recipe_name_alert(driver):
    with allure.step('Open Food diary page'):
        food_diary_page = FoodDiaryPage(driver)
        food_diary_page.open()
    with allure.step('Create new recipe button click'):
        food_diary_page.create_new_recipe()
    with allure.step('Press save button'):
        food_diary_page.click_save_button()
    with allure.step('Check recipe name alert'):
        assert food_diary_page.recipe_name_alert_is_displayed()


@allure.feature('Check food diary page')
@allure.story('Check create recipe - add ingredient')
def test_create_new_recipe_add_ingredient(driver):
    with allure.step('Open Food diary page'):
        food_diary_page = FoodDiaryPage(driver)
        food_diary_page.open()
    with allure.step('Create new recipe button click'):
        food_diary_page.create_new_recipe()
    with allure.step('Add ingredient'):
        food_diary_page.add_ingredient()
    with allure.step('Check ingredient added'):
        assert food_diary_page.added_ingredient_is_displayed()


@allure.feature('Check food diary page')
@allure.story('Check create recipe')
def test_create_new_recipe(driver):
    with allure.step('Open Food diary page'):
        food_diary_page = FoodDiaryPage(driver)
        food_diary_page.open()
    with allure.step('Create new recipe button click'):
        food_diary_page.create_new_recipe()
    with allure.step('Enter recipe name'):
        food_diary_page.enter_recipe_name()
    with allure.step('Press save button'):
        food_diary_page.click_save_recipe_button()
    with allure.step('Press my recipes button'):
        food_diary_page.click_my_recipes_button()
    with allure.step('Check recipe saved'):
        assert food_diary_page.my_recipe_is_displayed()


@allure.feature('Check food diary page')
@allure.story('Check delete recipe')
def test_delete_new_recipe(driver):
    with allure.step('Open Food diary page'):
        food_diary_page = FoodDiaryPage(driver)
        food_diary_page.open()
    with allure.step('Press my recipes button'):
        food_diary_page.click_my_recipes_button()
    with allure.step('Click new recipe button'):
        food_diary_page.click_my_new_recipe()
    with allure.step('Click delete recipe button'):
        food_diary_page.click_delete_recipe_button()
    with allure.step('Check recipe delete'):
        food_diary_page.click_my_recipes_button()
        assert food_diary_page.my_recipe_is_not_displayed() == 0


@allure.feature('Check food diary page')
@allure.story('Check create product - name alert')
def test_create_new_product_name_alert(driver):
    with allure.step('Open Food diary page'):
        food_diary_page = FoodDiaryPage(driver)
        food_diary_page.open()
    with allure.step('Create new product button click'):
        food_diary_page.create_new_product()
    with allure.step('Press save button'):
        food_diary_page.click_save_product_button()
    with allure.step('Check product name alert'):
        assert food_diary_page.product_name_alert_is_displayed()


@allure.feature('Check food diary page')
@allure.story('Check create product - product components')
def test_create_new_product_add_components(driver):
    with allure.step('Open Food diary page'):
        food_diary_page = FoodDiaryPage(driver)
        food_diary_page.open()
    with allure.step('Create new product button click'):
        food_diary_page.create_new_product()
    with allure.step('Add product components'):
        enter_value = food_diary_page.add_product_components()
    with allure.step('Get value added product components'):
        get_value = food_diary_page.added_product_components_values()
    with allure.step('Check values correctness'):
        assert enter_value == get_value


@allure.feature('Check food diary page')
@allure.story('Check create product - product components clear')
def test_create_new_product_clear_components(driver):
    with allure.step('Open Food diary page'):
        food_diary_page = FoodDiaryPage(driver)
        food_diary_page.open()
    with allure.step('Create new product button click'):
        food_diary_page.create_new_product()
    with allure.step('Add product components'):
        food_diary_page.add_product_components()
    with allure.step('Clear product components'):
        food_diary_page.clear_product_components()
    with allure.step('Get value added product components'):
        get_value = food_diary_page.added_product_components_values()
    with allure.step('Check values correctness'):
        assert get_value == ('0', '0', '0', '0')


@allure.feature('Check food diary page')
@allure.story('Check create product')
def test_create_new_product(driver):
    with allure.step('Open Food diary page'):
        food_diary_page = FoodDiaryPage(driver)
        food_diary_page.open()
    with allure.step('Create new product button click'):
        food_diary_page.create_new_product()
    with allure.step('Enter product name'):
        food_diary_page.enter_product_name()
    with allure.step('Press save button'):
        food_diary_page.click_save_product_button()
    with allure.step('Press return button'):
        food_diary_page.click_return_button()
    with allure.step('Press my products button'):
        food_diary_page.click_my_products_button()
    with allure.step('Check product saved'):
        assert food_diary_page.my_product_is_displayed()


@allure.feature('Check food diary page')
@allure.story('Check delete product')
def test_delete_new_product(driver):
    with allure.step('Open Food diary page'):
        food_diary_page = FoodDiaryPage(driver)
        food_diary_page.open()
    with allure.step('Press my products button'):
        food_diary_page.click_my_products_button()
    with allure.step('Click new product button'):
        food_diary_page.click_my_new_product()
    with allure.step('Click delete product button'):
        food_diary_page.click_delete_product_button()
    with allure.step('Check product delete'):
        food_diary_page.click_my_products_button()
        assert food_diary_page.my_product_is_not_displayed() == 0
