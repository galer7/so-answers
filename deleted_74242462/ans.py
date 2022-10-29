def isWordSubject(word):
    return word in ['I', 'WE', 'THEY']


def isWordVerb(word):
    if word == 'KNOW':
        return True, 'present'
    if word == 'KNEW':
        return True, 'past'

    return False, None


def isWordThat(word):
    return word == 'THAT'


def isSentenceCorrect(s, prev=None, tense=None):
    if len(s) == 0:
        return True

    if len(s) == 1:
        now, rest = s[0], []
    else:
        if prev is None:
            now, *rest = s.split(' ')
        else:
            now, *rest = s

    if prev is None:
        if not isWordSubject(now):
            return False
        return isSentenceCorrect(rest, now, tense)

    if isWordSubject(prev):
        isNowVerb, nowTense = isWordVerb(now)
        if not isNowVerb or (tense is not None and tense == 'past' and tense != nowTense):
            return False

        return isSentenceCorrect(rest, now, nowTense)

    if isWordVerb(prev)[0]:
        if not isWordThat(now):
            return False

        return isSentenceCorrect(rest, now, tense)

    if isWordThat(prev):
        if not isWordSubject(now):
            return False

        return isSentenceCorrect(rest, now, tense)


print(isSentenceCorrect('I KNEW THAT THEY KNEW'))   # True
print(isSentenceCorrect('I KNEW THAT THEY KNOW'))   # False
print(isSentenceCorrect('I KNEW THEY KNEW'))        # False
