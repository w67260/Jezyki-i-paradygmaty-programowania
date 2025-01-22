open System

type LinkedList<'T> =
    | Empty
    | Node of 'T * LinkedList<'T>

module LinkedList =

    let fromList (lst: 'T list) =
        let rec toLinkedList l = 
            match l with
            | [] -> Empty
            | head :: tail -> Node(head, toLinkedList tail)
        toLinkedList lst

    let rec printList list =
        match list with
        | Empty -> printfn ""
        | Node(value, next) ->
            printf "%A " value
            printList next

    let rec sumList list =
        match list with
        | Empty -> 0
        | Node(value, next) -> 
            match box value with
            | :? int as intValue -> intValue + sumList next
            | _ -> sumList next

    let rec reverse list =
        let rec reverseAcc acc lst =
            match lst with
            | Empty -> acc
            | Node(value, next) -> reverseAcc (Node(value, acc)) next
        reverseAcc Empty list

    let rec contains list value =
        match list with
        | Empty -> false
        | Node(v, next) when v = value -> true
        | Node(_, next) -> contains next value

    let rec findIndex list value index =
        match list with
        | Empty -> None
        | Node(v, next) when v = value -> Some index
        | Node(_, next) -> findIndex next value (index + 1)

    let rec countOccurrences list value =
        match list with
        | Empty -> 0
        | Node(v, next) when v = value -> 1 + countOccurrences next value
        | Node(_, next) -> countOccurrences next value

    let rec concatenate list1 list2 =
        match list1 with
        | Empty -> list2
        | Node(value, next) -> Node(value, concatenate next list2)

    let rec filter list predicate =
        match list with
        | Empty -> Empty
        | Node(value, next) when predicate value -> Node(value, filter next predicate)
        | Node(_, next) -> filter next predicate

    let rec removeDuplicates list =
        let rec remove acc lst =
            match lst with
            | Empty -> acc
            | Node(value, next) when contains acc value -> remove acc next
            | Node(value, next) -> remove (Node(value, acc)) next
        remove Empty list

    let rec partition list predicate =
        let rec partitionAcc acc1 acc2 lst =
            match lst with
            | Empty -> (acc1, acc2)
            | Node(value, next) when predicate value -> partitionAcc (Node(value, acc1)) acc2 next
            | Node(value, next) -> partitionAcc acc1 (Node(value, acc2)) next
        partitionAcc Empty Empty list


module Program =

    let displayMenu () =
        printfn "Wybierz opcję:"
        printfn "1. Sumuj elementy listy"
        printfn "2. Odwróć listę"
        printfn "3. Sprawdź, czy element znajduje się w liście"
        printfn "4. Znajdź indeks elementu"
        printfn "5. Zlicz wystąpienia elementu"
        printfn "6. Połącz dwie listy"
        printfn "7. Filtrowanie listy"
        printfn "8. Usuń duplikaty z listy"
        printfn "9. Podziel listę na dwie części"
        printfn "0. Wyjście"
        printf "Twój wybór: "

    let readUserList () =
        printf "Wprowadź elementy listy (oddzielone spacjami): "
        let input = Console.ReadLine()
        let elements = input.Split(' ') |> Array.toList
        LinkedList.fromList elements

    let main () =
        let mutable userList = LinkedList.Empty

        let rec loop () =
            displayMenu ()
            match Console.ReadLine() with
            | "1" ->
                printfn "Suma elementów listy: %d" (LinkedList.sumList userList)
                loop ()
            | "2" ->
                userList <- LinkedList.reverse userList
                printfn "Lista została odwrócona."
                loop ()
            | "3" ->
                printf "Podaj element do wyszukania: "
                let value = Console.ReadLine()
                if LinkedList.contains userList value then
                    printfn "Element znaleziony."
                else
                    printfn "Element nie znaleziony."
                loop ()
            | "4" ->
                printf "Podaj element, którego szukasz: "
                let value = Console.ReadLine()
                match LinkedList.findIndex userList value 0 with
                | Some(index) -> printfn "Indeks elementu: %d" index
                | None -> printfn "Element nie znaleziony."
                loop ()
            | "5" ->
                printf "Podaj element do zliczenia: "
                let value = Console.ReadLine()
                printfn "Element występuje %d razy." (LinkedList.countOccurrences userList value)
                loop ()
            | "6" ->
                printfn "Wczytaj pierwszą listę:"
                let list1 = readUserList ()
                printfn "Wczytaj drugą listę:"
                let list2 = readUserList ()
                let concatenatedList = LinkedList.concatenate list1 list2
                printfn "Połączona lista: "
                LinkedList.printList concatenatedList
                loop ()
            | "7" ->
                printf "Podaj warunek (np. > 5): "
                let condition = Console.ReadLine() |> int
                let filteredList = LinkedList.filter userList (fun x -> x |> int > condition)
                LinkedList.printList filteredList
                loop ()
            | "8" ->
                userList <- LinkedList.removeDuplicates userList
                printfn "Usunięto duplikaty."
                loop ()
            | "9" ->
                printf "Podaj warunek podziału: "
                let condition = Console.ReadLine() |> int
                let (part1, part2) = LinkedList.partition userList (fun x -> x |> int > condition)
                printfn "Część 1: "
                LinkedList.printList part1
                printfn "Część 2: "
                LinkedList.printList part2
                loop ()
            | "0" -> printfn "Zakończono działanie programu."
            | _ ->
                printfn "Nieznana opcja, spróbuj ponownie."
                loop ()

        loop ()

Program.main ()