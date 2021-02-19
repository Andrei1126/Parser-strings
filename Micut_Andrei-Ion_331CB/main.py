# Micut Andrei-Ion, Grupa 331CB
import sys
import compute

# realizez scrierea in fisier si formatul dorit


def file_append(file1, array):
    string = ""
    for digit in array:
        string += str(digit) + " "
    file1.write(string + '\n')


# in interiorul acestei functii, voi retine in substring
# pattern-ul de cautat (cu ajutorul functiei strip(), ma asigur
# ca nu am spatii la final), iar in string, textul in care caut


if __name__ == "__main__":
    input_file = open(sys.argv[1])
    output_file = open(sys.argv[2], 'w')
    substring = input_file.readline().strip()
    string = input_file.readline()

    # algoritmul de analizare a sirurilor de caractere discutat la curs
    # o parte din codul prezentat ulterior a fost prezentat si pe slide-urile de curs
    array = []
    q = 0
    nr_chars = 91
    delta = compute.compute_delta(substring, nr_chars)
    for i in range(0, len(string)):
        q = delta[q][ord(string[i])]
        if q == len(substring):
            array.append(i - (len(substring) - 1))
    file_append(output_file, array)
    input_file.close()
    output_file.close()