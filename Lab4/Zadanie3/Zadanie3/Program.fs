open System

let countWords (text: string) =
    text.Split([| ' '; '\t'; '\n' |], StringSplitOptions.RemoveEmptyEntries)
    |> Array.length

let countCharacters (text: string) =
    text.Replace(" ", "").Length

let mostFrequentWord (text: string) =
    text.Split([| ' '; '\t'; '\n'; '.'; ','; ';'; ':'; '!' |], StringSplitOptions.RemoveEmptyEntries)
    |> Array.map (fun word -> word.ToLowerInvariant())
    |> Array.countBy id
    |> Array.sortByDescending snd
    |> Array.tryHead

[<EntryPoint>]
let main argv =
    printfn "Witaj! Ten program analizuje wprowadzony tekst."
    printf "Podaj tekst do analizy: "
    let inputText = Console.ReadLine()

    let wordCount = countWords inputText
    let charCount = countCharacters inputText
    let frequentWord = mostFrequentWord inputText

    printfn "Liczba słów: %d" wordCount
    printfn "Liczba znaków (bez spacji): %d" charCount
    match frequentWord with
    | Some (word, count) -> printfn "Najczęściej występujące słowo: '%s' (wystąpiło %d razy)" word count
    | None -> printfn "Brak słów do analizy."
    0