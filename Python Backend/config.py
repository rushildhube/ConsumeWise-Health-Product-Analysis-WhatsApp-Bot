ALLERGEN_MAP = {
    'milk': ['milk', 'milk powder', 'dairy', 'milks'],
    'milks': ['milk', 'milk powder', 'dairy', 'milks'],
    'eggs': ['egg', 'egg white', 'egg yolk', 'eggs'],
    'egg': ['egg', 'egg white', 'egg yolk', 'eggs'],
    'peanuts': ['peanuts', 'groundnuts', 'peanut', 'peanut butter'],
    'peanut': ['peanuts', 'groundnuts', 'peanut', 'peanut butter'],
    'tree nuts': ['almonds', 'cashews', 'hazelnuts', 'macadamia nuts', 'pecans', 'pistachios', 'walnuts', 'tree nuts'],
    'tree nut': ['almonds', 'cashews', 'hazelnuts', 'macadamia nuts', 'pecans', 'pistachios', 'walnuts', 'tree nuts'],
    'soy': ['soy', 'soybeans', 'soy protein', 'soy lecithin', 'soys'],
    'soys': ['soy', 'soybeans', 'soy protein', 'soy lecithin', 'soys'],
    'wheat': ['wheat', 'wheat flour', 'gluten', 'wheats'],
    'wheats': ['wheat', 'wheat flour', 'gluten', 'wheats'],
    'fish': ['fish', 'fish sauce', 'fishes'],
    'fishes': ['fish', 'fish sauce', 'fishes'],
    'shellfish': ['shrimp', 'crab', 'lobster', 'prawns', 'shellfish'],
    'sesame': ['sesame', 'sesame seeds'],
    'sesames': ['sesame', 'sesame seeds'],
    'corn': ['corn', 'cornstarch'],
    'mustard': ['mustard', 'mustard seeds'],
    'sulfites': ['sulfites', 'sulfur dioxide'],
    'artificial colors': ['artificial colors', 'dye', 'coloring'],
    'caffeine': ['caffeine'],
    'lactose': ['lactose'],
    'casein': ['casein'],
    'pollen': ['pollen', 'grass pollen', 'ragweed pollen'],
    'dust mites': ['dust mites', 'dust'],
    'mold': ['mold', 'mold spores'],
    'pet dander': ['pet dander', 'cat dander', 'dog dander'],
    'latex': ['latex'],
    'nickel': ['nickel'],
    'fragrances': ['fragrances', 'perfumes', 'scents'],
    'antibiotics': ['antibiotics', 'penicillin'],
    'nsaids': ['nsaids', 'ibuprofen', 'aspirin'],
    'sulfa drugs': ['sulfa drugs', 'sulfonamides'],
    'soy sauce': ['soy sauce'],
    'alcohol': ['alcohol'],
    'ginger': ['ginger'],
    'garlic': ['garlic'],
    'turmeric': ['turmeric'],
    'msg': ['msg', 'monosodium glutamate'],
    'asparagus': ['asparagus'],
    'tomatoes': ['tomatoes'],
    'avocado': ['avocado'],
    'bananas': ['bananas'],
    'citrus fruits': ['citrus fruits', 'oranges', 'lemons'],
    'citrus fruit': ['citrus fruit', 'orange', 'lemon'],
    'strawberries': ['strawberries'],
    'apples': ['apples'],
    'peaches': ['peaches'],
    'pineapple': ['pineapple'],
    'coconut': ['coconut'],
    'grapes': ['grapes'],
    'celery': ['celery'],
    'carrots': ['carrots'],
    'onions': ['onions'],
    'onion': ['onions']
}

