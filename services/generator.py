import random
from string import ascii_lowercase, digits
from collections import Counter

class Generator(object):
    def __init__(self):
        self.stats = list()
        
    def _alpha_string(self):
        return self._generate_object(ascii_lowercase)
    
    def _real_number(self):
        return random.random() * random.randint(100, 200)
    
    def _integers(self):
        return self._generate_object(digits)
    
    def _alphanumerics(self):
        alphanumerics = list(ascii_lowercase + digits)
        random.shuffle(alphanumerics)
        ''.join(alphanumerics)
        return self._generate_object(alphanumerics)
    
    def _generate_object(self, data):
        object = ''
        for _ in range(random.randint(5, 15)):
            object += random.choice(data)
        return object
    
    def get_object(self):
        string_type = {
            "string": self._alpha_string(),
            "realnumber": self._real_number(),
            "integers": self._integers(),
            "alphanumerics": self._alphanumerics()
        }
        selected_type = random.choice(list(string_type.keys()))
        self.stats.append(selected_type)
        return string_type.get(selected_type)
    
    def make_report(self):
        return dict(Counter(self.stats))
