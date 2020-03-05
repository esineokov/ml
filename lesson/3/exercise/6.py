def int_func0(word):
    return str(word[0]).upper() + (str(word[1:] if len(word) > 1 else ""))


def int_func1(word):
    return str(word).title()


def int_func2(word):
    return str(word).lower().title()


def all_word_title(text):
    result = []
    for word in str(text).split():
        result.append(int_func2(word))
    return " ".join(result)


print(int_func0("hello"))
print(int_func1("hello"))
print(int_func2("hELLo"))
print(all_word_title("hello mY dEAr fRiEnD!"))
