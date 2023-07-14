def generate_hashtag(s):
    if (len(s) == 0 or s == " " or len(s) > 140):
        return False
    else:
        m = "#"
        for i in s.title():
            if(i!=" "):
                m += i
        return m
