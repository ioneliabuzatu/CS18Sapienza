import collections
from string import ascii_lowercase as alphabet


def BuildGraph(english_dictionary):
    
    """Each word of an English dictionary is a node with undirected edge
    if one word could be converted to another by a single transformation:
    deleting a character, substituting a character, or inserting a character"""
    
    graph = collections.defaultdict(list)  #each word is a key with a value that designates the transformations of that word
    letters = alphabet
    for word in english_dictionary:
        for i in range(len(word)): 
            # deletion
            remove = word[:i] + word[i + 1:]
            if remove in english_dictionary:
                graph[word].append(remove)     
            # substitution
            for char in letters:
                change = word[:i] + char + word[i + 1:]
                if change in english_dictionary and change != word:
                    graph[word].append(change)        
        # insertion
        for i in range(len(word) + 1):
            for char in letters:
                add = word[:i] + char + word[i:]
                if add in english_dictionary:
                    graph[word].append(add)

    return graph

test=['damp', 'teal', 'camp', 'head', 'came', 'tea', 'lame', 'lime', 'like', 'heal']

# with open("/Users/ioneliabuzatu/Desktop/words.txt", "r") as f:
#     text = {line.strip() for line in f}

graph = BuildGraph(test)



def transform(graph, start_word, end_word):
    
    """It finds the shortest path from start_word to end_word"""
    
    paths = collections.deque([[start_word]])
    extended = set()
    # Breadth First Search
    while len(paths) != 0:
        current_Path = paths.popleft()
        current_Word = current_Path[-1]
        if current_Word == end_word:
            return current_Path
        elif current_Word in extended:
            # already extended this word
            continue

        extended.add(current_Word)
        transforms = graph[current_Word]
        for word in transforms:
            if word == end_word:    #avoiding unnecessary pushes in case our start is the root
                return current_Path[:] + [word]
            if word not in current_Path:
                # avoid loops
                paths.append(current_Path[:] + [word])

    # no transformation
    return[]


print('-->'.join(transform(graph, 'head', 'tea')))  
# it outputs ['head', 'tead', 'tea'], shortest path if the English dictionary is used instead of the list 'test'
