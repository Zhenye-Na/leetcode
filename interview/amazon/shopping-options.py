# Shopping Options

# https://aonecode.com/amazon-online-assessment-shopping-options


def getNumberOfOptions(priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops, dollars):
    if not priceOfJeans or not priceOfShoes or not priceOfSkirts or not priceOfTops:
        return 0

    js = []
    for i in range(len(priceOfJeans)):
        for j in range(len(priceOfShoes)):
            js.append(priceOfJeans[i] + priceOfShoes[j])

    st = []
    for i in range(len(priceOfSkirts)):
        for j in range(len(priceOfTops)):
            st.append(priceOfSkirts[i] + priceOfTops[j])

    js.sort()
    st.sort()

    res = 0
    left, right = 0, len(st) - 1
    while left < len(js) and right >= 0:
        if js[left] + st[right] <= dollars:
            res += right - 0 + 1
            left += 1
        else:
            # js[left] + st[right] > dollars
            right -= 1

    return res
