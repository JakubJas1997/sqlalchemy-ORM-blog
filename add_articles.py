from session import session
from models import Author, Article
from faker import Faker

def main():
    author = session.query(Author).get(2)
    fake = Faker()
    article = Article(
        title=fake.sentence(),
        content=fake.sentence()
    )

    author.articles.append(article)   # add article to articles table, author is chosen in first line of function main
    session.commit()



if __name__ == '__main__':
    main()