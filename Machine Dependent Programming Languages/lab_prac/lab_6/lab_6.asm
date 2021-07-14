.model tiny
.386 

code segment 
	assume cs:code, ds:code 
	org 100h ; size psp

start: 
	jmp INIT
		
	old dd 0 
	buf db ' 00:00:00 ', 0
	counter db 0 
	string db "Hello world!", 10
	
time proc 
	mov ah, al 
	and al, 15 
	shr ah, 4
	add al, '0' 
	add ah, '0' 
		
	mov buf[bx + 1], ah 
	mov buf[bx + 2], al 
	add bx, 3 
	ret 
time endp

clock proc 
	pushf ; put flags register in stack
	call cs:old 
	push ds
	push es
	push ax 
	push bx 
	push cx 
	push dx 
	push di 
	push cs 
	pop ds 
	
	mov ah, 2 
	int 1Ah 
	
	xor bx, bx 
	mov al, ch ;hours
	call time 
	mov al, cl ; min
	call time 
	mov al, dh ; sec
	call time 
	
	mov ax, 0B800h 
	mov es, ax 
	
	add counter, 1
	cmp counter, 157 ; max of line
	jbe newline 
	mov counter, 0 
	
newline:
	mov al, counter
	shr al, 1 
	shl al, 1 
	xor ah, ah 
	mov di, ax 
	mov al, ' '
	stosw
	cmp di, 137
	jae write
	
	mov ah, 0Eh  ;color of line
	push si 
	lea si, string 
	print_line:
		mov al, [si]
		inc si
		cmp al, 10
		je next
		stosw
		jmp print_line
next:
	pop si 
	xor di, di 
	xor bx, bx 
	mov ah, 1Dh ; color of time	
write: 
	mov al, buf[bx] 
	stosw
	inc bx 
	cmp buf[bx], 0 
	jnz write 
	
	pop di 
	pop dx 
	pop cx 
	pop bx 
	pop ax 
	pop es 
	pop ds 
	iret 
clock endp 
end_clock: 

INIT: 
	mov ax, 3h 
	int 10h 
	
	mov ax, 351Ch  ; get address of old handler
	int 21h 
	
	mov word ptr old, bx 
	mov word ptr old + 2, es 
	
	mov ax, 251Ch ; set address of current handler
	mov dx, offset clock 
	int 21h 
	
	mov ax, 3100h  ; resident program comlpete
	mov dx, end_clock - start + 10Fh
	shr dx, 4 ; / 16 
	mov dx, offset INIT
	int 27h 
	
code ends 
end start
	