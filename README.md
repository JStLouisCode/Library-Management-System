# Library-Management-System

The Library Management System is a Python-based command-line application that allows users to manage a library of books. It provides various functionalities such as loading book data, adding and removing books, searching for books based on different criteria, getting all categories for a book title, sorting books, and quitting the program.

## Features

~ Load Data: The system allows users to load book data from a file. The supported file format and structure are specified in the 'T102_P5_load_data.py' file.

~ Add and Remove Books: Users can add new books to the library by providing details such as title, author, language, publisher, rating, pages, and category. They can also remove books from the library based on the title and category.

~ Search Books: Users can search for books in the library using various criteria, including title, rating, author, publisher, and category. The system provides functions to retrieve books that match the specified criteria.

~ Get All Categories for Book Title: Users can retrieve all the categories associated with a given book title.

~ Sort Books: The system allows users to sort the books in the library based on different attributes such as title, rating, publisher, and author. Sorting can be done in ascending or descending order.

## Installation

To use the Library Management System, follow these steps:

1. Ensure you have Python installed on your machine (version 3.5 or above).
2. Download the following files and place them in the same directory:
   ~ 'google_books_dataset(1).csv'
   ~ 'T102_P2_add_remove_search_dataset.py'
   ~ 'T102_P3_sorting_fun.py'
   ~ 'T102_P4_booksUI.py'
   ~ 'T102_P5_load_data.py'
3. Open a command-line interface and navigate to the directory where the files are located.
4. Run the following command to start the Library Management System:
   'python T102_P4_booksUI.py'

## Usage

Once the Library Management System is running, you can interact with it through the command-line interface. The system will display a menu of available commands and prompt you to enter your choice. Follow the on-screen instructions to perform various actions such as loading data, adding and removing books, searching for books, getting all categories for a book title, sorting books, and quitting the program.

Make sure to provide the required input in the specified format when prompted. Invalid inputs will be handled by displaying appropriate error messages.

## Dependencies 

The Library Management System does not have any external dependencies beyond Python itself. It is built using Python's standard library and does not require any additional packages or modules.
