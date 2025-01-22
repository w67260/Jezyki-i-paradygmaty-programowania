open System

let removeDuplicates (words: string list) =
    words |> List.distinct

printfn "Podaj słowa oddzielone spacjami:"
let inputText = Console.ReadLine()

let wordsList = inputText.Split([| ' ' |], System.StringSplitOptions.RemoveEmptyEntries) |> List.ofArray

let uniqueWords = removeDuplicates wordsList

printfn "Unikalne słowa:"
uniqueWords |> List.iter (printfn "%s")
