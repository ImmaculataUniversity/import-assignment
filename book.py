def write_book(chapters, *genres): #* will import all of the available genres
    #Summarizes the number of chapters and the genres of the book we are writing
    print(f"\nWriting a book with {chapters} chapters that fits the following genres:")
    for genre in genres:
        print(f"- {genre}")