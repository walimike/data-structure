def breakingRecords(scores):
    lowest, highest,high_record, low_record = 0,0,0,0
    for score in scores:
        print('====', score, highest, lowest)
        if highest == 0:
            highest = score
            lowest = score
        elif score > highest:
            highest = score
            high_record += 1
        elif score < lowest:
            lowest = score
            low_record += 1
        else:
            pass
    return high_record, low_record, highest, lowest

x=[0, 9, 3, 10, 2, 20]

print(breakingRecords(x))
