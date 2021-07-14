public str_to_num

fseg segment para public 'code' 
	assume cs:fseg 
	
str_to_num proc far 
	mov ax, 0 
	mov cx, 8 
	mov bh, 0 
	
	mov bl, [si] 
	cmp bl, '-' 
	pushf 
	jne next_digit 
	inc si 

	next_digit:
		mov bl, [si] 
		cmp bl, 0Dh ;
		je convert_end 
		cmp bl, ' '
		je convert_end 
		
		sub bl, "0" 
		mul cx 
		cmp dx, 0
		jne err
		
		add ax, bx 
		jc err 
		inc si 
		jmp next_digit 
	err:
		mov bl, 1 

	convert_end:
		popf 
		jne sign_end 
		mov bl, 0 
		cmp ax, 8000h 
		ja err2 
		not ax 
		inc ax 
		mov bh, 1
		jmp sign_end 
	err2: 
		 mov bl, 1
	sign_end:
		ret 
str_to_num endp 

fseg ends 

end