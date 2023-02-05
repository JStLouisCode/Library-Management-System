#Jared St Louis

#Imports
from T102_P5_load_data import *
from T102_check_equal import *

#Function Definitions

#Function 1 (sort_books_title)
def sort_books_title(dic: dict) -> list:
    
    """
    Return a list with the book data in a dictionary where books are sorted alphabetically by title.
    
    dic is a dictionary with many books.
    
    >>> sort_books_title(book_category_dictionary('google_books_dataset.csv'))
    [{'title': "'Salem's Lot", 'author': 'Stephen King', 'rating': 4.4, 'publisher': 'Hachette UK', 'pages': 300, 'language': 'English', 'category': ['Fiction', 'Thrillers']}, {'title': 'A Feast for Crows (A Song of Ice and Fire. Book 4)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 864, 'language': 'English', 'category': ['Fiction', 'Fantasy', 'Adventure', 'Epic']}, {'title': 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones. A Clash of Kings. A Storm of Swords. A Feast for Crows. A Dance with Dragons (A Song of Ice and Fire)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 4544, 'language': 'English', 'category': ['Fiction', 'Fantasy', 'Adventure', 'Epic']}, {'title': 'A Trace of Crime (a Keri Locke Mystery Book #4)', 'author': 'Blake Pierce', 'rating': 4.7, 'publisher': 'Blake Pierce', 'pages': 250, 'language': 'English', 'category': ['Fiction', 'Detective', 'Mystery']}, {another element}]
    
    """ 
    #convert dictionary to list
    list_books = dictionary_to_list(dic)
    
    #Bubble Sort Algo
    swap = True
    while swap:
        swap = False
        for i in range(len(list_books) -1):
            if list_books[i]['title'] > list_books[i+1]['title']:
                bubble_sort = list_books[i]
                list_books[i] = list_books[i+1]
                list_books[i+1] = bubble_sort
                swap = True
            
            
            elif list_books[i]['title'] == list_books[i+1]['title']: 
                if list_books[i]['title'] > list_books[i+1]['title']:
                    bubble_sort = list_books[i]
                    list_books[i] = list_books[i+1]
                    list_books[i+1] = bubble_sort
                    swap = True 
           
    return list_books

#Function 2 (sort_books_publisher)
def sort_books_publisher(dictionary: dict) -> list:
    """
    Returns sorted books in alphabetical order according to publisher and all the catagories in a list.
    
    dictionary is a dictionay with many books.
    
    >>> sort_books_publisher(book_category_dictionary("google_books_dataset.csv"))
    [{'title': 'Business Strategy (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 112, 'language': 'English', 'category': ['Economics', 'Business']}, {'title': 'Management (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 112, 'language': 'English', 'category': ['Economics', 'Management']}, {'title': 'Marketing (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 112, 'language': 'English', 'category': ['Economics']}, {'title': 'Personal Success (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 112, 'language': 'English', 'category': ['Economics', 'Business']}, {'title': 'The Essentials of Finance and Accounting for Nonfinancial Managers', 'author': 'Edward Fields', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 320, 'language': 'English', 'category': ['Economics', 'Business']}, {'title': 'Mrs. Pollifax Unveiled', 'author': 'Dorothy Gilman', 'rating': 3.9, 'publisher': 'Ballantine Books', 'pages': 208, 'language': 'English', 'category': ['Fiction', 'Detective']}, {'title': 'Eat That Frog!: 21 Great Ways to Stop Procrastinating and Get More Done in Less Time. Edition 3', 'author': 'Brian Tracy', 'rating': 4.7, 'publisher': 'Berrett-Koehler Publishers', 'pages': 144, 'language': 'English', 'category': ['Economics', 'Business']},{another element}]

    """
    #convert dictionary to list
    lst = dictionary_to_list(dictionary)
    
    #Bubble Sort Algo       
    n = len(lst)
    for i in range(n):
        for j in range(i+1,n):
            if (lst[i]["publisher"] > lst[j]["publisher"]):
                lst[i],lst[j] = lst[j],lst[i]
               
            elif (lst[i]["publisher"] == lst[j]["publisher"]):
                     
                if (lst[i]["title"] > lst[j]["title"]):
                    lst[i],lst[j] = lst[j],lst[i]
                    
    return lst

