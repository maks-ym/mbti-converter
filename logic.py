from typing import List


EI_MAP = {'e': "Extraverted",
          'i': "Introverted"}
FUNCTION_MAP = {'t': "Thinking",
                'n': "iNtuition",
                's': "Sensing",
                'f': "Feeling"}
POSSIBLE_VALUES = [f_ + ei_ for f_ in FUNCTION_MAP.keys() for ei_ in EI_MAP.keys()]


def mbti_type_correct(mbti_type: str) -> bool:
    """Check user input MBTI type correctness."""
    if mbti_type[0] not in ['E', 'I']:
        return False
    if mbti_type[1] not in ['N', 'S']:
        return False
    if mbti_type[2] not in ['T', 'F']:
        return False
    if mbti_type[3] not in ['P', 'J']:
        return False
    return True


def mbti2cf(mbti_type: str) -> List[str]:
    """
    Convert MBTI personality 4-letter code to Cognitive Function Stack.
    Using algorithm that can be used on a piece of paper.
    INTP -> Ti Ne Si Fe

    Steps from: https://www.psychologyjunkie.com/2018/04/01/decoding-your-myers-briggs-personality-type/
    """
    mbti_type = mbti_type.upper()
    res = ['',mbti_type[1],mbti_type[2],'']
    res[0] = 'S' if mbti_type[1] == 'N' else 'N'
    res[3] = 'T' if mbti_type[2] == 'F' else 'F'
    if mbti_type[-1] == "J":
        res = [res[i]+'e' if i % 2 == 0 else res[i]+'i' for i in range(4)]
    else:
        res = [res[i]+'i' if i % 2 == 0 else res[i]+'e' for i in range(4)]
    if mbti_type[0] == "E":
        res = res[1:] + [res[0]]
    else:
        res = res[2::-1] + [res[3]]
    return res


def explain_cogn_function(cog_fun: str) -> str:
    """
    Explain single cognitive function
    E.g. Te = Extraverted Thinking
    """
    if cog_fun.lower() in POSSIBLE_VALUES:
        return EI_MAP[cog_fun[1].lower()] + " " + FUNCTION_MAP[cog_fun[0].lower()]
    return "Somewhereverted Cognitive Function (Unknown for humans)"




def generate_all_mbti_types():
    """Generate all possible MBTI types"""
    res = []
    for ei_ in ['E', 'I']:
        for ns_ in ['N', 'S']:
            for tf_ in ['T', 'F']:
                for pj_ in ['P', 'J']:
                    res.append(ei_ + ns_ + tf_ + pj_)
    return res


if __name__ == "__main__":
    user_in = input("Te, Fe, etc: ")
    print(f"{user_in} - {explain_cogn_function(user_in)}")


    # print("All possible MBTI types:")
    # for mbti_type in generate_all_mbti_types():
    #     print(f"{mbti_type}: {mbti2cf(mbti_type)}")
