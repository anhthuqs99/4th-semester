public matrix_input
public matrix_print

dseg segment para public 'data'
	N db ? 
	matrix db 81 dup(?) ; square matrix 9*9 
	buffer db 127, ?, 128 dup(?)
	vowels db "aeiou$" 
	msg1 db "Input size of matrix: $"
	msg2 db 10, "Input elements of matrix: ", 10, 13, "$" 
	msg3 db 10, "New matrix: ", 10, 13, "$"
dseg ends 

cseg_func segment para public 'code'
	assume cs:cseg_func, ds:dseg 

matrix_input proc far 
	mov ax, dseg 
	mov ds, ax 
	
	lea dx, msg1 ; print msg1
	mov ah, 09h 
	int 21h 
	
	mov ah, 01h
	int 21h
	sub al, "0"
	mov [N], al 
	
	lea dx, msg2 ; print msg2
	mov ah, 09h 
	int 21h 
	
	mov ch, 0 ; index row 
	mov di, 0 ; index elements 
	read_row:
		mov cl, 0 ; index column 
		
		lea dx, buffer
		mov ah, 0ah 
		int 21h
		
		lea si, buffer[2]
		mov ah, 0 ; counter
		
		read_column:
			mov al, [si] 
			mov matrix[di], al 
			;mov [matrix + di], al
			call count_vowels
			inc di 
			inc si 
			inc si ; ignore space 
			
			inc cl
			cmp cl, N 
			jne read_column 
		
		mov bx, di 
		sub bl, N 
		add bl, ch 
		add ah, "0"
		
		mov matrix[bx], ah ; count->diagonal
		
		mov dl, 10
		mov ah, 02h 
		int 21h 
		
		inc ch
		cmp ch, N 
		jne read_row 
	
	ret 
matrix_input endp 

matrix_print proc far 
	mov ax, dseg 
	mov ds, ax 
	
	lea dx, msg3 
	mov ah, 09h
	int 21h 
	
	mov ah, 02h
	
	mov ch, 0 ; index row
	mov si, 0 ; index elements
	
	print_row:
		mov cl, 0 ; index column
		
		print_column:
			mov dl, matrix[si] 
			int 21h 
			mov dl, ' ' ; print space
			int 21h 
			
			inc si 
			inc cl 
			cmp cl, N 
			jne print_column 
			
		mov dl, 10
		int 21h
		
		inc ch 
		cmp ch, N 
		jne print_row 
	ret
matrix_print endp

count_vowels proc near 
	push cx
	push di 
	
	mov cx, 5 
	lea di, vowels
	
	count:
		cmp al, [di] 
		je ok 
		
		inc di 
		loop count 
		jmp e_count 
	ok:
		inc ah 
	e_count:
		pop di 
		pop cx 
	
	ret 
count_vowels endp

cseg_func ends 
end
	