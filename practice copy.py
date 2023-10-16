from collections import Counter

products = ["towel red long thin", "blanket red thick short", "curtain red long wide", "mattress thick", "hat red thin", "pillow red long", "muffler blue thick long"]
purchased = ["blanket", "curtain", "hat", "muffler"]

# 제품의 우선순위 = 각 제품의 특성으로 결정 -> 고객이 구매하지 않은 제품 중에서 우선순위가 가장 높은 하나를 선택해서 추천

# 특성의 우선순위 => 고객이 구매했던 특성이 몇번 나타나는지 각각 세기 -> 특성 나타난 횟수 크기가 높은 순서대로 우선순위 -> 
# 횟수가 같으면 사전순으로 앞서는게 우선순위(정렬 필요)

# 제품의 우선순위 -> 더 높은 우선순위의 특성을 가지고 있는 제품 순서대로 우선순위
# 가장 높은 운선순위 특성이 같아면 그 다음으로 우선순위가 높은 특성들을 차례대로 비교
# 비교할 특성이 먼저 바닥난 제품의 우선순위가 상대적으로 낮다

products_name = [] # 상품 이름 ['sofa', 'blanket', 'towel', 'mattress', 'curtain']
products_dict = {} # 상품 이름 : 상품 특성 {'sofa': ['red', 'long'], 'blanket': ['blue', 'long'], 'towel': ['red'], 'mattress': ['long'], 'curtain': ['blue', 'long', 'cheap']}

for i in range(len(products)):
    sample = list(products[i].split())
    products_name.append(sample[0])
    products_dict[sample[0]] = []
    for j in range(1,len(sample)):
        products_dict[sample[0]].append(sample[j])

customer_dict = {} # {'towel': ['red'], 'mattress': ['long'], 'curtain': ['blue', 'long', 'cheap']}
for j in range(len(purchased)):
    customer_dict[purchased[j]] = products_dict[purchased[j]]
customer_cha = [] # ['red', 'long', 'blue', 'long', 'cheap']
for k in customer_dict:
    for l in range(len(customer_dict[k])):
        customer_cha.append(customer_dict[k][l])

counter_customer_cha = Counter(customer_cha) # Counter({'long': 2, 'red': 1, 'blue': 1, 'cheap': 1})
cha_order = [] # [['long', 2], ['blue', 1], ['cheap', 1], ['red', 1]]

for key,value in counter_customer_cha.items():
    cha_order.append([key,value])

cha_order = sorted(cha_order, key= lambda x:(-x[1],x[0]))

order = [] # ['long', 'blue', 'cheap', 'red']
for m in range(len(cha_order)):
    order.append(cha_order[m][0])

recommend_name_lst = [] # ['sofa', 'blanket']
for n in range(len(products_name)):
    if products_name[n] not in purchased:
        recommend_name_lst.append(products_name[n])

recommend_chr_lst = [] # [['towel', 'red', 'long', 'thin'], ['mattress', 'thick'], ['pillow', 'red', 'long']]
for o in range(len(recommend_name_lst)):
    recommend_chr = products_dict[recommend_name_lst[o]]
    recommend_chr_lst.append([recommend_name_lst[o]])
    for p in range(len(recommend_chr)):
        recommend_chr_lst[o].append(recommend_chr[p])

recommend_length_lst = []
for q in range(len(recommend_chr_lst)):
    recommend_length_lst.append(len(recommend_chr_lst[q]))

length = max(recommend_length_lst)

for r in range(1,length):
    length = len(recommend_chr_lst)
    recommend_all_lst = sorted(recommend_chr_lst, key= lambda x:(order.index(x[r])))
    for s in range(length):
        if not recommend_chr_lst[s]:
            recommend_chr_lst.remove(recommend_chr_lst[s])
        length = len(recommend_chr_lst)

print(recommend_chr_lst)
    





            

        









