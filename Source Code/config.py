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
    {'ingredients': 'carrot, carrots', 'nova_classification': 1},  # Fresh vegetables
    {'ingredients': 'spinach, spinach leaves', 'nova_classification': 1},  # Leafy greens
    {'ingredients': 'banana, bananas', 'nova_classification': 1},  # Fresh fruit
    {'ingredients': 'almond, almonds', 'nova_classification': 1},  # Whole nuts
    {'ingredients': 'chicken breast, chicken breasts', 'nova_classification': 1},  # Fresh meat
    {'ingredients': 'salmon, salmons', 'nova_classification': 1},  # Fresh fish
    {'ingredients': 'brown rice, brown rices', 'nova_classification': 1},  # Whole grain
    {'ingredients': 'milk, milks', 'nova_classification': 1},  # Fresh milk
    {'ingredients': 'yogurt, yogurts', 'nova_classification': 1},  # Plain yogurt (minimally processed)
    {'ingredients': 'egg, eggs', 'nova_classification': 1},  # Whole eggs
    {'ingredients': 'potato, potatoes', 'nova_classification': 1},  # Fresh tubers
    {'ingredients': 'whole wheat flour, whole wheat flours', 'nova_classification': 1},  # Ground flour (minimally processed)
    {'ingredients': 'apple, apples', 'nova_classification': 1},  # Fresh fruit
    {'ingredients': 'broccoli, broccolis', 'nova_classification': 1},  # Fresh vegetables
    {'ingredients': 'quinoa, quinonas', 'nova_classification': 1},  # Whole grain
    {'ingredients': 'beet, beets', 'nova_classification': 1},  # Fresh root vegetable
    {'ingredients': 'zucchini, zucchinis', 'nova_classification': 1},  # Fresh vegetable
    {'ingredients': 'kale, kales', 'nova_classification': 1},  # Leafy greens
    {'ingredients': 'tofu, tofus', 'nova_classification': 1},  # Plant-based protein
    {'ingredients': 'barley, barleys', 'nova_classification': 1},  # Whole grain

    # NOVA 2 examples (Processed Culinary Ingredients)
    {'ingredients': 'olive oil, olive oils', 'nova_classification': 2},
    {'ingredients': 'butter, butters', 'nova_classification': 2},
    {'ingredients': 'coconut oil, coconut oils', 'nova_classification': 2},
    {'ingredients': 'corn oil, corn oils', 'nova_classification': 2},
    {'ingredients': 'vegetable oil, vegetable oils', 'nova_classification': 2},
    {'ingredients': 'honey, honeys', 'nova_classification': 2},
    {'ingredients': 'salt, salts', 'nova_classification': 2},  # Added salt as an example
    {'ingredients': 'sugar, sugars', 'nova_classification': 2},  # Added sugar
    {'ingredients': 'vinegar, vinegars', 'nova_classification': 2},  # Added vinegar
    {'ingredients': 'soy sauce, soy sauces', 'nova_classification': 2},  # Added soy sauce
    {'ingredients': 'mustard, mustards', 'nova_classification': 2},  # Added mustard
    {'ingredients': 'pepper, peppers', 'nova_classification': 2},  # Added pepper
    {'ingredients': 'balsamic vinegar, balsamic vinegars', 'nova_classification': 2},  # Added balsamic vinegar
    {'ingredients': 'syrup, syrups', 'nova_classification': 2},  # Added syrup
    {'ingredients': 'margarine, margarines', 'nova_classification': 2},  # Added margarine
    {'ingredients': 'sesame oil, sesame oils', 'nova_classification': 2},  # Added sesame oil

    # NOVA 3 examples (Processed Foods)
    {'ingredients': 'canned bean, canned beans', 'nova_classification': 3},
    {'ingredients': 'canned tomato, canned tomatoes', 'nova_classification': 3},
    {'ingredients': 'pickle, pickles', 'nova_classification': 3},
    {'ingredients': 'tuna in olive oil, tunas in olive oil', 'nova_classification': 3},
    {'ingredients': 'cheese, cheeses', 'nova_classification': 3},
    {'ingredients': 'salted peanut, salted peanuts', 'nova_classification': 3},
    {'ingredients': 'bread, breads', 'nova_classification': 3},
    {'ingredients': 'yogurt, yogurts with sugar', 'nova_classification': 3},  # Added variation
    {'ingredients': 'potato chips, potato chip', 'nova_classification': 3},  # Added potato chips
    {'ingredients': 'processed cheese, processed cheeses', 'nova_classification': 3},  # Added processed cheese
    {'ingredients': 'snack bar, snack bars', 'nova_classification': 3},  # Added snack bars
    {'ingredients': 'pasta, pastas', 'nova_classification': 3},  # Added pasta
    {'ingredients': 'salsa, salsas', 'nova_classification': 3},  # Added salsa
    {'ingredients': 'frozen vegetable, frozen vegetables', 'nova_classification': 3},  # Added frozen vegetables
    {'ingredients': 'frozen fruit, frozen fruits', 'nova_classification': 3},  # Added frozen fruit
    {'ingredients': 'canned soup, canned soups', 'nova_classification': 3},  # Added canned soups

    # NOVA 4 examples (Ultra-Processed Foods)
    {'ingredients': 'high fructose corn syrup, high fructose corn syrups', 'nova_classification': 4},  # Sweetened beverage
    {'ingredients': 'hydrogenated vegetable oil, hydrogenated vegetable oils', 'nova_classification': 4},  # Snack food
    {'ingredients': 'instant noodle, instant noodles', 'nova_classification': 4},  # Instant noodle product
    {'ingredients': 'processed cheese, processed cheeses', 'nova_classification': 4},  # Processed cheese slices
    {'ingredients': 'soft drink, soft drinks', 'nova_classification': 4},  # Soft drink
    {'ingredients': 'candy, candies', 'nova_classification': 4},  # Candy
    {'ingredients': 'frozen pizza, frozen pizzas', 'nova_classification': 4},  # Frozen pizza
    {'ingredients': 'breakfast cereal, breakfast cereals', 'nova_classification': 4},  # Sugary breakfast cereal
    {'ingredients': 'snack cake, snack cakes', 'nova_classification': 4},  # Added snack cakes
    {'ingredients': 'microwave meal, microwave meals', 'nova_classification': 4},  # Added microwave meals
    {'ingredients': 'frozen dinner, frozen dinners', 'nova_classification': 4},  # Added frozen dinners
    {'ingredients': 'instant pudding, instant puddings', 'nova_classification': 4},  # Added instant puddings
    {'ingredients': 'cereal bar, cereal bars', 'nova_classification': 4},  # Added cereal bars
    {'ingredients': 'chocolate bar, chocolate bars', 'nova_classification': 4},  # Added chocolate bars
    {'ingredients': 'energy drink, energy drinks', 'nova_classification': 4},  # Added energy drinks
    {'ingredients': 'processed meat, processed meats', 'nova_classification': 4}  # Added processed meats
]
