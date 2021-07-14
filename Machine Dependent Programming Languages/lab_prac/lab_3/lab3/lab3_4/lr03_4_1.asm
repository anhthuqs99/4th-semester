PUBLIC X ;заставляет компоновщик соединить все сегменты с одинаковым именем
EXTRN exit: far ;Дальний (far) - на произвольный адрес (4 байта).

SSTK SEGMENT para STACK 'STACK'
	db 100 dup(0)
SSTK ENDS

SD1 SEGMENT para public 'DATA'
	X db 'X'
SD1 ENDS

SC1 SEGMENT para public 'CODE'
	assume CS:SC1, DS:SD1
main:	
	jmp exit ;Безусловный переход на адрес, указанный операндом
SC1 ENDS
END main