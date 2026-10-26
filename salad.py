total_ingredient = int(input("Total Ingredient(g): "))
salt_target = (float(input("Salt target (1%): ") or "1")) / 100.0

recipe = {
    "酱油": 24,
    "辣椒油": 16,
    "蚝油": 12,
    "白糖": 12,
    "盐": 2,
    "味精": 2,
}

sodium = {
    "酱油": 0.06,
    "蚝油": 0.045,
    "盐": 0.39,
    "味精": 0.12,
}

total_sodium = sum([weight * sodium[i] for i, weight in recipe.items() if i in sodium])
pct = total_ingredient * salt_target * 0.39 / total_sodium
for i, w in recipe.items():
    print(f"{i}: {w * pct:.2f}g")
