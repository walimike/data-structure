def timeInWords(h, m):
    hour = int(h)
    minute = int(m)
    if minute == 0:
        return "{} o' clock".format(figure_to_words(hour))
    elif minute == 1:
        return "one minute past {}".format(figure_to_words(hour))
    elif minute == 15:
        return "quater past {}".format(figure_to_words(hour))
    elif minute == 45:
        return "quater to {}".format(figure_to_words(compute_am_pm(hour)))
    elif minute == 30:
        return "half past {}".format(figure_to_words(hour))
    elif 1 < minute < 30:
        return "{} minutes past {}".format(figure_to_words(minute),figure_to_words(hour))
    elif 30 < minute < 60:
        mins = 60 - minute
        if mins == 1:
            return  "one minute to {}".format(figure_to_words(compute_am_pm(hour)))
        return "{} minutes to {}".format(figure_to_words(mins),figure_to_words(compute_am_pm(hour)))

# def to_the_hour(hour):
#     if h

def compute_am_pm(hour):
    if hour == 12:
        return 1
    return hour + 1

def figure_to_words(figure):
    if figure == 1:
        return 'one'
    elif figure == 2:
        return 'two'
    elif figure == 3:
        return 'three'
    elif figure == 4:
        return 'four'
    elif figure == 5:
        return 'five'
    elif figure == 6:
        return 'six'
    elif figure == 7:
        return 'seven'
    elif figure == 8:
        return 'eight'
    elif figure == 9:
        return 'nine'
    elif figure == 10:
        return 'ten'
    elif figure == 11:
        return 'eleven'
    elif figure == 12:
        return 'twelve'
    elif figure == 13:
        return 'thirteen'
    elif figure == 14:
        return 'fourteen'
    elif figure == 15:
        return 'fifteen'
    elif figure == 16:
        return 'sixteen'
    elif figure == 17:
        return 'seventeen'
    elif figure == 18:
        return 'eighteen'
    elif figure == 19:
        return 'nineteen'
    elif figure == 20:
        return 'twenty'
    elif figure == 21:
        return 'twentyone'
    elif figure == 22:
        return 'twentytwo'
    elif figure == 23:
        return 'twentythree'
    elif figure == 24:
        return 'twentyfour'
    elif figure == 25:
        return 'twentyfive'
    elif figure == 26:
        return 'twentysix'
    elif figure == 27:
        return 'twentyseven'
    elif figure == 28:
        return 'twentyeight'
    elif figure == 29:
        return 'twenty nine'
    elif figure == 30:
        return 'thirty'
# for i in range(0,60):
print(timeInWords(6,35))