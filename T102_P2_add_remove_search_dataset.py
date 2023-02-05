#Jared St Louis 

#Imports
from T102_P5_load_data import *

#8 Functions

#Function 1 (add_book)
def add_book(library: dict, newbook: tuple) -> dict:
    """
    Return the updated dictionary and print a message.
    
    library is a dictionary with many books, where the new book must be added.
    
    newbook is a tuple argument that has seven values giving information of the book. 
    
    >>> add_book(book_category_dictionary("google_books_dataset.csv"), ('Harry Potter', 'JK Rowling', 'English', 'Bloomsbury', 'Fiction', '8.9', '223'))
    {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'language': 'English'}, {another element}, {another element}, {'title': "Harry Potter", 'author': 'JK Rowling', 'rating': 8.9, 'publisher': 'Bloomsbury', 'pages': 223, 'language': 'English'}]}
    """
    title, author, language, publisher, category, rating, pages = newbook
    
    #create a dictionary to represent the new book
    newbook_dict = {}
    
    newbook_dict['title'] = title
    newbook_dict['author'] = author
    newbook_dict['language'] = language
    newbook_dict['publisher'] = publisher
    newbook_dict['rating'] = rating
    newbook_dict['pages'] = pages 
    
    if category in library:
        #add new book to the correct category in the old dictionary
        library[category].append(newbook_dict) #adds to list inside the dictionary.
    else: #for new category that is not in the dataset
        library[category] = []
        library[category].append(newbook_dict) #adds to list inside the dictionary.
    
    print("The book has been added correctly.")
    return library #Return new updated dictionary

#Function 2 (remove_book)
def remove_book(library: dict, booktitle: str, bookcat: str) -> dict:
    """
    Return the updated dictionary.
    
    library is a dictionary with many books, where a book must be removed.
    
    booktitle is the book's title.
    
    bookcat is the book's category.
    
    >>> remove_book(book_category_dictionary("google_books_dataset.csv"), 'Killer Blonde', 'Fiction')
    {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'language': 'English'}, {another element}, {one less element than before (not in dictionary)}
    """
    if bookcat in library: 
        books = library.get(bookcat)
        for book in books: 
            if booktitle == book['title']:
                books.remove(book)
                print("The book has been removed correctly")
                return library

    print("There was an error removing the book. Book not found.")
    return library

#Function 3 (get_books_by_category)
def get_books_by_category(dictionary: dict, data_category: str ) -> str:
    """
        Returns the total number of books in the category.
        
        dictionary is a dictionary with many books.
        
        data_category is the category to print.
        
        >>> get_books_by_category(book_category_dictionary("google_books_dataset.csv"),'Comics')
        The category Comics has 7  books. This is the list of books:
        Book 1 : Deadpool Kills the Marvel Universe by Cullen Bunn
        Book 2 : Young Justice Vol. 1 by Art Baltazar
        Book 3 : Ultimate Spider-Man Vol. 11: Carnage by Brian Michael Bendis
        Book 4 : Immortal Hulk Vol. 1: Or Is He Both? by Al Ewing
        Book 5 : Watchmen (2019 Edition) by Alan Moore
        Book 6 : The Joker by Brian Azzarello
        Book 7 : Venomized by Cullen Bunn
        """
    titles = []
    if data_category in dictionary:
        titles = dictionary.get(data_category)
        print("The category",data_category,"has",len(titles)," books. This is the list of books:")

        count=0
        for c in titles:
            count +=1
            c['author']
            c['title']
            print("Book",str(count),":", c['title'], "by",c['author'])
    return count

#Function 4 (get_books_by_rate)
def get_books_by_rate(library: dict, rate: int) -> int:
    """
    Return the number of books for the given rate.
    
    library is a dictionary with many books.
    
    rate is a positive integer. 
    
    >>> get_books_by_rate(book_category_dictionary("google_books_dataset.csv"), 3)
    8
    >>> get_books_by_rate(book_category_dictionary("google_books_dataset.csv"), 5)
    5
    >>> get_books_by_rate(book_category_dictionary("google_books_dataset.csv"), 6)
    0
    """
    rate_list = []
    new_list = []
    for i in library.keys():
        new_list = library.get(i)
        for book in new_list:
            if (book['rating'] != "N/A"):
                actual_rating = int(float(book['rating']))
                if actual_rating == rate:
                    if not (book in rate_list):
                        rate_list.append(book)
                    
    #count num of books between the specifc rate
    num_of_books = len(rate_list)
    print("There are",num_of_books,"books whose rate is between", rate,"and", rate + 1,". This is the list of books: ")
    
    #for loop stating which books rates are between x and y. referencing through Title
    booknum = 1
    for book in rate_list:
        print("Book",booknum,":", book['title'], "by", book['author'])
        booknum += 1
    return num_of_books


