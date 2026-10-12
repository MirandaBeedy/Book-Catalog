
# Book Catalog Reflection

## Automated Test Failure

Test: test_book_list_displays_book

AssertionError: False is not true : Couldn't find 'Things We Never Got Over' in the following response

Ran 1 test in 0.088s

FAILED (failures=1)

The test failed because I temporarily changed the Books view so it would not display any books from the database. This showed that my test could detect when a book was missing from the page.

## Question 1: Foreign Keys
I put the ForeignKey in the Book model and connected it to the Publisher model. I did this because 1 Publisher can have multiple books Published by them. However, 1 book belongs to only 1 Publisher. If the relationship is reversed, Books and Publishers will not be displayed appropriately. 

## Question 2: Book Field Type
I chose IntegerField for the publication year because publication years are whole numbers, rather than words. This would eliminate the ease of sorting and comparing numericals when filtering through publication years.
