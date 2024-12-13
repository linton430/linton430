words = text.lower().split()
word_counts = counter(words)
most_common = word_counts.most_common(5)
for word, count in most_common:
    print(f"{word}: {count}")
    word_counts
test_file = "textfile.txt"
#my best attempt i believe i went wrong around line 5
