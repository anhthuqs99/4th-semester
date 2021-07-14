#pragma warning(disable : 4996)

#include <iostream>
#include<cstring>

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
	char str[] = "thisisatest";
	char test[] = "";
	int res = my_strlen(str);

	cout << "my_strlen: " << res << endl;

	cout << str << test << " : " << res << endl;


	my_strncpy(test, str, res);
	cout << str << test << " : " << res << endl;

	return 0;
}
