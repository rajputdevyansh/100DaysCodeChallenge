# create a program to add a song and then
# first count total letter and total words
# Calculate word repetition

song = """
Oh, Father tell me, do we get what we deserve?
Whoa, we get what we deserve
And way down we go
Way down we go
Say way down we go
Way down we go
You let your feet run wild
Time has come as we all, oh, go down
Yeah but for the fall, ooh, my
Do you dare to look him right in the eyes? Yeah
Oh, 'cause they will run you down, down 'til the dark
Yes and they will run you down, down 'til you fall
And they will run you down, down 'til you go
Yeah, so you can't crawl no more
And way down we go
Way down we go
Say way down we go
Oh, 'cause they will run you down, down 'til you fall
Way down we go
Oh baby, yeah
Oh, baby
Baby
Way down we go
Yeah
And way down we go
Way down we go
Say way down we go, ooh
Way down we go
"""
print(song)
print(len(song))
print(song.split())
print(len(song.split()))
wc = {}
for w in song.split():
    if w in wc:
        wc[w] += 1
    else:
        wc[w] = 1
print(wc)

"""
Output:- 
714
['Oh,', 'Father', 'tell', 'me,', 'do', 'we', 'get', 'what', 'we', 'deserve?', 'Whoa,', 'we', 'get', 'what', 'we', 'deserve', 'And', 'way', 'down', 'we', 'go', 'Way', 'down', 'we', 'go', 'Say', 'way', 'down', 'we', 'go', 'Way', 'down', 'we', 'go', 'You', 'let', 'your', 'feet', 'run', 'wild', 'Time', 'has', 'come', 'as', 'we', 'all,', 'oh,', 'go', 'down', 'Yeah', 'but', 'for', 'the', 'fall,', 'ooh,', 'my', 'Do', 'you', 'dare', 'to', 'look', 'him', 'right', 'in', 'the', 'eyes?', 'Yeah', 'Oh,', "'cause", 'they', 'will', 'run', 'you', 'down,', 'down', "'til", 'the', 'dark', 'Yes', 'and', 'they', 'will', 'run', 'you', 'down,', 'down', "'til", 'you', 'fall', 'And', 'they', 'will', 'run', 'you', 'down,', 'down', "'til", 'you', 'go', 'Yeah,', 'so', 'you', "can't", 'crawl', 'no', 'more', 'And', 'way', 'down', 'we', 'go', 'Way', 'down', 'we', 'go', 'Say', 'way', 'down', 'we', 'go', 'Oh,', "'cause", 'they', 'will', 'run', 'you', 'down,', 'down', "'til", 'you', 'fall', 'Way', 'down', 'we', 'go', 'Oh', 'baby,', 'yeah', 'Oh,', 'baby', 'Baby', 'Way', 'down', 'we', 'go', 'Yeah', 'And', 'way', 'down', 'we', 'go', 'Way', 'down', 'we', 'go', 'Say', 'way', 'down', 'we', 'go,', 'ooh', 'Way', 'down', 'we', 'go']
165
{'Oh,': 4, 'Father': 1, 'tell': 1, 'me,': 1, 'do': 1, 'we': 18, 'get': 2, 'what': 2, 'deserve?': 1, 'Whoa,': 1, 'deserve': 1, 'And': 4, 'way': 6, 'down': 18, 'go': 14, 'Way': 7, 'Say': 3, 'You': 1, 'let': 1, 'your': 1, 'feet': 1, 'run': 5, 'wild': 1, 'Time': 1, 'has': 1, 'come': 1, 'as': 1, 'all,': 1, 'oh,': 1, 'Yeah': 3, 'but': 1, 'for': 1, 'the': 3, 'fall,': 1, 'ooh,': 1, 'my': 1, 'Do': 1, 'you': 9, 'dare': 1, 'to': 1, 'look': 1, 'him': 1, 'right': 1, 'in': 1, 'eyes?': 1, "'cause": 2, 'they': 4, 'will': 4, 'down,': 4, "'til": 4, 'dark': 1, 'Yes': 1, 'and': 1, 'fall': 2, 'Yeah,': 1, 'so': 1, "can't": 1, 'crawl': 1, 'no': 1, 'more': 1, 'Oh': 1, 'baby,': 1, 'yeah': 1, 'baby': 1, 'Baby': 1, 'go,': 1, 'ooh': 1}4

"""
