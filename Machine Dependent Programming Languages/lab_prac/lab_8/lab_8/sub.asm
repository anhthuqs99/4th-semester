.686
.MODEL FLAT, C
.STACK
.CODE
my_sub proc

	push ebp
	mov ebp, esp

	;fld qword ptr [ebp + 8]
	;fld qword ptr [ebp + 16]
	;fsubp st(1), st(0)
	;fstp qword ptr [ebp + 8]
	;mov eax,  [ebp + 8]

	movsd       xmm0,mmword ptr [ebp + 8]  
	movsd       xmm1,mmword ptr [ebp + 16] 
	psubq		xmm1, xmm0
	movsd       mmword ptr [eax],xmm1 
	
	pop ebp
	ret
my_sub endp
END