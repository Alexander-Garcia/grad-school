#lang racket
(define (check n)
(cond
  ((>= n 10) (if(<= n 100) #t #f))
)
)

(check 9)

