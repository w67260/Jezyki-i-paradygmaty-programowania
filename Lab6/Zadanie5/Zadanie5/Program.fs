open System

let findLongestWord (text: string) =
    let words = text.Split([| ' '; '\t'; '\n'; '\r' |], StringSplitOptions.RemoveEmptyEntries)
    
    let longestWord = 
        words |> Array.maxBy (fun word -> word.Length)
    
    longestWord

let processText () =
    printfn "Podaj tekst:"
    let inputText = Console.ReadLine()

    let longestWord = findLongestWord inputText
    
    printfn "Najdłuższe słowo: %s" longestWord
    printfn "Długość najdłuższego słowa: %d" longestWord.Length

processText ()