#Function 5 (get_books_by_title)
def get_books_by_title(dictionary: dict, title: str) -> str:
    """
    Returns whether the title of a book has been found or not with a boolean variable.
    
    dictionary is a dictionary with many books.
    
    title is the book's title.
    
    >>> get_books_by_title(book_category_dictionary('google_books_dataset.csv'), ('Edgedancer: From the Stormlight Archive'))
    True
    >>> get_books_by_title(book_category_dictionary('google_books_dataset.csv'), ('Tall Tales and Wee Stories: The Best of Billy Connolly'))
    True
      """
    
    for i in dictionary.keys():
        my_defined_list = dictionary.get(i)
        for book in my_defined_list:
            if book['title'] == title:
                print("The book has been found")
                return True           
                           
    print("The book has NOT been found")
    return False

#Function 6 (get_books_by_author)
def get_books_by_author(dictionary: dict, author: str) -> int: 
    """
    Returns the books written by the particular author.
    
    dictionary is a dictionary with many books.
    
    author is the author's full name.
    
    >>> get_books_by_author(book_category_dictionary('google_books_dataset.csv'), ('Barbara Allan')) 
    The author Barbara Allan has published the following books
    Book 1 : Antiques Roadkill: A Trash 'n' Treasures Mystery , rate: 3.3
    Book 2 : Antiques Con , rate: 4.8
    Book 3 : Antiques Chop , rate: 4.5
    Book 4 : Antiques Knock-Off , rate: 4.3
    """
    author_list = []
    defined_list = []
    for i in dictionary.keys():
        defined_list = dictionary.get(i)
        for book in defined_list:
            if (book['author'] != 'N/A'):
                scannedauthor = str(book['author'])
                if  scannedauthor == author:
                    if not (book in author_list):
                        author_list.append(book)
    space = ''                   
    theauthor = str(author)
    print('The author',theauthor,'has published the following books:')
    
    book_number = 1
    for book in author_list:
        print("Book", book_number,":", book['title'], ",", "rate:", book['rating']) 
        book_number += 1
    return len(author_list)

#Function 7 (get_books_by_publisher)
def get_books_by_publisher(dictionary: dict, data_publisher: str)-> int:
    
    """
    Returns the total number of books. 
    
    dictionary is a dictionary with many books.
    
    data_publisher is the publisher's name.
    
    >>> get_books_by_publisher(book_category_dictionary('google_books_dataset.csv'), "Kensington Publishing Corp.")
    2
    """
    title_aut = []
    pub_list = []
    for i in dictionary.keys():
        title_aut = dictionary.get(i)
        for book in title_aut:
            if (book['publisher'] != 'N/A'):
                om_pub = str(book['publisher'])
                if  om_pub == data_publisher:
                    if not (book in pub_list):
                        pub_list.append(book)
    pub1 = (data_publisher)
    print('The publisher',pub1,'has published the following books:')
        
    counter = 1
    for book in pub_list:
        print("Book", str(counter),":", book['title'], "by", "Author", book['author']) 
        counter += 1
        my_pub = ""
    return len(pub_list)

#Function 8 (get_all_categories_for_book_title)
def  get_all_categories_for_book_title(dict_name: dict, book_title: str ) -> int:

    """
    Returns the total number of books written by the author entered (author_name) considering every book which has the same title but in different category as one book.
    
    dict_name is a dictionary with many books.
    
    book_title is the book's title.
    
    >>> get_all_categories_for_book_title(book_category_dictionary('google_books_dataset.csv')
    2
    """
    categories = []
    for category in dict_name:
        for books in dict_name[category]:
            if book_title == books['title']:
                categories.append(category)
    num_of_cat = len(categories)
    print("The book title",book_title,"belongs to the following categories:")
    for i in range(len(categories)):
        print("Category",i+1,': "',categories[i])
                
    return len(categories)

#Main Script (Automated Testing)

