items = [['hat', 'headgear'], ['sunglasses', 'eyewear'], ['turban', 'headgear']]

# 빈 딕셔너리를 생성하여 headgear와 eyewear 항목을 그룹화합니다.
grouped_items = {}

for item in items:
    item_name, item_type = item
    if item_type in grouped_items:
        grouped_items[item_type].append(item_name)
    else:
        grouped_items[item_type] = [item_name]

# headgear와 eyewear 그룹을 추출합니다.
headgear_items = grouped_items.get('headgear', [])
eyewear_items = grouped_items.get('eyewear', [])

print("Headgear:", headgear_items)
print("Eyewear:", eyewear_items)