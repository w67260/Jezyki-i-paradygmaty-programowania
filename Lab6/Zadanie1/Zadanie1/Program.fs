open System

let countWordsAndChars (text: string) =
    let words = text.Split([| ' '; '\t'; '\n'; '\r' |], System.StringSplitOptions.RemoveEmptyEntries)
    let wordCount = words.Length
    
    let charCount = text.Replace(" ", "").Length
    
    printfn "Liczba słów: %d" wordCount
    printfn "Liczba znaków (bez spacji): %d" charCount

printfn "Podaj tekst:"
let inputText = Console.ReadLine()

countWordsAndChars inputText
