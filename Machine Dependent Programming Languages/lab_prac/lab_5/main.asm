; Input unsigned octal number 
; Output Unsigned binary number 
; Output Signed hexadecimal number

extrn number_input: far 
extrn number_output: far

stk segment para stack 'stack' 
	db 100 dup(?) 
stk ends 

dseg segment para public 'data' 
	menu_print	db 10, 13
				db "1. Input number", 10, 13
				db "2. Unsigned binary", 10, 13
				db "3. Signed hexadecimal", 10, 13
				db "4. clear screen", 10, 13 
				db "0. exit ", 10, 13
				db "Input choice: $"
	in_msg	db "Input Number: $"
	out_msg	db "Converted number :$"
	func 	dw exit 
			dw input  
			dw bin_out
			dw hex_out
			dw clear_scr
dseg ends 

cseg segment para public 'code' 
	assume cs:cseg, ds:dseg, ss:stk 

main:
	mov ax, dseg 
	mov ds, ax 
	
	call clear_scr
	
	menu: 
		lea dx, menu_print
		mov ah, 09h 
		int 21h 
		
		mov ah, 01h 
		int 21h
		
		sub al, "0" 
		
		cmp al, 4
		ja menu
		
		xor ah, ah 
		add al, al 
		
		mov si, ax 
		
		call newline
	
		call word ptr func[si] 
		
		call newline
		jmp menu
		
exit proc near 
	call clear_scr
	mov ah, 4ch 
	int 21h
exit endp

input proc near
	call newline 
	lea dx, in_msg
	mov ah, 09h 
	int 21h 
	call number_input 
	call newline
	ret 
input endp

bin_out proc near 
	lea dx, out_msg
	mov ah, 09h 
	int 21h 
	
	mov bl, 2 ; base
	mov bh, 0 ;unsigned
	call number_output 
	ret
bin_out endp 

hex_out proc near 
	lea dx, out_msg
	mov ah, 09h 
	int 21h 
	
	mov bl, 16 ; base 
	mov bh, 1 ;signed
	call number_output
	ret 
hex_out endp
clear_scr proc near 
	mov ax, 3h ; clear screen
	int 10h
	ret 
clear_scr endp
newline proc near 
	mov dl, 10
	mov ah, 02h 
	int 21h
		
	mov dl, 13 
	mov ah, 02h 
	int 21h
	
	ret
newline endp
cseg ends
end main 