#lang racket
(define (check n)
(cond
  ((< n 10) 1)
  ((<= n 100) 2)
  (else 3)
)
)

(check 101)

