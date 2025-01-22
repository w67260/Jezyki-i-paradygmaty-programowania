let rec permutations list =
    match list with
    | [] -> [[]]
    | head :: tail ->
        let restPermutations = permutations tail
        [ for perm in restPermutations do
            for i in 0 .. List.length perm do
                yield List.insertAt i head perm ]


let numbers = [1; 2; 3]
let perms = permutations numbers

printfn "Permutacje listy:"
perms |> List.iter (fun perm -> printfn "%A" perm)