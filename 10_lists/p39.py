scores = [75, 82, 91]

print(all(score >= 50 for score in scores))
print(any(score == 100 for score in scores))
