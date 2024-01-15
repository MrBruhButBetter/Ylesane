import praw
import credentials
import matplotlib.pyplot as plt

reddit = praw.Reddit(
    client_id = credentials.client_id,
    client_secret = credentials.client_secret,
    user_agent = "reddit::BgP1DPlYjIAeXXdd2P08kg (u/Null_Brain_cells)"
)


Black_Listed_Words = ["would","that's","what","good","why","did", "they", "like","|", "the", "i", "and", "to", "a", "of", "is", "this", "in", "an", "it", "then", "is", "for", "but", "or", "on", "my", "with", "that", "was", "if", "jus", "you", "are", "not", "have", "do", "be", "at", "by", "so", "we", "up", "out", "he", "she", "me", "him", "her", "its", "our", "your", "their", "from", "into", "over", "under", "just", "some", "about", "how", "can", "will", "get", "got", "has", "had"]
words = {}
for submission in reddit.subreddit("Minecraft").hot(limit=5):
    submission.comments.replace_more(limit=0)
    for comment in submission.comments:

        for word in comment.body.split():
            
            word = word.lower()
            if word in Black_Listed_Words: continue
            if words.get(word) == None:
                words[word] = 1
            else:
                words[word] += 1

sorted_words = dict(sorted(words.items(), key=lambda item: item[1], reverse=True))

top_10_words = dict(list(sorted_words.items())[:10])

print(top_10_words)

sorted_words = dict(sorted(words.items(), key=lambda item: item[1], reverse=True))
top_10_words = dict(list(sorted_words.items())[:10])


labels = top_10_words.keys()
sizes = top_10_words.values()

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.axis('equal')  


plt.savefig("pizza_diagram.jpg")
plt.show()