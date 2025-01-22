open System

let isPalindrome (text: string) =
    let cleanText = text.Replace(" ", "").ToLower()
    cleanText = String(Array.rev (cleanText.ToCharArray()))

printfn "Podaj tekst:"
let inputText = Console.ReadLine()

if isPalindrome inputText then
    printfn "Tekst jest palindromem."
else
    printfn "Tekst nie jest palindromem."
