from session import session
from models import Article, Author


def main():
    # as we did before
    #   article = session.query(Article).get(1)
    #   author = session.query(Author).get(article.author_id)
    #   print(article, author)

    # as we do now. we have to add relationship to class Article
    article = session.query(Article).get(9)
    print(article, article.author)


if __name__ == '__main__':
    main()
