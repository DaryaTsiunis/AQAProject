from pages.base_page import BasePage
from locators import loc_food_diary_page as loc
import constants as con
from selenium.webdriver.common.keys import Keys


class FoodDiaryPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = 'https://tvoydnevnik.com/diary/foodDiary/20139564/'

    def create_new_recipe(self):
        create_new_recipe_button = self.find(loc.create_new_recipe_button)
        create_new_recipe_button.click()

    def enter_recipe_name(self):
        recipe_name_field = self.find(loc.recipe_name_field)
        recipe_name_field.click()
        recipe_name_field.send_keys(con.recipe_name_text)

    def click_save_button(self):
        save_button = self.find(loc.save_recipe_button)
        save_button.click()

    def click_save_recipe_button(self):
        save_button = self.find(loc.save_recipe_button)
        save_button.click()
        self.refresh_page()

    def recipe_name_alert_is_displayed(self):
        recipe_name_alert = self.find(loc.recipe_name_alert)
        return recipe_name_alert.is_displayed()

    def add_ingredient(self):
        ingredient_group_name = self.find(loc.ingredient_group)
        ingredient_group_name.click()
        ingredient_name = self.find(loc.ingredient_name)
        ingredient_name.click()
        add_ingredient_button = self.find(loc.add_ingredient_button)
        add_ingredient_button.click()

    def added_ingredient_is_displayed(self):
        added_ingredient = self.find(loc.added_ingredient_name)
        return added_ingredient.is_displayed()

    def add_product_components(self):
        product_components = self.find_all(loc.product_components_fields)
        product_components[0].send_keys(Keys.BACKSPACE)
        product_components[0].send_keys(con.calories)
        product_components[1].send_keys(Keys.BACKSPACE)
        product_components[1].send_keys(con.squirrels)
        product_components[2].send_keys(Keys.BACKSPACE)
        product_components[2].send_keys(con.fats)
        product_components[3].send_keys(Keys.BACKSPACE)
        product_components[3].send_keys(con.carbohydrates)
        return con.calories, con.squirrels, con.fats, con.carbohydrates

    def added_product_components_values(self):
        product_components_values = self.find_all(loc.product_components_fields)
        return (product_components_values[0].get_attribute('value'),
                product_components_values[1].get_attribute('value'),
                product_components_values[2].get_attribute('value'),
                product_components_values[3].get_attribute('value')
                )

    def clear_product_components(self):
        clear_components_button = self.find(loc.clear_components_button)
        clear_components_button.click()

    def click_my_recipes_button(self):
        my_recipes_button = self.find(loc.my_recipes_button)
        my_recipes_button.click()

    def my_recipe_is_displayed(self):
        my_recipe = self.find(loc.recipe_name)
        return my_recipe.is_displayed()

    def click_my_new_recipe(self):
        my_recipe = self.find(loc.recipe_name)
        my_recipe.click()

    def click_delete_recipe_button(self):
        delete_recipe_button = self.find(loc.delete_recipe_button)
        delete_recipe_button.click()
        delete_recipe_button_confirm = self.find(loc.delete_recipe_button_confirm)
        delete_recipe_button_confirm.click()
        self.refresh_page()

    def my_recipe_is_not_displayed(self):
        return len(self.find_all(loc.recipe_name))

    def create_new_product(self):
        create_new_product_button = self.find(loc.create_new_product_button)
        create_new_product_button.click()

    def enter_product_name(self):
        product_name_field = self.find(loc.product_name_field)
        product_name_field.click()
        product_name_field.send_keys(con.product_name_text)

    def click_save_product_button(self):
        save_product_button = self.find(loc.save_product_button)
        save_product_button.click()

    def product_name_alert_is_displayed(self):
        product_name_alert = self.find(loc.product_name_alert)
        return product_name_alert.is_displayed()

    def click_return_button(self):
        return_button = self.find(loc.return_button)
        return_button.click()
        self.refresh_page()

    def click_my_products_button(self):
        my_products_button = self.find(loc.my_products_button)
        my_products_button.click()

    def my_product_is_displayed(self):
        my_product = self.find(loc.product_name)
        return my_product.is_displayed()

    def click_my_new_product(self):
        my_product = self.find(loc.product_name)
        my_product.click()

    def click_delete_product_button(self):
        delete_product_button = self.find(loc.delete_product_button)
        delete_product_button.click()
        delete_product_button_confirm = self.find(loc.delete_product_button_confirm)
        delete_product_button_confirm.click()
        self.refresh_page()

    def my_product_is_not_displayed(self):
        return len(self.find_all(loc.product_name))
