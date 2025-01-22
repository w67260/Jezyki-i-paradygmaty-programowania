open System

type Account = {
    AccountId: string
    Balance: decimal
}

let createAccount accountId initialBalance =
    { AccountId = accountId; Balance = initialBalance }

let deposit account amount =
    if amount > 0m then
        { account with Balance = account.Balance + amount }
    else
        account

let withdraw account amount =
    if amount > 0m && amount <= account.Balance then
        { account with Balance = account.Balance - amount }
    else
        account

let displayBalance account =
    printfn "Saldo konta %s: %.2f" account.AccountId account.Balance

[<EntryPoint>]
let main argv =
    let mutable accounts = Map.empty<string, Account>

    let rec menu () =
        printfn "\nMenu banku:"
        printfn "1. Utwórz konto"
        printfn "2. Depozytuj środki"
        printfn "3. Wypłać środki"
        printfn "4. Wyświetl saldo"
        printfn "5. Wyjdź"
        printf "Wybierz opcję: "
        match Console.ReadLine() with
        | "1" ->
            printf "Podaj ID konta: "
            let accountId = Console.ReadLine()
            printf "Podaj początkowe saldo: "
            let initialBalance = Console.ReadLine()
            try
                let balance = decimal initialBalance
                if balance >= 0m then
                    let newAccount = createAccount accountId balance
                    accounts <- accounts.Add(accountId, newAccount)
                    printfn "Konto zostało utworzone."
                else
                    printfn "Saldo początkowe musi być większe lub równe zero."
            with
            | :? FormatException -> printfn "Nieprawidłowa kwota."
            menu()

        | "2" ->
            printf "Podaj ID konta: "
            let accountId = Console.ReadLine()
            printf "Podaj kwotę do depozytu: "
            let depositAmount = Console.ReadLine()
            try
                let amount = decimal depositAmount
                match accounts.TryFind accountId with
                | Some account ->
                    let updatedAccount = deposit account amount
                    accounts <- accounts.Add(accountId, updatedAccount)
                    printfn "Depozyt zakończony sukcesem."
                | None -> printfn "Nie znaleziono konta o podanym ID."
            with
            | :? FormatException -> printfn "Nieprawidłowa kwota."
            menu()

        | "3" ->
            printf "Podaj ID konta: "
            let accountId = Console.ReadLine()
            printf "Podaj kwotę do wypłaty: "
            let withdrawAmount = Console.ReadLine()
            try
                let amount = decimal withdrawAmount
                match accounts.TryFind accountId with
                | Some account ->
                    if amount <= account.Balance then
                        let updatedAccount = withdraw account amount
                        accounts <- accounts.Add(accountId, updatedAccount)
                        printfn "Wypłata zakończona sukcesem."
                    else
                        printfn "Brak wystarczających środków na koncie."
                | None -> printfn "Nie znaleziono konta o podanym ID."
            with
            | :? FormatException -> printfn "Nieprawidłowa kwota."
            menu()

        | "4" ->
            printf "Podaj ID konta: "
            let accountId = Console.ReadLine()
            match accounts.TryFind accountId with
            | Some account -> displayBalance account
            | None -> printfn "Nie znaleziono konta o podanym ID."
            menu()

        | "5" ->
            printfn "Do widzenia!"

        | _ ->
            printfn "Nieprawidłowa opcja. Spróbuj ponownie."
            menu()

    menu()
    0