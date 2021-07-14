; square matrix
; count number of vowels in line
; write it on diagonal matrix 
extrn matrix_input: far
extrn matrix_print: far 

stk segment para stack 'stack'
	db 100 dup(0)
stk ends

cseg segment para public 'code' 
	assume cs:cseg, ss:stk 
	
main:
	call matrix_input
	call matrix_print 
	
	mov ah, 4ch
	int 21h 
cseg ends 
end main