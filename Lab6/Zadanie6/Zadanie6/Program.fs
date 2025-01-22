open System

let replaceWord (inputText: string) (searchWord: string) (replaceWord: string) =
    inputText.Replace(searchWord, replaceWord)

let processText () =
    printfn "Podaj tekst:"
    let inputText = Console.ReadLine()

    printfn "Podaj słowo, które chcesz wyszukać:"
    let searchWord = Console.ReadLine()

    printfn "Podaj słowo, na które chcesz zamienić:"
    let newWord = Console.ReadLine()

    let modifiedText = replaceWord inputText searchWord newWord

    printfn "Zmodyfikowany tekst:"
    printfn "%s" modifiedText

processText ()
