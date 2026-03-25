def input_default(prompt: str, default: int):
    return int(input(prompt.format(default=default)) or default)

def calc():
    meat_weight = int(input("Total Meat Amount (Beef + Shrimp) in grams: "))
    other_weight = int(input("Total Other Ingredients in grams: "))

    water_weight = meat_weight * 0.4
    oil_weight = (meat_weight + water_weight + other_weight) * 0.02
    total_weight = meat_weight + water_weight + other_weight + oil_weight 
    salt_ratio = float(input("Total salt ratio (default 1.5): ") or "1.5")
    total_sodium = total_weight * salt_ratio / 100 * 23 / 59
    soy_weight = input_default("Total soy sause weight (default: {default}): ", int(total_weight * 0.02))
    oyster_weight = input_default("Total oyster sause weight (default: {default}): ", int(total_weight * 0.02))
    msg_weight = input_default("Total MSG weight (default: {default})", int(total_weight * 0.005))
    salt_weight = input_default("Total Salt weight (default: {default})", int((total_sodium - soy_weight * 0.06 - oyster_weight * 0.045 - msg_weight * 0.12) / 0.39))

    print("额外添加")
    print("水: ", water_weight)
    print("油: ", oil_weight)
    print("调料:")
    print("酱油: ", soy_weight)
    print("蚝油: ", oyster_weight)
    print("味精: ", msg_weight)
    print("盐: ", salt_weight)


if __name__ == "__main__":
    calc()
