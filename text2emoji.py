import emojis

def word_to_emoji(word):
    res = emojis.db.get_emoji_by_alias(word)
    if res is None:
        return
    return res.emoji

def sentence_to_emoji(sentence):
    sentence = sentence.split()

    for i in range(len(sentence)):
        res = word_to_emoji(sentence[i].lower())
        if res is not None:
            sentence[i] = res

    return " ".join(sentence)









