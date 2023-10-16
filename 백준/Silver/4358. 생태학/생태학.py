import sys

tree_dict = {}

pyobon = 0

while True:
    tree = sys.stdin.readline().rstrip()
    if tree == "":
        break
    pyobon += 1
    if tree not in tree_dict:
        tree_dict[tree] = 1
    else:
        tree_dict[tree] += 1

tree_dict = dict(sorted(tree_dict.items()))

for i in tree_dict:
    per = ((tree_dict[i] / pyobon)*100)
    result = "{:.4f}".format(per)
    print("{} {}".format(i,result))