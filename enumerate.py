print()
print()
shopping = {
    "Piekarnia": ["chleb","pączek", "bułki",],
    "Warzywniak": ["marchew","seler", "rukola"]
}
for n, value in enumerate(shopping["Piekarnia"]):
    shopping["Piekarnia"][n] = value.title()
for n, value in enumerate(shopping["Warzywniak"]):
    shopping["Warzywniak"][n] = value.title()
print()
for i in shopping:
  print("Idę do", i, "kupuję tu następujące rzeczy:", shopping[i])
