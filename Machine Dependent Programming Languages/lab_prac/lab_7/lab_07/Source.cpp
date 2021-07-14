#pragma warning(disable : 4996)

#include <iostream>

using namespace std;

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
	char src[6] = "hello";
	char dest[6] = "";
	int res = my_strlen(src);
	
	cout << res << endl;

	my_strncpy(dest, src, res);
	cout << dest << " : " << res << endl;

	return 0;
}
