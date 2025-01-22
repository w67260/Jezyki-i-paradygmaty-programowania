type Book(title: string, author: string, pages: int) =
    member this.Title = title
    member this.Author = author
    member this.Pages = pages

    member this.GetInfo() =
        sprintf "Tytuł: %s, Autor: %s, Liczba stron: %d" this.Title this.Author this.Pages

type User(name: string) =
    let mutable borrowedBooks = []

    member this.Name = name

    member this.BorrowBook(book: Book) =
        borrowedBooks <- book :: borrowedBooks
        printfn "%s wypożyczył książkę: %s" this.Name book.Title

    member this.ReturnBook(book: Book) =
        borrowedBooks <- List.filter (fun b -> b <> book) borrowedBooks
        printfn "%s zwrócił książkę: %s" this.Name book.Title

    member this.ListBorrowedBooks() =
        borrowedBooks |> List.map (fun b -> b.Title) |> String.concat ", "

type Library() =
    let mutable books = []

    member this.AddBook(book: Book) =
        books <- book :: books
        printfn "Dodano książkę: %s" book.Title

    member this.RemoveBook(book: Book) =
        books <- List.filter (fun b -> b <> book) books
        printfn "Usunięto książkę: %s" book.Title

    member this.ListBooks() =
        if books.Length > 0 then
            printfn "Książki w bibliotece:"
            books |> List.iter (fun book -> printfn "%s" (book.GetInfo()))
        else
            printfn "Biblioteka jest pusta."

[<EntryPoint>]
let main argv =
    let library = Library()
    let user = User("Jan Kowalski")

    let book1 = Book("W pustyni i w puszczy", "Henryk Sienkiewicz", 320)
    let book2 = Book("Pan Tadeusz", "Adam Mickiewicz", 240)
    let book3 = Book("Lalka", "Bolesław Prus", 460)
    
    library.AddBook(book1)
    library.AddBook(book2)
    library.AddBook(book3)

    library.ListBooks()

    user.BorrowBook(book1)
    user.BorrowBook(book2)

    printfn "Wypożyczone książki przez %s: %s" user.Name (user.ListBorrowedBooks())

    user.ReturnBook(book1)

    library.ListBooks()

    library.RemoveBook(book3)

    library.ListBooks()

    0