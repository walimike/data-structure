def climbingLeaderboard(scores, alice):
    sorted_scores = sorted(set(scores), reverse=True)
    l = len(sorted_scores)
    for score in alice:
        while (l > 0) and (score >= sorted_scores[l-1]):
            l -= 1
        print (l+1)





x=[1,2,3,5,4,2]
# # print(sorted(set(x)))
# y=set(x)
# print(y.sort(reverse=True))
scores=[100,90,90,80,75,60]
# alice=[50,65,77,90,102]
alice=[55,65,77,90,102]
y=[100,100,50,40,40,20,10]
x =[5,25,50,120]
climbingLeaderboard(x,y)


# print(abs(sorted(x)[-1]))