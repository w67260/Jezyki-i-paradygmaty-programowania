open System

let exchangeRates =
    Map [
        ("USD", "EUR"), 0.91
        ("USD", "GBP"), 0.75
        ("EUR", "USD"), 1.10
        ("EUR", "GBP"), 0.83
        ("GBP", "USD"), 1.33
        ("GBP", "EUR"), 1.20
    ]

let convertCurrency amount sourceCurrency targetCurrency =
    match exchangeRates.TryFind (sourceCurrency, targetCurrency) with
    | Some rate -> amount * rate
    | None ->
        printfn "Nieobsługiwana para walut: %s -> %s" sourceCurrency targetCurrency
        0.0

[<EntryPoint>]
let main argv =
    printfn "Witaj! Ten program konwertuje kwoty między walutami."
    printf "Podaj kwotę do przeliczenia: "
    let amountInput = Console.ReadLine()
    printf "Podaj walutę źródłową (USD, EUR, GBP): "
    let sourceCurrency = Console.ReadLine()
    printf "Podaj walutę docelową (USD, EUR, GBP): "
    let targetCurrency = Console.ReadLine()

    try
        let amount = float amountInput

        let convertedAmount = convertCurrency amount sourceCurrency targetCurrency

        if convertedAmount <> 0.0 then
            printfn "Przeliczona kwota: %.2f %s" convertedAmount targetCurrency
    with
    | :? FormatException ->
        printfn "Błąd: Wprowadzone dane muszą być liczbami."
    | ex ->
        printfn "Nieoczekiwany błąd: %s" ex.Message

    0