type BankAccount(accountNumber: string, initialBalance: decimal) =
    member val AccountNumber = accountNumber with get, set
    member val Balance = initialBalance with get, set

    member this.Deposit(amount: decimal) =
        if amount > 0m then
            this.Balance <- this.Balance + amount
            printfn "Wpłata na konto %s wyniosła %.2f. Nowe saldo: %.2f" this.AccountNumber amount this.Balance
        else
            printfn "Kwota wpłaty musi być większa niż 0."

    member this.Withdraw(amount: decimal) =
        if amount > 0m && amount <= this.Balance then
            this.Balance <- this.Balance - amount
            printfn "Wypłata z konta %s wyniosła %.2f. Nowe saldo: %.2f" this.AccountNumber amount this.Balance
        else
            printfn "Niewystarczające środki na koncie lub błędna kwota wypłaty."

type Bank() =
    let mutable accounts = []

    member this.CreateAccount(accountNumber: string, initialBalance: decimal) =
        let newAccount = BankAccount(accountNumber, initialBalance)
        accounts <- newAccount :: accounts
        printfn "Utworzono konto o numerze %s z saldem %.2f." accountNumber initialBalance

    member this.GetAccount(accountNumber: string) =
        accounts |> List.tryFind (fun account -> account.AccountNumber = accountNumber)

    member this.UpdateAccount(accountNumber: string, newBalance: decimal) =
        match this.GetAccount(accountNumber) with
        | Some(account) -> 
            account.Balance <- newBalance
            printfn "Saldo konta %s zostało zaktualizowane na %.2f." accountNumber newBalance
        | None -> 
            printfn "Nie znaleziono konta o numerze %s." accountNumber

    member this.DeleteAccount(accountNumber: string) =
        match this.GetAccount(accountNumber) with
        | Some(account) -> 
            accounts <- List.filter (fun a -> a.AccountNumber <> accountNumber) accounts
            printfn "Konto o numerze %s zostało usunięte." accountNumber
        | None -> 
            printfn "Nie znaleziono konta o numerze %s." accountNumber

    member this.ListAccounts() =
        if accounts.Length > 0 then
            printfn "Lista kont bankowych:"
            accounts |> List.iter (fun account -> printfn "Numer konta: %s, Saldo: %.2f" account.AccountNumber account.Balance)
        else
            printfn "Brak kont w banku."

[<EntryPoint>]
let main argv =
    let bank = Bank()

    bank.CreateAccount("12345", 1000.00m)
    bank.CreateAccount("67890", 500.00m)

    bank.ListAccounts()

    let account = bank.GetAccount("12345")
    match account with
    | Some(a) -> 
        a.Deposit(500.00m)
        a.Withdraw(200.00m)
    | None -> printfn "Konto nie zostało znalezione."

    bank.UpdateAccount("67890", 1000.00m)

    bank.DeleteAccount("12345")

    bank.ListAccounts()

    0