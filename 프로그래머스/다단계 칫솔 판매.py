def solution(enroll, referral, seller, amount):
    referral_dic = {}
    amount_dic = {name: 0 for name in enroll}

    for i in range(len(enroll)):
        referral_dic[enroll[i]] = referral[i]

    for i in range(len(seller)):
        name = seller[i]
        money = amount[i] * 100

        while name != "-" and money > 0:
            cur = money - money // 10
            give = money // 10 # 부모에게 줄 돈
            amount_dic[name] += cur
            name = referral_dic[name]
            money = give

    return [amount_dic[name] for name in enroll]