#Function 3 (sort_books_author)
def sort_books_author(dict_list: dict) -> list:
    """
    Return a list with the book data in a dictionary where books are sorted alphabetically by author name.
    
    dict_list is a dictionay with many books.
    
    >>> sort_books_author(book_category_dictionary("google_books_dataset.csv"))
    [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 'N/A', 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'language': 'English', 'category': ['Fiction', 'Detective', 'Mystery']}, {'title': "Edgedancer: From the Stormlight Archive", 'author': 'Brandon Sanderson', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': 226, 'language': 'English', 'category': ['Fiction']}, {another element}]
    
    >>> sort_books_ascending_rate(book_category_dictionary("google_books_dataset.csv"))
    [{'title': "Watchmen (2019 Edition)", 'author': 'Alan Moore', 'rating': 4.2, 'publisher': 'DC Comics', 'pages': 448, 'language': 'English', 'category': ['Comics']}, {'title': "Secrets of the Millionaire Mind: Mastering the Inner Game of Wealth", 'author': 'T. Harv Eker', 'rating': 4.6, 'publisher': 'Harper Collins', 'pages': 224, 'language': 'English', 'category': ['Economics']}, {another element}]
    """
    #convert dictionary to list
    lst = dictionary_to_list(dict_list) 
    
    n = len(lst)
    for i in range(n):
        for j in range(i+1,n):
            if (lst[i]["author"] > lst[j]["author"]):
                lst[i],lst[j] = lst[j],lst[i]
               
            elif (lst[i]["author"] == lst[j]["author"]):
                     #author equal , ;look at title
                if (lst[i]["title"] > lst[j]["title"]):
                    lst[i],lst[j] = lst[j],lst[i]
                    
    return lst

#Function 4 (sort_books_ascending_rate)
def sort_books_ascending_rate(library: dict) -> list:
    """
    Return a list with the book data stored as a dictionary where books are sorted by rate in ascending order.
    
    library is a dictionary with many books.
    
    >>> sort_books_ascending_rate(book_category_dictionary("google_books_dataset.csv"))
    [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 'N/A', 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'language': 'English', 'category': ['Fiction', 'Detective', 'Mystery']}, {'title': "Edgedancer: From the Stormlight Archive", 'author': 'Brandon Sanderson', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': 226, 'language': 'English', 'category': ['Fiction']}]
    
    >>> sort_books_ascending_rate(book_category_dictionary("google_books_dataset.csv"))
    [{'title': "Young Justice Vol. 1", 'author': 'Art Baltazar', 'rating': 4.1, 'publisher': 'DC', 'pages': 164, 'language': 'English', 'category': ['Comics']}, {'title': "The Malady and Other Stories: An Andrzej Sapkowski Sampler", 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 96, 'language': 'English', 'category': ['Fantasy']}]
     
    >>> sort_books_ascending_rate(book_category_dictionary("google_books_dataset.csv"))
    [{'title': "Watchmen (2019 Edition)", 'author': 'Alan Moore', 'rating': 4.2, 'publisher': 'DC Comics', 'pages': 448, 'language': 'English', 'category': ['Comics']}, {'title': "Secrets of the Millionaire Mind: Mastering the Inner Game of Wealth", 'author': 'T. Harv Eker', 'rating': 4.6, 'publisher': 'Harper Collins', 'pages': 224, 'language': 'English', 'category': ['Economics']}]
    """
    
    #convert dictionary to list
    new_list = dictionary_to_list(library)
    
    #Bubble Sort Algo
    n = len(new_list)
    for i in range(n):
        #if both is N/A, if one on the left is N/a, if one on the right is N/A, if both are not N/A, if both are the same value (look at title)
        for j in range(i+1, n): #i+1 moves up from the left side 
            #if both are N/A
            if new_list[i]['rating'] == "N/A" and new_list[j]['rating'] == "N/A":
                if new_list[i]['title'] > new_list[j]['title']:
                    new_list[i]['title'], new_list[j]['title'] = new_list[j]['title'], new_list[i]['title']
            
            #if one on the left is N/a
            elif new_list[i]['rating'] == "N/A":
                continue
            
            #if one on the right is N/A
            elif new_list[j]['rating'] == "N/A":
                new_list[i]['rating'], new_list[j]['rating'] = new_list[j]['rating'], new_list[i]['rating'] 
                
            #if both are the same value (look at title)
            elif new_list[i]['rating'] == new_list[j]['rating']:
                if new_list[i]['title'] > new_list[j]['title']:
                    new_list[i]['title'], new_list[j]['title'] = new_list[i]['title'], new_list[j]['title']                
               
            #if both are not N/A
            elif new_list[i]['rating'] > new_list[j]['rating']:
                new_list[i]['rating'], new_list[j]['rating'] = new_list[j]['rating'], new_list[i]['rating']
                
    return new_list

#Function 5 (dictionary_to_list)
def dictionary_to_list(library: dict) -> list:
    """
    Returns dictionary as a list.
    
    library is a dictionary with many books.
    
    >>> dictionary_to_list(book_category_dictionary("google_books_dataset.csv"))
    [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 'N/A', 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'language': 'English', 'category': ['Fiction', 'Detective', 'Mystery']}, {'title': "Edgedancer: From the Stormlight Archive", 'author': 'Brandon Sanderson', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': 226, 'language': 'English', 'category': ['Fiction']}, {another element}]
    
    """
    new_list = []
    for categories in library.keys():
        books = library.get(categories)
        for i in range(len(books)):
            books[i]['category'] = [categories]
        if len(new_list) == 0:
            new_list = books
        else:
            for book in books:
                book_in_list = False
                for i in range(len(new_list)):
                    if book['title'] == new_list[i]['title']:
                        new_list[i]['category'] += book['category']
                        book_in_list = True
                if book_in_list == False:
                    new_list += [book]    
                
    return new_list


