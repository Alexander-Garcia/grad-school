#lang racket
; remove second and third element from list and return the list
(define (remove_second_and_third_element lst)
  (cond
    [(not(list? lst)) '(Error please pass a list)]
    [(null? lst) '()]
    [(null? (cdr lst)) '()]
    [(null? (cddr lst)) '() ]
    [else (cons (car lst) (cdddr lst))]
  )
)

'(type passed is not a list)
(remove_second_and_third_element 'a)

'(list less than 3 elements)
(remove_second_and_third_element '(1 3))

'(list of 3 elements (1 2 3))
(remove_second_and_third_element '(1 2 3))

'(list of 5 elements (1 2 3 4 5))
(remove_second_and_third_element '(1 2 3 4 5))
