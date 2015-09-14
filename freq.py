#!/usr/bin/python

def freq(words):
    freq = {}
    for word in words:
        word = word.lower()
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

if __name__ == "__main__":
    print freq(["Hello", "hello", "this", "that", "how", "why", "helloo",
        "why"])