def check_equal(description: str, outcome, expected) -> None:
    """
    Print a "passed" message if outcome and expected have same type and
    are equal (as determined by the == operator); otherwise, print a 
    "fail" message.
    
    Parameter "description" should provide information that will help us
    interpret the test results; e.g., the call expression that yields
    outcome.
    
    Parameters "outcome" and "expected" are typically the actual value returned
    by a call expression and the value we expect a correct implementation
    of the function to return, respectively. Both parameters must have the same
    type, which must be a type for which == is used to determine if two values
    are equal. Don't use this function to check if floats, lists of floats,
    tuples of floats, etc. are equal. 
    """
    
    outcome_type = type(outcome)
    expected_type = type(expected)
    if outcome_type != expected_type:
        
        # The format methods is explained on pages 119-122 of 
        # 'Practical Programming', 3rd ed.
        
        print("{0} FAILED: expected ({1}) has type {2}, " \
              "but outcome ({3}) has type {4}".
              format(description, expected, str(expected_type).strip('<class> '), 
                      outcome, str(outcome_type).strip('<class> ')))
        return False
    elif outcome != expected:
        print("{0} FAILED: expected {1}, got {2}".
              format(description, expected, outcome))
        return False
    else:
        print("{0} PASSED".format(description))
    print("------")
    return True

#Start Tests
def main():
   #Test for add_book
    x = add_book(book_category_dictionary("google_books_dataset.csv"), ('Harry Potter', 'JK Rowling', 'English', 'Bloomsbury', 'Fiction', '8.9', '223'))
    print(x)    
    print()
    
   #Test for remove_book
    x = remove_book(book_category_dictionary("google_books_dataset.csv"), 'Killer Blonde', 'Fiction')
    print(x)
    print() 
    
   #Test for get_books_by_category
    passed_tests = 0
    num_of_tests= 0
    
    passed_tests += check_equal("Testing get_books_by_category.", get_books_by_category(book_category_dictionary("google_books_dataset.csv"),'Comics')
 , 7)
    num_of_tests += 1
    
    failed_tests = num_of_tests - passed_tests
    
    print("num_of_tests is: " + str(num_of_tests))
    print("The total number of passed tests are: " + str(passed_tests))
    print("The total number of failed tests are: " + str(failed_tests))    
    print()

   #Test for get_books_by_rate 
    passed_tests = 0
    num_of_tests= 0
   
    passed_tests += check_equal("Testing get_books_by_rate.", get_books_by_rate(book_category_dictionary("google_books_dataset.csv"), 5) , 5)
    num_of_tests += 1
   
    failed_tests = num_of_tests - passed_tests
   
    print("num_of_tests is: " + str(num_of_tests))
    print("The total number of passed tests are: " + str(passed_tests))
    print("The total number of failed tests are: " + str(failed_tests))   
    print()
    
   #Test for get_books_by_title
    passed_tests = 0
    num_of_tests= 0
    
    passed_tests += check_equal("Testing get_books_by_title.",get_books_by_title(book_category_dictionary('google_books_dataset.csv'), ('Edgedancer: From the Stormlight Archive')), True)  
    num_of_tests += 1
    
    failed_tests = num_of_tests - passed_tests
    
    print("num_of_tests is: " + str(num_of_tests))
    print("The total number of passed tests are: " + str(passed_tests))
    print("The total number of failed tests are: " + str(failed_tests))
    print()
    
    #Test for get_books_by_author
    passed_tests = 0
    num_of_tests= 0
    
    passed_tests += check_equal("Testing get_books_by_author.", get_books_by_author(book_category_dictionary('google_books_dataset.csv'), ('Barbara Allan')) , 4)
    num_of_tests += 1
    
    failed_tests = num_of_tests - passed_tests
    
    print("num_of_tests is: " + str(num_of_tests))
    print("The total number of passed tests are: " + str(passed_tests))
    print("The total number of failed tests are: " + str(failed_tests))
    print()
    
    #Test for get_books_by_publisher
    passed_tests = 0
    num_of_tests= 0
    
    passed_tests += check_equal("Testing get_books_by_publisher.", get_books_by_publisher(book_category_dictionary('google_books_dataset.csv'), "Kensington Publishing Corp.")  , 2)
    num_of_tests += 1
    
    failed_tests = num_of_tests - passed_tests
    
    print("num_of_tests is: " + str(num_of_tests))
    print("The total number of passed tests are: " + str(passed_tests))
    print("The total number of failed tests are: " + str(failed_tests))
    print()    
    
    #Test for get_all_categories_for_book_title
    passed_tests = 0
    num_of_tests= 0
    
    passed_tests += check_equal("Testing get_all_categories_for_book_title.", get_all_categories_for_book_title(book_category_dictionary('google_books_dataset.csv'), ('Killer Blonde')) , 2)
    num_of_tests += 1
    
    failed_tests = num_of_tests - passed_tests
    
    print("num_of_tests is: " + str(num_of_tests))
    print("The total number of passed tests are: " + str(passed_tests))
    print("The total number of failed tests are: " + str(failed_tests))
    print()    
#if __name__ == "__main__":
        #main()    

    