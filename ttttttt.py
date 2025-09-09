def backspaceCompare(s: str, t: str) -> bool:
    print(1)
    if len(s) == 0 and len(t) == 0:
        return True
    else:
        s1 = getString(s)
        print(s1)
        s2 = getString(t)
        print(s2)
    return compareString(s1, s2)


def getString(s: str) -> str:
    if len(s) == 0:
        return s
    right = 0
    len_str = len(s)
    result = []
    while right < len_str:
        if s[right] == '#':
            if len(result) > 0:
                result.pop(-1)
        else:
            result.append(s[right])
        right = right + 1
    print("Result: ", result)
    return str(result)


def compareString(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    left = 0
    len_str = len(s)
    while left < len_str:
        if s[left] != t[left]:
            return False
        left = left + 1
    return True

if __name__ == '__main__':
    s = "y#fo##f"
    t = "y#f#o##f"
    res = backspaceCompare(s, t)
    print(res)