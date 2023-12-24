SIZE = [
    {'international': 'XXS', 'DE': 36, 'US': 8, 'FR': 38, 'UK': 24},
    {'international': 'XS', 'DE': 38, 'US': 10, 'FR': 40, 'UK': 26},
    {'international': 'S', 'DE': 40, 'US': 12, 'FR': 42, 'UK': 28},
    {'international': 'M', 'DE': 42, 'US': 14, 'FR': 44, 'UK': 30},
    {'international': 'L', 'DE': 44, 'US': 16, 'FR': 46, 'UK': 32},
    {'international': 'XL', 'DE': 46, 'US': 18, 'FR': 48, 'UK': 34},
    {'international': 'XXL', 'DE': 48, 'US': 20, 'FR': 50, 'UK': 36},
    {'international': 'XXXL', 'DE': 50, 'US': 22, 'FR': 52, 'UK': 38},
]


def size_conversion(input_id: str, output_id: str, size_country=None):
    if size_country:
        filter_item = filter(lambda x: x[input_id] == size_country, SIZE)
    else:
        filter_item = filter(lambda x: x['international'] == input_id, SIZE)
    for i in filter_item:
        filter_item = i
    search_size = filter_item[output_id]
    if size_country:
        message = (f'Size {input_id} - {size_country} in {output_id} = {search_size}. For reference, '
                   f'this is international size - {filter_item["international"]}')
    else:
        message = f'Size {input_id} in {output_id} = {search_size}.'
    return message


# DE 48 in US
s = size_conversion('DE', 'US', size_country=48)
print(s)

# M in UK
s = size_conversion('M', 'UK')
print(s)
