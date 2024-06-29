#lang racket
(define (guess   s a_list)                                

     (cond

           ((null?  a_list)   '())

           ((eqv?  s  (car a_list))  a_list )

            (else  (guess  s  (cdr a_list)))

))

(guess '2 '(3 1 2 5))
