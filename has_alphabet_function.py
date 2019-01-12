def has_alphabet(text):
    def worlds_list_upper(string):
        upper_string = string.upper()
        new_list = []
        for letra in upper_string:
            new_list.append(letra)
        return new_list
    text = worlds_list_upper(text)
    alfabeto = "A – B – C – D – E – F – G – H – I – J – K – L – M – N – O – P – Q – R – S – T – U – V – W – X – Y – Z "
    alfabeto = alfabeto.split(" – ")
    intersection = set(text).intersection(alfabeto)
    return intersection != set()
