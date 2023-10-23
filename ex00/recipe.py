class Recipe:
    def __init__(self, name: str, cooking_lvl: int, cooking_time: int, ingredients: list[str], recipe_type: str, description: str = ''):
        self.name = name
        if cooking_lvl < 1 or cooking_lvl > 5:
            raise 'IncorrectInput: cooking_lvl must be between 1 and 5'
        self.cooking_lvl = cooking_lvl
        if cooking_time < 0 or cooking_time > 60:
            raise 'IncorrectInput: cooking_time must be minutes range'
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        if recipe_type != 'starter' | recipe_type != 'lunch' | recipe_type != 'desert':
            raise 'IncorrectInput: recipe_type must be either starter, lunch or desert'
        self.recipe_type = recipe_type

    def __str__(self) -> str:
        """Return the string to print with the recipe info"""
        return 'Recipe for {} (level: {}):\n\
    Description: {}\n\
    Ingredients list: {}\n\
    To be eaten for {}\n\
    Takes {} minutes of cooking'.format(
            self.name,
            self.cooking_lvl,
            self.description,
            self.ingredients,
            self.recipe_type,
            self.cooking_time)