nova_data = [
    # NOVA 1 examples (Unprocessed or Minimally Processed Foods)
    {'ingredients': 'carrot, carrots', 'nova_classification': 1},
    {'ingredients': 'spinach, spinach leaves', 'nova_classification': 1},
    {'ingredients': 'banana, bananas', 'nova_classification': 1},
    {'ingredients': 'almond, almonds', 'nova_classification': 1},
    {'ingredients': 'chicken breast, chicken breasts', 'nova_classification': 1},
    {'ingredients': 'salmon, salmons', 'nova_classification': 1},
    {'ingredients': 'brown rice, brown rices', 'nova_classification': 1},
    {'ingredients': 'milk, milks', 'nova_classification': 1},
    {'ingredients': 'yogurt, yogurts', 'nova_classification': 1},
    {'ingredients': 'egg, eggs', 'nova_classification': 1},
    {'ingredients': 'potato, potatoes', 'nova_classification': 1},
    {'ingredients': 'whole wheat flour, whole wheat flours', 'nova_classification': 1},
    {'ingredients': 'apple, apples', 'nova_classification': 1},
    {'ingredients': 'broccoli, broccolis', 'nova_classification': 1},
    {'ingredients': 'quinoa, quinonas', 'nova_classification': 1},
    {'ingredients': 'beet, beets', 'nova_classification': 1},
    {'ingredients': 'zucchini, zucchinis', 'nova_classification': 1},
    {'ingredients': 'kale, kales', 'nova_classification': 1},
    {'ingredients': 'tofu, tofus', 'nova_classification': 1},
    {'ingredients': 'barley, barleys', 'nova_classification': 1},
    {'ingredients': 'rolled oat flakes', 'nova_classification': 1},
    {'ingredients': 'wheat', 'nova_classification': 1},
    {'ingredients': 'barley', 'nova_classification': 1},

    # NOVA 2 examples (Processed Culinary Ingredients)
    {'ingredients': 'olive oil, olive oils', 'nova_classification': 2},
    {'ingredients': 'butter, butters', 'nova_classification': 2},
    {'ingredients': 'coconut oil, coconut oils', 'nova_classification': 2},
    {'ingredients': 'corn oil, corn oils', 'nova_classification': 2},
    {'ingredients': 'vegetable oil, vegetable oils', 'nova_classification': 2},
    {'ingredients': 'honey, honeys', 'nova_classification': 2},
    {'ingredients': 'salt, salts', 'nova_classification': 2},  # Common salt
    {'ingredients': 'sea salt, sea salts', 'nova_classification': 2},
    {'ingredients': 'rock salt, rock salts', 'nova_classification': 2},
    {'ingredients': 'kosher salt, kosher salts', 'nova_classification': 2},
    {'ingredients': 'table salt, table salts', 'nova_classification': 2},
    {'ingredients': 'baking soda, baking sodas', 'nova_classification': 2},  # Raising agents
    {'ingredients': 'baking powder, baking powders', 'nova_classification': 2},  # Raising agents
    {'ingredients': 'cream of tartar, cream of tartars', 'nova_classification': 2},  # Raising agents
    {'ingredients': 'sugar, sugars', 'nova_classification': 2},
    {'ingredients': 'vinegar, vinegars', 'nova_classification': 2},
    {'ingredients': 'soy sauce, soy sauces', 'nova_classification': 2},
    {'ingredients': 'mustard, mustards', 'nova_classification': 2},
    {'ingredients': 'pepper, peppers', 'nova_classification': 2},
    {'ingredients': 'balsamic vinegar, balsamic vinegars', 'nova_classification': 2},
    {'ingredients': 'syrup, syrups', 'nova_classification': 2},
    {'ingredients': 'margarine, margarines', 'nova_classification': 2},
    {'ingredients': 'sesame oil, sesame oils', 'nova_classification': 2},

    # NOVA 3 examples (Processed Foods)
    {'ingredients': 'canned bean, canned beans', 'nova_classification': 3},
    {'ingredients': 'canned tomato, canned tomatoes', 'nova_classification': 3},
    {'ingredients': 'pickle, pickles', 'nova_classification': 3},
    {'ingredients': 'tuna in olive oil, tunas in olive oil', 'nova_classification': 3},
    {'ingredients': 'cheese, cheeses', 'nova_classification': 3},
    {'ingredients': 'salted peanut, salted peanuts', 'nova_classification': 3},
    {'ingredients': 'bread, breads', 'nova_classification': 3},
    {'ingredients': 'yogurt, yogurts with sugar', 'nova_classification': 3},
    {'ingredients': 'potato chips, potato chip', 'nova_classification': 3},
    {'ingredients': 'processed cheese, processed cheeses', 'nova_classification': 3},
    {'ingredients': 'snack bar, snack bars', 'nova_classification': 3},
    {'ingredients': 'pasta, pastas', 'nova_classification': 3},
    {'ingredients': 'salsa, salsas', 'nova_classification': 3},
    {'ingredients': 'frozen vegetable, frozen vegetables', 'nova_classification': 3},
    {'ingredients': 'frozen fruit, frozen fruits', 'nova_classification': 3},
    {'ingredients': 'canned soup, canned soups', 'nova_classification': 3},



    # NOVA 4 examples (Ultra-Processed Foods)
    {'ingredients': 'high fructose corn syrup, high fructose corn syrups', 'nova_classification': 4},
    {'ingredients': 'hydrogenated vegetable oil, hydrogenated vegetable oils', 'nova_classification': 4},
    {'ingredients': 'instant noodle, instant noodles', 'nova_classification': 4},
    {'ingredients': 'processed cheese, processed cheeses', 'nova_classification': 4},
    {'ingredients': 'soft drink, soft drinks', 'nova_classification': 4},
    {'ingredients': 'candy, candies', 'nova_classification': 4},
    {'ingredients': 'frozen pizza, frozen pizzas', 'nova_classification': 4},
    {'ingredients': 'breakfast cereal, breakfast cereals', 'nova_classification': 4},
    {'ingredients': 'snack cake, snack cakes', 'nova_classification': 4},
    {'ingredients': 'microwave meal, microwave meals', 'nova_classification': 4},
    {'ingredients': 'frozen dinner, frozen dinners', 'nova_classification': 4},
    {'ingredients': 'instant pudding, instant puddings', 'nova_classification': 4},
    {'ingredients': 'cereal bar, cereal bars', 'nova_classification': 4},
    {'ingredients': 'chocolate bar, chocolate bars', 'nova_classification': 4},
    {'ingredients': 'energy drink, energy drinks', 'nova_classification': 4},
    {'ingredients': 'processed meat, processed meats', 'nova_classification': 4},

    # Emulsifiers (Ultra-Processed Level 4)
    {'ingredients': 'emulsifier, emulsifiers', 'nova_classification': 4},
    {'ingredients': 'e322, 322, e471, 471, e472, 472, e476, 476', 'nova_classification': 4},  # Lecithins, Mono & Diglycerides
    {'ingredients': 'e322a, 322a, e475, 475, e472a, 472a, e470b, 470b', 'nova_classification': 4},  # Other emulsifiers

    # Preservatives (Ultra-Processed Level 4)
    {'ingredients': 'preservative, preservatives', 'nova_classification': 4},
    {'ingredients': 'e200, 200, e201, 201, e202, 202, e203, 203', 'nova_classification': 4},  # Sorbates
    {'ingredients': 'e210, 210, e211, 211, e212, 212, e213, 213', 'nova_classification': 4},  # Benzoates
    {'ingredients': 'e220, 220, e221, 221, e222, 222, e223, 223', 'nova_classification': 4},  # Sulfites

    # Stabilizers (Ultra-Processed Level 4)
    {'ingredients': 'stabilizer, stabilizers', 'nova_classification': 4},
    {'ingredients': 'e400, 400, e401, 401, e402, 402, e403, 403', 'nova_classification': 4},  # Alginates
    {'ingredients': 'e410, 410, e412, 412, e415, 415, e450, 450', 'nova_classification': 4},  # Guar gum, xanthan gum, etc.

    # Other Additives (Ultra-Processed Level 4)
    {'ingredients': 'color, colors', 'nova_classification': 4},  # General colorants
    {'ingredients': 'artificial flavor, artificial flavors', 'nova_classification': 4},  # General artificial flavoring
    {'ingredients': 'sweetener, sweeteners', 'nova_classification': 4},
    {'ingredients': 'aspartame, saccharin, sucralose, e950, 950, e951, 951, e952, 952, e954, 954', 'nova_classification': 4},  # Artificial sweeteners
    {'ingredients': 'emulsifying salt (E452), emulsifying salts (E452, E339, E341, E331)', 'nova_classification': 4},  # Emulsifying salts
    {'ingredients': 'iodized salt, iodized salts', 'nova_classification': 2},  # Iodized salt
    {'ingredients': 'class II preservative (E200), class II preservatives (E200, E234)', 'nova_classification': 4},  # Class II preservatives

    {'ingredients': 'processed meat, processed meats', 'nova_classification': 4},
    {'ingredients': 'bacon, sausage, ham, salami', 'nova_classification': 4},

    # Additional Ultra-Processed Ingredients from the provided list
    {'ingredients': 'refined wheat flour (maida)', 'nova_classification': 4},
    {'ingredients': 'edible vegetable oil (palm)', 'nova_classification': 4},
    {'ingredients': 'sugar', 'nova_classification': 4},
    {'ingredients': 'cashew nuts (4.5%)', 'nova_classification': 4},
    {'ingredients': 'invert syrup', 'nova_classification': 4},
    {'ingredients': 'milk solids', 'nova_classification': 4},
    {'ingredients': 'butter (96%)', 'nova_classification': 4},
    {'ingredients': 'raising agents (503 & 500)', 'nova_classification': 4},
    {'ingredients': 'iodised salt', 'nova_classification': 4},
    {'ingredients': 'emulsifiers (322, 471, 472)', 'nova_classification': 4},
    {'ingredients': 'added flavors (nature identical and artificial)', 'nova_classification': 4},

    {'ingredients': 'water', 'nova_classification': 1},  # Unprocessed
    {'ingredients': 'mango pulp (19.5%)', 'nova_classification': 3},  # Possibly processed
    {'ingredients': 'sugar', 'nova_classification': 2},  # Processed culinary ingredient
    {'ingredients': 'acidity regulators (INS330, INS331(iii))', 'nova_classification': 2},  # Processed
    {'ingredients': 'INS330 (citric acid)', 'nova_classification': 2},  # Processed
    {'ingredients': 'INS331(iii) (sodium citrate)', 'nova_classification': 2},  # Processed
    {'ingredients': 'preservatives (INS211, INS224, INS202)', 'nova_classification': 4},  # Ultra-processed
    {'ingredients': 'INS211 (sodium benzoate)', 'nova_classification': 4},  # Ultra-processed
    {'ingredients': 'INS224 (potassium sorbate)', 'nova_classification': 4},  # Ultra-processed
    {'ingredients': 'INS202 (sorbic acid)', 'nova_classification': 4},  # Ultra-processed
    {'ingredients': 'antioxidant (INS300)', 'nova_classification': 2},  # Processed

    {'ingredients': 'caffeine', 'nova_classification': 4},  # Ultra-processed
    {'ingredients': 'taurine', 'nova_classification': 4},  # Ultra-processed
    {'ingredients': 'acidity regulators', 'nova_classification': 2},  # Processed
    {'ingredients': 'malic acid, INS296', 'nova_classification': 2},  # Processed
    {'ingredients': 'tartaric acid, INS334', 'nova_classification': 2},  # Processed
    {'ingredients': 'lactic acid, INS270', 'nova_classification': 2},  # Processed
    {'ingredients': 'phosphoric acid, INS338', 'nova_classification': 2},  # Processed

    {'ingredients': 'acidity regulators (INS330, INS331)', 'nova_classification': 3},  
    {'ingredients': 'citric acid (INS330)', 'nova_classification': 2},  # Processed
    {'ingredients': 'sodium citrate (INS331)', 'nova_classification': 2},  # Processed
    {'ingredients': 'malic acid (INS296)', 'nova_classification': 2},  # Processed
    {'ingredients': 'tartaric acid (INS334)', 'nova_classification': 2},  # Processed
    {'ingredients': 'lactic acid (INS270)', 'nova_classification': 2},  # Processed
    {'ingredients': 'phosphoric acid (INS338)', 'nova_classification': 2},  # Processed
    {'ingredients': 'fumaric acid (INS297)', 'nova_classification': 2},  # Processed
    {'ingredients': 'acetic acid (INS260)', 'nova_classification': 2},  # Processed
    {'ingredients': 'ascorbic acid (INS300)', 'nova_classification': 2},  # Processed
    {'ingredients': 'sorbic acid (INS200)', 'nova_classification': 2},  # Processed
    {'ingredients': 'benzoic acid (INS210)', 'nova_classification': 2},  # Processed

    # Apple Juice Concentrate
    {'ingredients': 'apple juice concentrate (1.5%)', 'nova_classification': 3},
    {'ingredients': 'apple juice concentrate (1.0%)', 'nova_classification': 3},
    {'ingredients': 'apple juice concentrate (0.8%)', 'nova_classification': 3},
    {'ingredients': 'apple juice concentrate (0.5%)', 'nova_classification': 3},
    {'ingredients': 'apple juice concentrate (1.5%) CO2', 'nova_classification': 3},
    {'ingredients': 'apple juice concentrate (1.0%) CO2', 'nova_classification': 3},
    {'ingredients': 'apple juice concentrate (0.8%) CO2', 'nova_classification': 3},
    {'ingredients': 'apple juice concentrate (0.5%) CO2', 'nova_classification': 3},

    # Orange Juice Concentrate
    {'ingredients': 'orange juice concentrate (1.2%)', 'nova_classification': 3},
    {'ingredients': 'orange juice concentrate (1.0%)', 'nova_classification': 3},
    {'ingredients': 'orange juice concentrate (0.8%)', 'nova_classification': 3},
    {'ingredients': 'orange juice concentrate (0.5%)', 'nova_classification': 3},
    {'ingredients': 'orange juice concentrate (1.2%) CO2', 'nova_classification': 3},
    {'ingredients': 'orange juice concentrate (1.0%) CO2', 'nova_classification': 3},
    {'ingredients': 'orange juice concentrate (0.8%) CO2', 'nova_classification': 3},
    {'ingredients': 'orange juice concentrate (0.5%) CO2', 'nova_classification': 3},

    # Grape Juice Concentrate
    {'ingredients': 'grape juice concentrate (1.0%)', 'nova_classification': 3},
    {'ingredients': 'grape juice concentrate (0.8%)', 'nova_classification': 3},
    {'ingredients': 'grape juice concentrate (0.5%)', 'nova_classification': 3},
    {'ingredients': 'grape juice concentrate (0.3%)', 'nova_classification': 3},
    {'ingredients': 'grape juice concentrate (1.0%) CO2', 'nova_classification': 3},
    {'ingredients': 'grape juice concentrate (0.8%) CO2', 'nova_classification': 3},
    {'ingredients': 'grape juice concentrate (0.5%) CO2', 'nova_classification': 3},
    {'ingredients': 'grape juice concentrate (0.3%) CO2', 'nova_classification': 3},

    # Cranberry Juice Concentrate
    {'ingredients': 'cranberry juice concentrate (1.5%)', 'nova_classification': 3},
    {'ingredients': 'cranberry juice concentrate (1.2%)', 'nova_classification': 3},
    {'ingredients': 'cranberry juice concentrate (1.0%)', 'nova_classification': 3},
    {'ingredients': 'cranberry juice concentrate (0.5%)', 'nova_classification': 3},
    {'ingredients': 'cranberry juice concentrate (1.5%) CO2', 'nova_classification': 3},
    {'ingredients': 'cranberry juice concentrate (1.2%) CO2', 'nova_classification': 3},
    {'ingredients': 'cranberry juice concentrate (1.0%) CO2', 'nova_classification': 3},
    {'ingredients': 'cranberry juice concentrate (0.5%) CO2', 'nova_classification': 3},

    # Pineapple Juice Concentrate
    {'ingredients': 'pineapple juice concentrate (1.0%)', 'nova_classification': 3},
    {'ingredients': 'pineapple juice concentrate (0.8%)', 'nova_classification': 3},
    {'ingredients': 'pineapple juice concentrate (0.6%)', 'nova_classification': 3},
    {'ingredients': 'pineapple juice concentrate (0.4%)', 'nova_classification': 3},
    {'ingredients': 'pineapple juice concentrate (1.0%) CO2', 'nova_classification': 3},
    {'ingredients': 'pineapple juice concentrate (0.8%) CO2', 'nova_classification': 3},
    {'ingredients': 'pineapple juice concentrate (0.6%) CO2', 'nova_classification': 3},
    {'ingredients': 'pineapple juice concentrate (0.4%) CO2', 'nova_classification': 3},

    # Tomato Concentrate
    {'ingredients': 'tomato concentrate (1.0%)', 'nova_classification': 3},
    {'ingredients': 'tomato concentrate (0.8%)', 'nova_classification': 3},
    {'ingredients': 'tomato concentrate (0.6%)', 'nova_classification': 3},
    {'ingredients': 'tomato concentrate (0.4%)', 'nova_classification': 3},
    {'ingredients': 'tomato concentrate (1.0%) CO2', 'nova_classification': 3},
    {'ingredients': 'tomato concentrate (0.8%) CO2', 'nova_classification': 3},
    {'ingredients': 'tomato concentrate (0.6%) CO2', 'nova_classification': 3},
    {'ingredients': 'tomato concentrate (0.4%) CO2', 'nova_classification': 3},

    # Peach Concentrate
    {'ingredients': 'peach concentrate (1.0%)', 'nova_classification': 3},
    {'ingredients': 'peach concentrate (0.8%)', 'nova_classification': 3},
    {'ingredients': 'peach concentrate (0.6%)', 'nova_classification': 3},
    {'ingredients': 'peach concentrate (0.4%)', 'nova_classification': 3},
    {'ingredients': 'peach concentrate (1.0%) CO2', 'nova_classification': 3},
    {'ingredients': 'peach concentrate (0.8%) CO2', 'nova_classification': 3},
    {'ingredients': 'peach concentrate (0.6%) CO2', 'nova_classification': 3},
    {'ingredients': 'peach concentrate (0.4%) CO2', 'nova_classification': 3},

    # Mango Concentrate
    {'ingredients': 'mango concentrate (1.0%)', 'nova_classification': 3},
    {'ingredients': 'mango concentrate (0.8%)', 'nova_classification': 3},
    {'ingredients': 'mango concentrate (0.5%)', 'nova_classification': 3},
    {'ingredients': 'mango concentrate (0.3%)', 'nova_classification': 3},
    {'ingredients': 'mango concentrate (1.0%) CO2', 'nova_classification': 3},
    {'ingredients': 'mango concentrate (0.8%) CO2', 'nova_classification': 3},
    {'ingredients': 'mango concentrate (0.5%) CO2', 'nova_classification': 3},
    {'ingredients': 'mango concentrate (0.3%) CO2', 'nova_classification': 3},

    # Strawberry Concentrate
    {'ingredients': 'strawberry concentrate (1.0%)', 'nova_classification': 3},
    {'ingredients': 'strawberry concentrate (0.8%)', 'nova_classification': 3},
    {'ingredients': 'strawberry concentrate (0.6%)', 'nova_classification': 3},
    {'ingredients': 'strawberry concentrate (0.4%)', 'nova_classification': 3},
    {'ingredients': 'strawberry concentrate (1.0%) CO2', 'nova_classification': 3},
    {'ingredients': 'strawberry concentrate (0.8%) CO2', 'nova_classification': 3},
    {'ingredients': 'strawberry concentrate (0.6%) CO2', 'nova_classification': 3},
    {'ingredients': 'strawberry concentrate (0.4%) CO2', 'nova_classification': 3},

    # Raspberry Concentrate
    {'ingredients': 'raspberry concentrate (1.0%)', 'nova_classification': 3},
    {'ingredients': 'raspberry concentrate (0.8%)', 'nova_classification': 3},
    {'ingredients': 'raspberry concentrate (0.5%)', 'nova_classification': 3},
    {'ingredients': 'raspberry concentrate (0.3%)', 'nova_classification': 3},
    {'ingredients': 'raspberry concentrate (1.0%) CO2', 'nova_classification': 3},
    {'ingredients': 'raspberry concentrate (0.8%) CO2', 'nova_classification': 3},
    {'ingredients': 'raspberry concentrate (0.5%) CO2', 'nova_classification': 3},
    {'ingredients': 'raspberry concentrate (0.3%) CO2', 'nova_classification': 3},

    # Blueberry Concentrate
    {'ingredients': 'blueberry concentrate (1.0%)', 'nova_classification': 3},
    {'ingredients': 'blueberry concentrate (0.8%)', 'nova_classification': 3},
    {'ingredients': 'blueberry concentrate (0.6%)', 'nova_classification': 3},
    {'ingredients': 'blueberry concentrate (0.4%)', 'nova_classification': 3},
    {'ingredients': 'blueberry concentrate (1.0%) CO2', 'nova_classification': 3},
    {'ingredients': 'blueberry concentrate (0.8%) CO2', 'nova_classification': 3},
    {'ingredients': 'blueberry concentrate (0.6%) CO2', 'nova_classification': 3},
    {'ingredients': 'blueberry concentrate (0.4%) CO2', 'nova_classification': 3},

    # Vegetable Juice Concentrate
    {'ingredients': 'vegetable juice concentrate (1.0%)', 'nova_classification': 3},
    {'ingredients': 'vegetable juice concentrate (0.8%)', 'nova_classification': 3},
    {'ingredients': 'vegetable juice concentrate (0.6%)', 'nova_classification': 3},
    {'ingredients': 'vegetable juice concentrate (0.4%)', 'nova_classification': 3},
    {'ingredients': 'vegetable juice concentrate (1.0%) CO2', 'nova_classification': 3},
    {'ingredients': 'vegetable juice concentrate (0.8%) CO2', 'nova_classification': 3},
    {'ingredients': 'vegetable juice concentrate (0.6%) CO2', 'nova_classification': 3},
    {'ingredients': 'vegetable juice concentrate (0.4%) CO2', 'nova_classification': 3},


]


