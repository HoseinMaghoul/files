from collections import Counter


def stop_words():
    with open("stopwords.txt", 'r', encoding='utf-8') as f:
        return f.read().split()


def count_words(fname, n):
    with open(fname, 'r', encoding='utf-8') as f:
        count = Counter(word for line in f
                        for word in line.split()
                        if word not in stop_words())
    return  count.most_common(n)

if __name__ == "__main__":
    words = count_words('sample.txt', 10)
    print(words)
