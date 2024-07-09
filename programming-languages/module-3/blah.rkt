#lang racket
; write a racket two-way selection structure that produces a list '(9 9) when second element of a list named a_list is identical to the atom 'n and an empyt list otherwise
(define (check a_list)
  (if (eq? (cadr a_list) 'n)
      '(9 9)
      '())
  )
