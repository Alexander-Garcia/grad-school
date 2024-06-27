#lang racket
(define (square x) (* x x))
'(output of square func)
(square 4)

(define (factorial n)
  (if (<= n 1)
    1
    (* n (factorial (- n 1)))
  )
)
'(output of factorial func)
(factorial 3)

(define (leap year)
  (cond
    ((zero? (modulo year 400)) #t)
    ((zero? (modulo year 100)) #f)
    (else (zero? (modulo year 4)))
  )
)

'(output of leap func)
(leap 1900)

; car returns first element of a list
`(output of car)
(car `(1 2 3))

; cdr returns the list minus the first element
`(output of cdr)
(cdr `(1 2 3))

; cons takes two arguments (item_to_add_to_list `())
; if both items are atoms it returns a dotted pair
'(output of cons)
(cons 1 `())

; testing 
'(output of const with car and cdr)
(define a_list `(1 2))
(cons (car a_list) (cdr a_list))


; like saying (cdr (cdr (car `((A (B C)) E F))
'(testing cddar)
(cddar `((A (B C)) E F))
