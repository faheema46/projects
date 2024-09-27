import requests

# Function to search for books using the Google Books API
def search_google_books(book_title):
    api_url = "https://www.googleapis.com/books/v1/volumes"
    params = {"q": book_title, "maxResults": 5}  # You can adjust maxResults
    response = requests.get(api_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        books = data.get('items', [])
        if books:
            return books
        else:
            return None
    else:
        return None

# Function to generate a Google search link for finding PDF of the book
def generate_pdf_search_link(book_title):
    return f"https://www.google.com/search?q={book_title.replace(' ', '+')}+filetype:pdf"

# Main chatbot interaction function
def chatbot():
    print("Welcome to the PDF Book Finder!")
    while True:
        user_input = input("\nEnter the title of the book you're looking for (or type 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        # Search for books using Google Books API
        books = search_google_books(user_input)
        
        if books:
            print(f"\nFound {len(books)} book(s):")
            for index, book in enumerate(books):
                title = book['volumeInfo'].get('title', 'No Title')
                authors = ', '.join(book['volumeInfo'].get('authors', ['Unknown Author']))
                print(f"{index + 1}. {title} by {authors}")
                
            # Ask the user if they want to search for PDF
            selection = int(input("\nSelect the book you want to search a PDF for (enter the number): ")) - 1
            selected_book_title = books[selection]['volumeInfo'].get('title', 'No Title')
            search_link = generate_pdf_search_link(selected_book_title)
            print(f"\nYou can try searching for a PDF here: {search_link}")
        
        else:
            print("\nNo books found. Please try again with a different title.")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
