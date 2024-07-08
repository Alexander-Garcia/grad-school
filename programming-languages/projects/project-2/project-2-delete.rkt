#lang racket
; take a list and atom
; delete occurrences of the atom from the list
; returns the list result
(define (delete-atom lst atom)
  (cond
    ; make sure the list is a list
    [(not(list? lst)) '(ERROR: pass a list please)]
    ; if its null base case
    [(null? lst) '()]
    ; check if list is nested and trigger recursion on the nested list
    [(list? (car lst)) (cons (delete-atom (car lst) atom) (delete-atom (cdr lst) atom))]
    ; chop the first element and check it
    [(eq? (car lst) atom) (delete-atom (cdr lst) atom)]
    [else (cons (car lst) (delete-atom (cdr lst) atom))]
  )
)

'(Error for when list is not a list)
(delete-atom 1 1)

'(delete 1 from list (1))
(delete-atom '(1) 1)

'(delete 1 from list with nested list (1 2 (1 3) 3 4))
(delete-atom '(1 2 '(1 3) 3 4 ) 1)

'(delete 1 from INCEPTION - a list within a list within a list...the world isnt real)
(delete-atom '(1 '(1 '(1) 2) 2 3) 1)
