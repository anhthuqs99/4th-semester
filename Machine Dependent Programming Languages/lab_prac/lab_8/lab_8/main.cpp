#include <iostream>

using namespace std;

double average_asm(double* arr, int n)
{
    double result;
    __asm {
        push esi;

        mov esi, arr;
        mov ecx, n;
        
        fldz                                ; st(0) = 0.0
        loop_label:
        fadd qword ptr[esi]                 ; st(0) = st(0) + qword ptr [esi]
            add esi, 8                      ; double 8 byte
            loop loop_label;
        ; mantissa exponent
        fild n                              ; load integer
        fdivp st(1), st(0)                  ; st(1) = st(1) / st(0) and pop st(0)
                                            ; division with extraction from stack
        fstp result                         ; save f value with extraction from stack
 
        pop esi;
    }

    return result;
}

int main()
{
    /*
    double a = 3.5;
    double b = 4.0;
    double sum = 0;
    // calculate sum of a, b
    __asm {
        fld a; load floating value
        fld b;
        faddp st(1), st(0); addition with extraction from stack
        fstp sum; 
    }

    cout <<a <<" + "<<b<<" = "<<sum << "\n";
    */

    double arr[] = { 1.5, 2.5, 3};
    double ave = average_asm(arr, 3);

    cout <<"Average of array: "<< ave << "\n";


    return 0;
}


