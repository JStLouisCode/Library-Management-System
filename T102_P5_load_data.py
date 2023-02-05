#Jared St Louis 

#Function Definition
def book_category_dictionary (filename :str) -> dict:
    """
    Return a dictionary with the category as the key and everything else as values 
    in a list of dictionaires.
 
    filename is the name of the given file.
 
    >>> book_category_dictionary("google_books_dataset.csv")
    {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'language': 'English'}, {another element}]}
    """
    file = open(filename, 'r') #opens the file
      
    word_dict = {}
       
    counter = 0
    for line in file: #[Repeatedly] reads the line
        #split into words
        word_list = line.split(',')
        if counter == 0:
            word_dict = {}
        else:
            if not word_list[5] in word_dict:
                word_dict[word_list[5]] = []
            book = {}
            book['title'] = word_list[0]
            book['author'] = word_list[1]
            book['rating'] = word_list[2]
            book['publisher'] = word_list[3]
            book['pages'] = word_list[4]
            book['language'] = word_list[6].replace('\n', "")
               
            word_dict[word_list[5]].append(book)

            book['pages'] = int(book['pages']) #change value of pages from str to int
            
            if (book['rating'] != "N/A"):
                book['rating'] = float(book['rating']) #change rating from str to float   
                
        counter += 1   
        
    
        #remove duplicates (in same category), use ranges length of books, for j in range i + 1

    for categories in word_dict.keys():
        books = word_dict.get(categories) #[{}]
        duplicates = [] #list of duplicates
        for book in range(len(books)): 
            for book2 in range(book + 1, len(books)):
                if (books[book]['title'] == books[book2]['title']):
                    duplicates.append(book2) #collecting indexes of duplicates and adding them to a list
        number_of_deletions = 0 #to prevent list from going out of range
        duplicates = set(duplicates) #created set to remove duplicate of indexes in list (ex. duplicate (business) = [5, 7, 7])
        for duplicate in duplicates:
            word_dict[categories].pop(duplicate-number_of_deletions) #remove duplicates from list
            number_of_deletions += 1
                   
    file.close() #Closes the file
                   
    return word_dict    


