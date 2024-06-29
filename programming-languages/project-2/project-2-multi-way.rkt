#lang racket
; area of equilateral triangle - sqrt 3 /4 * a**2 where a = length of side
; area of hexagon - 3 * sqrt(3) / 2 * a**2 where a = length of side

; helper functions
; square func
(define (squared x) (* x x))
; func for calculating eq triangle
(define (calc_eq_triangle sqrt3 a) (* (/ sqrt3 4) (squared a)))
; func for calculating are of hexagon
(define (calc_hexagon sqrt3 a) (* (/ (* sqrt3 3) 2) (squared a)))

; identifier determines if calculating area of triangle or hexagon
; 1 for triangle
; 2 for hexagon
; a = length of sides
(define (my_calc identifier a)
  (let (
        (sqrt3 1.732)
        )
      (cond
        ; if a is not integer
        [(not(integer? a)) #f]
        ; if a length of side isn't positive return false
        [(not(positive? a)) #f]
        ; calculate area of eq triangle
        [(eq? identifier 1) (calc_eq_triangle sqrt3 a)]
        ; calculate area of hexagon
        [(eq? identifier 2) (calc_hexagon sqrt3 a)]
        ; catch invalid input and return false
        [else #f]
      )
  )
)

'(Running my_calc multi-way selection structure: 1 and 5 as parameters)
(my_calc 1 5)

'(Running my_calc multi-way selection structure: 1 and -2 as parameters)
(my_calc 1 -2)

'(Running my_calc multi-way selection structure: atom a as both parameters)
(my_calc 'a 'a)

'(Running my_calc two-way selection structure: 3 and 5 parameters)
(my_calc 3 5)

'(Running my_calc multi-way selection structure: 2 and 5 as parameters)
(my_calc 2 5)

