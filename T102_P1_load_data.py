#Jared St Louis 

#Function Definition 
def book_category_dictionary (filename: str) -> dict:
 """
 Return a dictionary with the category as the key and everything else as values 
 in a list of dictionaires.
 
 filename is the name of the given file.
 
 >>> book_category_dictionary("google_books_dataset.csv")
 {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'language': 'English'}, {another element}
 """
 file = open(filename, 'r') #opens the file
    
 word_dict = dict()
    
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
            
 file.close() #Closes the file
        
 return word_dict

