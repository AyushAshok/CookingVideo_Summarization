from nltk.stem import PorterStemmer
stemmer = PorterStemmer()


class BagOfWords:
    def __init__(self):
        self.original_bow=[
            "turmeric", "i", "studying", "cumin", "eat", "no", "coriander", "garam masala", "asafoetida", "hing", "mustard seeds", 
            "fenugreek", "cardamom", "cinnamon", "cloves", "red chili powder", "tamarind", "ginger", 
            "garlic", "onion", "tomato", "green chili", "bay leaf", "curry leaves", "fennel seeds", 
            "black salt", "rock salt", "jaggery", "sugar", "salt", "biryani masala", "chaat masala", 
            "tandoori masala", "methi", "saffron", "kaffir lime", "coconut", "coconut milk", "sugar", "water", "lemon","lemonade",
            "coconut oil", "sesame oil", "ghee", "yogurt", "paneer", "tofu", "lentils", "moong dal", 
            "masoor dal", "toor dal", "chana dal", "rajma", "chickpeas", "green peas", "black beans", 
            "rice", "basmati rice", "pulao rice", "quinoa", "millets", "wheat", "barley", "semolina", 
            "flour", "whole wheat flour", "gram flour", "rice flour", "corn flour", "oats", "methi leaves", 
            "spinach", "amaranth", "bitter gourd", "sweet potato", "pumpkin", "carrot", "cauliflower", "boil", "dissolve", "heat", "pan", "glass",
            "eggplant", "cabbage", "tomato", "green beans", "okra", "bamboo shoots", "mushrooms", "juice", "squeeze",
            "potato", "onion", "garlic", "ginger", "green peas", "pomegranate", "cucumber", "coriander leaves", 
            "mint leaves", "cilantro", "spring onion", "kauri", "chana", "dry fruits", "dates", "raisins", 
            "pistachios", "cashews", "almonds", "walnuts", "sesame seeds", "pumpkin seeds", "sunflower seeds", 
            "peanuts", "ghee", "buttermilk", "cream", "milk", "cheese", "yogurt", "paneer", "sour cream", 
            "cheese curds", "water", "coconut water", "rose water", "sugar", "jaggery", "honey", "molasses", "cook", "mash",
        ]
        self.bow = [stemmer.stem(word.lower().strip()) for word in self.original_bow]

    def stemming(self,word):
        return stemmer.stem(word)
    
    def check_word(self,words):
        wordss = words.strip().strip(".").strip(",").strip("-")
        word=self.stemming(wordss)
        if word.lower() in self.bow:
            return True
        return False

    
