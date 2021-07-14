public num_print

fseg segment para public 'code' 
	assume cs:fseg 

num_print proc far 
	mov cx, 0 
	cmp bh, 0 
	je reverse ; unsigned
	;test bh, 1
	;jz reverse
	
	dec ax 
	not ax 
	mov bh, 0 
	
	push ax
	
	mov dl, "-" ; print sign
	mov ah, 02h 
	int 21h 
	
	pop ax
	
	reverse:
		mov dx, 0
		div bx 
		push dx 
		inc cx 
		cmp ax, 0 
		jne reverse 
		
		mov ah, 02h 

	print:
		pop dx 
		cmp dl, 9 
		jg change 
		add dl, "0" 
		jmp print_digit 
		
		change: 
			add dl, 57h 
		print_digit: 
			int 21h 
		loop print 
	
	ret 
num_print endp
fseg ends
end
	