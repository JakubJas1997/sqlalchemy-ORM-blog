from models import Author
from session import session

def main():
    for author in session.query(Author):
        for art in author.articles:
            print(author, art)

if __name__ == "__main__":
    main()
