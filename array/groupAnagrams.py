import collections


def groupAnagrams(strs):
    anagrams = collections.defaultdict(list)

    for word in strs:
        # 정렬하여 딕셔너리에 추가
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))