extrn input:far
extrn string:far
extrn msg2:far

stk segment para stack 'stack'
	db 100 dup(0)
stk ends

cseg segment para public 'code'
	assume cs:cseg, ss:stk

main:
	
	call input 
	
	lea dx, msg2
	mov ah, 09h
	int 21h
	
	mov ah, 02h
	lea si, string[2] ; address
	mov cx, 8
	print:
		mov dl, [si]
		int 21h
		mov dl, 32 ;space
		int 21h
		inc si
	loop print	
	
	mov ah, 4ch
	int 21h
	
cseg ends

end main