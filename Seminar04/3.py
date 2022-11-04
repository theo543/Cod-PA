from dataclasses import dataclass, replace

@dataclass(frozen=True)
class book:
    title: str
    authors: list[str]
    year_published: int
    price: int

def discount_old_books(books : list[book]):
    def update_price(b : book):
        if b.year_published < 2000:
            return replace(b, price=b.price*4//5)
        else: return b
    return map(update_price, books)

def revyear_title(b : book):
    return (-b.year_published, b.title)

def nrauthors_revprice(b : book):
    return (len(b.authors), -b.price)

def authorlastname_authorfirstname_title_year(b : book):
    names = b.authors[0].split(' ')
    return (names[1], names[0], b.title, b.year_published)

def main():
    print("Discounted:")
    books = [book("Calculus", ["Dan Anghel"], 1999, 140),
             book("English-Romanian Dictionary", ["Ava Smith"], 2000, 40),
             book("How to Install a Modem", ["Daria Anghel"], 1990, 30),
             book("Python Programming", ["Dora Baciu", "Maria Drăgănescu"], 2019, 300),
             book("Java Programming", ["Maria Drăgănescu", "Dan Baciu"], 1999, 400),
             book("C++ Programming", ["Maria Drăgănescu", "Dan Baciu"], 2010, 400),
             book("C++ Programming", ["Maria Drăgănescu", "Dan Baciu"], 2011, 400),
             book("Topology", ["Ștefan Costea"], 1999, 100)]
    print(*discount_old_books(books), sep='\n')
    print("Sort: decreasing year, title:")
    print(*sorted(books, key=revyear_title), sep='\n')
    print("Sort: number of authors, decreasing prices:")
    print(*sorted(books, key=nrauthors_revprice), sep='\n')
    print("Sort: last name of first author, first name of first author, title, year")
    print(*sorted(books, key=authorlastname_authorfirstname_title_year), sep='\n')
    pass

if __name__ == "__main__":
    main()
