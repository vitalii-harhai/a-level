# Написати функцію переведення розмірів жіночої білизни з міжнародної у решту.
# Всередині функції потрібно просто звертатися до правильно складеного словника.

def size_international_to_regional(dict_size: dict, international_size: str, regional_id: str):
    output_size = dict_size[international_size][regional_id]
    return output_size


size = {
    'XXS': {'DE': 36, 'US': 8, 'FR': 38, 'UK': 24},
    'XS': {'DE': 38, 'US': 10, 'FR': 40, 'UK': 26},
    'S': {'DE': 40, 'US': 12, 'FR': 42, 'UK': 28},
    'M': {'DE': 42, 'US': 14, 'FR': 44, 'UK': 30},
    'L': {'DE': 44, 'US': 16, 'FR': 46, 'UK': 32},
    'XL': {'DE': 46, 'US': 18, 'FR': 48, 'UK': 34},
    'XXL': {'DE': 48, 'US': 20, 'FR': 50, 'UK': 36},
    'XXXL': {'DE': 50, 'US': 22, 'FR': 52, 'UK': 38},
}

# XL in US
print(size_international_to_regional(size, 'XL', 'US'))

# XXXL in DE
print(size_international_to_regional(size, 'XXXL', 'DE'))

