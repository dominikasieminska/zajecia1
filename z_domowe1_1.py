def bmi(masa,wzrost):
    bmi = round(masa/((wzrost/100)**2),2)
    return bmi

print(bmi(75,176))


def komentarz(bmi):

    if bmi < 18.5:
        komentarz = "niedowaga"

    elif bmi >= 18.5 and bmi <= 24.99 :
        komentarz = "wartość prawidłowa"

    else:
        komentarz = "nadwaga"

    return komentarz

print(komentarz(20))
print(komentarz(19))
print(komentarz(25))
