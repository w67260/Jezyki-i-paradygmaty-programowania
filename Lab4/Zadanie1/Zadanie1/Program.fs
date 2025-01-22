open System

type UserData = { Weight: float; Height: float }

let calculateBMI weight height = weight / (height / 100.0) ** 2.0

let getBMICategory bmi =
    match bmi with
    | _ when bmi < 18.5 -> "Niedowaga"
    | _ when bmi >= 18.5 && bmi < 24.9 -> "Waga prawidłowa"
    | _ when bmi >= 25.0 && bmi < 29.9 -> "Nadwaga"
    | _ -> "Otyłość"

[<EntryPoint>]
let main argv =
    printfn "Witaj! Ten program oblicza Twoje BMI."
    printf "Podaj swoją wagę w kilogramach: "
    let weightInput = Console.ReadLine()
    printf "Podaj swój wzrost w centymetrach: "
    let heightInput = Console.ReadLine()

    try
        let weight = float weightInput
        let height = float heightInput

        let userData = { Weight = weight; Height = height }

        let bmi = calculateBMI userData.Weight userData.Height

        let category = getBMICategory bmi

        printfn "Twoje BMI wynosi: %.2f" bmi
        printfn "Kategoria BMI: %s" category
    with
    | :? FormatException ->
        printfn "Błąd: Wprowadzone dane muszą być liczbami."
    | ex ->
        printfn "Nieoczekiwany błąd: %s" ex.Message

    0