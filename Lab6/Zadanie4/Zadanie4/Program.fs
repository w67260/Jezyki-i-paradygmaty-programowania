open System

let convertFormat (input: string) =
    let parts = input.Split([| ';' |], System.StringSplitOptions.RemoveEmptyEntries)
    
    if parts.Length = 3 then
        let firstName = parts.[0].Trim()
        let lastName = parts.[1].Trim()
        let age = parts.[2].Trim()
        
        sprintf "%s, %s (%s lat)" lastName firstName age
    else
        "Błędny format danych"

let rec processEntries () =
    printfn "Podaj dane w formacie 'imię; nazwisko; wiek' (lub wpisz 'koniec' aby zakończyć):"
    let input = Console.ReadLine()
    
    if input.ToLower() = "koniec" then
        printfn "Zakończono wprowadzanie danych."
    else
        let formattedText = convertFormat input
        printfn "Przekształcony format: %s" formattedText
        processEntries ()

processEntries ()
