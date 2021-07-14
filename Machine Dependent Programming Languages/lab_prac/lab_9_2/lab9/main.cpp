#include <iostream>

int main()
{
	char str[100] = { 0 };
	int sum = 0;
	std::cout << "Enter string: ";
	std::cin >> str;

	if (str[0] == 'a' and str[1] == 's' and str[2] == 'm')
	{
		//std::cout << "asm " << std::endl;
		for (int i = 3; str[i] != '\0'; i++)
			sum = sum + str[i];
		std::cout << "sum : " << sum << std::endl;
		if (sum == 200)
			std::cout << "OK";
		else
			std::cout << "FAILED";
	}
	else
		std::cout << "FAILED";

}