#Main Script
def main():
    
   #Test for sort_books_title
    passed_tests = 0
    num_of_tests= 0
    
    
    passed_tests += check_equal("Testing sort_books_title.", sort_books_title(book_category_dictionary('test2.csv')), [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'language': 'English', 'category': ['Fiction']}, {'title': "The Malady and Other Stories: An Andrzej Sapkowski Sampler", 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 96, 'language': 'English', 'category': ['Fantasy']}, {'title': "Young Justice Vol. 1", 'author': 'Art Baltazar', 'rating': 4.1, 'publisher': 'DC', 'pages': 164, 'language': 'English', 'category': ['Comics']}])
    num_of_tests += 1
    
    failed_tests = num_of_tests - passed_tests
    
    print("num_of_tests is: " + str(num_of_tests))
    print("The total number of passed tests are: " + str(passed_tests))
    print("The total number of failed tests are: " + str(failed_tests))    
    print()

   #Test for sort_books_publisher 
    passed_tests = 0
    num_of_tests= 0
   
    passed_tests += check_equal("Testing sort_books_publisher.", sort_books_publisher(book_category_dictionary('test3.csv')), [{'title': "Riley Paige Mystery Bundle: Once Gone (#1) and Once Taken (#2)", 'author': 'Blake Pierce', 'rating': 4.5, 'publisher': 'Blake Pierce', 'pages': 250, 'language': 'English', 'category': ['Detective']}, {'title': "Watchmen (2019 Edition)", 'author': 'Alan Moore', 'rating': 4.2, 'publisher': 'DC Comics', 'pages': 448, 'language': 'English', 'category': ['Comics']}, {'title': "Secrets of the Millionaire Mind: Mastering the Inner Game of Wealth", 'author': 'T. Harv Eker', 'rating': 4.6, 'publisher': 'Harper Collins', 'pages': 224, 'language': 'English', 'category': ['Economics']}, {'title': "Night of the Bold (Kings and Sorcerers Book 6)", 'author': 'Morgan Rice', 'rating': 4.3, 'publisher': 'Morgan Rice', 'pages': 250, 'language': 'English', 'category': ['Fantasy']}])
    num_of_tests += 1
   
    failed_tests = num_of_tests - passed_tests
   
    print("num_of_tests is: " + str(num_of_tests))
    print("The total number of passed tests are: " + str(passed_tests))
    print("The total number of failed tests are: " + str(failed_tests))   
    print()
    
   #Test for sort_books_author
    passed_tests = 0
    num_of_tests= 0
    
    passed_tests += check_equal("Testing sort_books_author.", sort_books_author(book_category_dictionary('test2.csv')), [{'title': "The Malady and Other Stories: An Andrzej Sapkowski Sampler", 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 96, 'language': 'English', 'category': ['Fantasy']}, {'title': "Young Justice Vol. 1", 'author': 'Art Baltazar', 'rating': 4.1, 'publisher': 'DC', 'pages': 164, 'language': 'English', 'category': ['Comics']}, {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'language': 'English', 'category': ['Fiction']}])  
    num_of_tests += 1
    
    failed_tests = num_of_tests - passed_tests
    
    print("num_of_tests is: " + str(num_of_tests))
    print("The total number of passed tests are: " + str(passed_tests))
    print("The total number of failed tests are: " + str(failed_tests))
    print()
    
    #Test for sort_books_ascending_rate
    passed_tests = 0
    num_of_tests= 0
    
    passed_tests += check_equal("Testing sort_books_ascending_rate.", sort_books_ascending_rate(book_category_dictionary('test2.csv')), [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'language': 'English', 'category': ['Fiction']}, {'title': "Young Justice Vol. 1", 'author': 'Art Baltazar', 'rating': 4.1, 'publisher': 'DC', 'pages': 164, 'language': 'English', 'category': ['Comics']}, {'title': "The Malady and Other Stories: An Andrzej Sapkowski Sampler", 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 96, 'language': 'English', 'category': ['Fantasy']}])
    num_of_tests += 1
    
    failed_tests = num_of_tests - passed_tests
    
    print("num_of_tests is: " + str(num_of_tests))
    print("The total number of passed tests are: " + str(passed_tests))
    print("The total number of failed tests are: " + str(failed_tests))
    print()
    
#if __name__ == "__main__":
        #main()    
        


