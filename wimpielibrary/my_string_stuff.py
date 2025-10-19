import random
import re

# Replace numbers in a string with random numbers while preserving length of the text.
replace_numbers_preserve_length = lambda text: re.sub(r'\d+', lambda m: ''.join(str(random.randint(0, 9)) for _ in m.group()), text)