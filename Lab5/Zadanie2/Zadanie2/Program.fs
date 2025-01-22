type 'a BinaryTree =
    | Empty
    | Node of 'a * 'a BinaryTree * 'a BinaryTree

let rec searchRecursive tree value =
    match tree with
    | Empty -> false
    | Node (v, left, right) ->
        if v = value then true
        else
            searchRecursive left value || searchRecursive right value

let searchIterative tree value =
    let rec loop stack =
        match stack with
        | [] -> false
        | Empty :: rest -> loop rest
        | Node (v, left, right) :: rest ->
            if v = value then true
            else loop (left :: right :: rest)
    loop [tree]


let tree =
    Node (10,
        Node (5, Empty, Empty),
        Node (15, Node (12, Empty, Empty), Node (20, Empty, Empty)))

let resultRecursive = searchRecursive tree 12
let resultIterative = searchIterative tree 12

printfn "Wynik rekurencyjny: %b" resultRecursive
printfn "Wynik iteracyjny: %b" resultIterative