score = 99
degree = ('D' if score <= 60 else
          'C' if 60 < score <= 80 else
          'B' if 80 < score <= 90 else
          'A' if 90 < score <= 100 else
          "Write a valid number between 0-100")
print(degree)
