public input
public string
public msg2

dseg segment para public 'data'
	msg1 db "Input string: $"
	msg2 db "8 first symbol: $"
	string db 127, ?, 128 dup(?)
dseg ends

cseg_func segment para public 'code'
	assume cs:cseg_func, ds:dseg
	
input proc far

	mov ax, dseg
	mov ds, ax
	
	lea dx, msg1
	mov ah, 09h
	int 21h
	
	mov ah, 0ah
	lea dx, string
	int 21h
	
	mov dl, 10
	mov ah, 02h
	int 21h
	
	ret
input endp
cseg_func ends
end