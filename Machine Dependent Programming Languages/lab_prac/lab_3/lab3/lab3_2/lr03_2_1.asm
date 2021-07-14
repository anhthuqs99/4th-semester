STK SEGMENT para STACK 'STACK' ; PARA — сегмент начинается по адресу, кратному 16
	db 100 dup(0) ;dup: Для инициализации всех элементов массива одинаковыми значениями используется оператор DUP
	;db: 1byte
STK ENDS ; Директива ENDS определяет конец сегмента.

SD1 SEGMENT para common 'DATA'
	W dw 3444h ;dw: 2byte
SD1 ENDS
END
