def return_anagram(target: str, *candidates) -> list:
    target = target.strip().lower()
    anagrams = []

    def is_anagram(word1: str, word2: str) -> bool:
        word1 = sorted(word1.strip().lower())
        word2 = sorted(word2.strip().lower())

        return word1 == word2

    for word in candidates:
        if is_anagram(target, word):
            anagrams.append(word)

    return anagrams


print(return_anagram("stone", "tones", "banana", "tons", "notes", "Seton"))
