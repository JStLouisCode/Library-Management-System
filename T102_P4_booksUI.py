#Jared St Louis 

#Imports
from T102_P5_load_data import *
from T102_P2_add_remove_search_dataset import *
from T102_P3_sorting_fun import *

#Refactor Functions 

#Function (Display menu)
def display_menu():
    """
    Displays sorted books.
    
    The available commands are:
    1- L)oad data
    2- A)dd book
    3- R)emove book
    4- G)et books
    T)itle R)ate A)uthor P)ublisher C)ategory
    5- GCT) Get all Categories for book Title
    6- S)ort books
    T)itle R)ate P)ublisher A)uthor
    7- Q)uit
    Please type your command: 
    """
    sort_or_not = input("The available commands are:  \n 1- L)oad Data \n 2- A)dd book \n 3- R)emove book \n 4- G)et book \n    T)itle R)ate A)uthor P)ublisher C)ategory \n 5- GCT) Get all Categories for book Title \n 6- S)ort books \n T)itle R)ate A)uthor P)ublisher \n Q)uit \n Please type your command: ").upper()
    return sort_or_not

#Function (If command is valid or not)
def validate_command(user_input: str) -> bool:
    """
    Returns True if users input is in list or False if user input is not in list.
    
    user_input is the user's input.
    
    >>> user_input('a')
    True
    >>> user_input('u')
    False
    """
    #list to check if commands are valid
    valid_commands = ['l', 'L', 'a', 'A', 'r', 'R', 'g', 'G', 'gct', 'GCT', 's', 'S', 'q', 'Q']
    return user_input in valid_commands

#Function Definitions

#UI Function
def UI():
    """
    Returns results of commands/subcommands executed.
    """    
    x = True
    y = False #data load

    #file not loaded shows up once
    while x == True:
        UserInput = display_menu()
        if validate_command(UserInput) == False: #call for validate_command
            print("Command does not exist. Try again.")
        #File Loading
        elif (UserInput == "L"):
            filename = input("Enter a file name: ")
            LoadedBooks = book_category_dictionary(filename)
            print("File loaded.")        
            y = True
        
        #allows user to quit and breaks loop
        elif UserInput.upper() == 'Q': 
                x = False 
        
        elif y == False:
            print("File has not been loaded yet. Please Try again.")         
                
        #(Add/Remove books)
        elif (UserInput == "A" ):
            if (y):
                title = input("title of the book: ") 
                author = input("author of the book: ")
                language = input("language of the book: ")
                publisher = input("publisher of the book: ")
                rating = input("rating of the book: ") 
                pages = input("number of pages in the book: ") 
                category = input("category of the book: ")
                
                bookList=[title, author, language, publisher, category, rating, pages]
                newBook_tuple = tuple(bookList)
                #call the function
                new_library = add_book(LoadedBooks, newBook_tuple)
                print(new_library) 
                x = False
                
        elif (UserInput == "R"):
            if (y):
                title = input("title of the book: ")
                category = input("category of the book: ")
                print(remove_book(LoadedBooks , title, category))
                x = False
                
        #Get books (title/rate/author/rate/publisher/category)
        
        elif UserInput.upper() == 'G' and y == True:
            exact_function = input('How do you want to get books? Type "T" to get books by title, "R" to get books by rate, "A" to get books by author, "P" to get books by publisher, "C" to get books by category: ') 
            
            if exact_function.upper() == 'T': # uses title function
                title = input("Please Enter title: ")
                print(get_books_by_title(LoadedBooks, title))
            elif exact_function.upper() == 'R': # uses rating function
                rate = str(input("Please Enter (integer) rate : "))
                print(get_books_by_rate(LoadedBooks, int(rate)))
            elif exact_function.upper() == 'A': # uses author function
                author = input("Please Enter author name: ")
                print(get_books_by_author(LoadedBooks, author))
            elif exact_function.upper() == 'P':
                publisher = input("Enter publisher: ") 
                print(get_books_by_publisher(LoadedBooks, publisher))  
            elif exact_function.upper() == 'C':
                category = input("Enter category: ") 
                print(get_books_by_category(LoadedBooks, category))              
            
            else:
                print("Command does not exist. Try again.") #if user types anything other than subcommands T, R, or A
        
        #Get all categories for book title
        
        elif UserInput == 'GCT' or UserInput == 'gct' and x == True:

                title = input("Enter a title: ")
                print(get_all_categories_for_book_title(LoadedBooks, title))
            
        #Sort books
        elif UserInput.upper() == 'S' and y == True:
            choose_sort = input('How do you want to sort? Type "T" to sort by title, "R" to sort by rate, "P" to sort by publisher, or "A" to sort by author: ')
            if choose_sort.upper() == "T":
                print(sort_books_title(LoadedBooks))
            elif choose_sort.upper() == "R":
                print(sort_books_ascending_rate(LoadedBooks))
            elif choose_sort.upper() == "P":
                print(sort_books_publisher(LoadedBooks))
            elif choose_sort.upper() == "A":
                print(sort_books_author(LoadedBooks))
            
            else:
                print("Command does not exist. Try again.") #if user types anything other than subcommands T, R, P, or A
                       
                                      
#Main Script
def main():  
    UI()
if __name__ == "__main__":
            main()    
