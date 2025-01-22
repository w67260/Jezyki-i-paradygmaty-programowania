let rec hanoi n source target auxiliary =
    if n > 0 then
        hanoi (n - 1) source auxiliary target
        printfn "Przenieś dysk %d z %s na %s" n source target
        hanoi (n - 1) auxiliary target source



let hanoiIterative n source target auxiliary =
    let totalMoves = pown 2 n - 1
    let mutable moves = 0

    let mutable source = source
    let mutable target = target
    let mutable auxiliary = auxiliary

    if n % 2 = 0 then
        let temp = target
        target <- auxiliary
        auxiliary <- temp

    while moves < totalMoves do
        if moves % 3 = 0 then
            printfn "Ruch %d: Przenieś dysk z %s na %s" (moves + 1) source target
        elif moves % 3 = 1 then
            printfn "Ruch %d: Przenieś dysk z %s na %s" (moves + 1) source auxiliary
        else
            printfn "Ruch %d: Przenieś dysk z %s na %s" (moves + 1) auxiliary target

        moves <- moves + 1



hanoi 3 "A" "C" "B"
hanoiIterative 3 "A" "C" "B"