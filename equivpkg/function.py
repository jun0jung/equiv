def check_reflexive(R):
    A = set(sum([[*i] for i in R], [])) # 세트에서 각 튜플을 언패킹한 후 리스트로 변환뒤 다시 세트로 변환
    count = 0
    for i in R:
        a, b = i
        if a==b:
            count += 1
    if count == len(A):
        return True
    else:
        return False

def check_symmetric(R):
    for i in R:
        a, b = i
        if a != b:
            if (a,b) in R and (b,a) in R:
                continue
            else: 
                return False
    return True

def check_transitive(R):
    result = True
    for i in R:
        a, b = i
        if a != b:
            for k in R:
                c, d = k
                if b == c:
                    if (a,d) in R:
                        result = True
                    else:
                        return False
    return result

def check_equivalance(R):
    return check_reflexive(R) and check_symmetric(R) and check_transitive(R)
