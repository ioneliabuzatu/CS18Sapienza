"""Transformation of a word to another one with same length where each intermediate belongs to an English dictionary.
All possible paths from start to end are found."""



from string import ascii_lowercase as alphabet

with open("/Users/ioneliabuzatu/Desktop/words.txt", "r") as f:   #file under the name words.txt
    text = {line.strip() for line in f}


class Solution(object):
    def findPathway(self, start_word, end_word, dictionary)
        def Path(path, word):
            if len(a[word]) == 0:
                result.append([word] + path)
                return
            path.insert(0, word)
            for w in a[word]:
                Path(path, w)
            path.pop(0)

        a = {}
        for word in dictionary:
            a[word] = []
        result = []
        cur_word = set()
        cur_word.add(start_word)

        while True:
            pre_word = cur_word
            cur_word = set()
            for word in pre_word:
                dictionary.remove(word)
            for word in pre_word:
                for i in range(len(start)):
                    left = word[:i]
                    right = word[i + 1:]
                    for char in alphabet:
                        if char != word[i]:
                            next_word = left + char + right
                            if next_word in dictionary:
                                a[next_word].append(word)
                                cur_word.add(next_word)
            if len(cur_word) == 0:
                return []
            if end_word in cur_word:
                break
        Path([], end_word)
        return result



test=Solution()
start = "head"
end = "tail"
for path in test.findPathway(start,end,text):
    print('-->'.join(path))
