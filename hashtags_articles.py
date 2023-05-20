from session import session
from models import Article, Hashtag

def main():
    hashtag = session.query(Hashtag).get(6)
    print(f"Article with #{hashtag.name}")
    for article in hashtag.articles:
        print(article.title)


    print("-"*50)
    for article in session.query(Article).all():
        print(article.title)
        for hashtag in article.hashtags:
            print(f"   #{hashtag.name}")



if __name__ == '__main__':
    main()