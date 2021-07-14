#include <iostream>

extern "C" void my_strncpy(char* src, char* dst, const int len);

int my_strlen(char* string) {
	int len;

	__asm {
		mov edi, [string]
		xor ecx, ecx
		xor al, al
		not ecx
		repne scasb

		not ecx
		dec ecx
		
		mov len, ecx
	}

	return len;
}

int main(void) {
	char str[6] = "test";
	char test[6] = { 0 };
	int res = my_strlen(str);
	
	std::cout << "my_strlen:" << res << std::endl;

	my_strncpy(str, test, res);
	std::cout << "source: " << str <<std::endl;
	std::cout << "copy: "<< test << std::endl;

	return 0;
}
