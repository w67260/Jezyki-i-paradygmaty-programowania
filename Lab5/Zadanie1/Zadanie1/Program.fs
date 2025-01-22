let rec fibonacci n =
    match n with
    | 0 -> 0
    | 1 -> 1
    | _ -> fibonacci (n - 1) + fibonacci (n - 2)


let fibonacciTailRecursive n =
    let rec aux a b n =
        match n with
        | 0 -> a
        | 1 -> b
        | _ -> aux b (a + b) (n - 1)
    aux 0 1 n