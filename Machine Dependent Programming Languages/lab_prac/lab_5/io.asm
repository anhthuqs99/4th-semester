extrn str_to_num: far
extrn num_print: far

public number_input 
public number_output

dseg segment para public 'data' 
	buffer db 15, ?, 16 dup(?) 
	num dw 0 
dseg ends 

cseg2 segment para public 'code' 
	assume cs:cseg2, ds:dseg 

number_input proc far 
	mov ax, dseg 
	mov ds, ax 
	
	lea dx, buffer 
	mov ah, 0ah 
	int 21h 
	
	
	lea si, buffer[2] 
	
	call str_to_num
	
	mov [num], ax 
	
	mov dl, 10
	mov ah, 02h 
	
	ret 
number_input endp 

number_output proc far 
	mov ax, num 
	
	call num_print
	
	ret 
number_output endp 

cseg2 ends 
end