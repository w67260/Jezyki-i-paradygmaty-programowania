open System
open System.Linq

// Typ reprezentujący planszę gry typu "Kółko i Krzyżyk"
type Board = char array array

// Funkcja inicjalizująca pustą planszę
let createEmptyBoard () : Board =
    Array.init 3 (fun _ -> Array.create 3 ' ')

// Funkcja wyświetlająca planszę gry
let displayBoard (board: Board) =
    board
    |> Array.iteri (fun i row ->
        printfn "%s" (String.concat " | " (row |> Array.map string))
        if i < 2 then printfn "--+---+--")

// Funkcja sprawdzająca, czy na planszy znajduje się zwycięzca
let checkWinner (board: Board) : char option =
    let lines =
        [
            // Wiersze
            yield! board
            // Kolumny
            for col in 0..2 -> Array.map (fun row -> row.[col]) board
            // Przekątne
            yield [| board.[0].[0]; board.[1].[1]; board.[2].[2] |]
            yield [| board.[0].[2]; board.[1].[1]; board.[2].[0] |]
        ]
    lines
    |> List.tryFind (fun line -> line |> Array.distinct |> Array.length = 1 && line.[0] <> ' ')
    |> Option.map (fun line -> line.[0])

// Funkcja sprawdzająca, czy plansza jest pełna
let isBoardFull (board: Board) : bool =
    board |> Array.forall (Array.forall ((<>) ' '))

// Funkcja wykonywania ruchu
let makeMove (board: Board) (row: int) (col: int) (symbol: char) : bool =
    if board.[row].[col] = ' ' then
        board.[row].[col] <- symbol
        true
    else
        false

// Funkcja wybierająca losowy ruch dla komputera
let getComputerMove (board: Board) : (int * int) =
    let emptyCells =
        [ for i in 0..2 do
            for j in 0..2 do
                if board.[i].[j] = ' ' then yield (i, j) ]
    let random = System.Random()
    emptyCells.[random.Next(emptyCells.Length)]

// Główna funkcja gry
[<EntryPoint>]
let main argv =
    let board = createEmptyBoard()
    let mutable gameOver = false

    printfn "Witaj w grze 'Kółko i Krzyżyk'!"

    let rec gameLoop () =
        displayBoard board
        if not gameOver then
            printf "Twój ruch (podaj wiersz i kolumnę, np. 1 1): "
            let input = Console.ReadLine().Split(' ')
            try
                let row = int input.[0] - 1
                let col = int input.[1] - 1
                if row >= 0 && row < 3 && col >= 0 && col < 3 && makeMove board row col 'X' then
                    match checkWinner board with
                    | Some winner ->
                        displayBoard board
                        printfn "Gratulacje! Wygrałeś: %c" winner
                        gameOver <- true
                    | None ->
                        if isBoardFull board then
                            displayBoard board
                            printfn "Remis!"
                            gameOver <- true
                        else
                            let compRow, compCol = getComputerMove board
                            makeMove board compRow compCol 'O' |> ignore
                            match checkWinner board with
                            | Some winner ->
                                displayBoard board
                                printfn "Komputer wygrywa: %c" winner
                                gameOver <- true
                            | None ->
                                if isBoardFull board then
                                    displayBoard board
                                    printfn "Remis!"
                                    gameOver <- true
                else
                    printfn "Nieprawidłowy ruch. Spróbuj ponownie."
            with
            | :? System.Exception -> printfn "Błąd wejścia. Podaj wiersz i kolumnę w formacie 1 1."
            gameLoop()

    gameLoop()
    printfn "Gra zakończona. Dziękujemy za grę!"
    0
