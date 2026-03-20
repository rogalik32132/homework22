#include <iostream>
#include <string>
using namespace std;

struct Book {
    string title;
    string author;
    int year;
};

int main() {
    Book b;

    cout << "Enter title: ";
    cin >> b.title;

    cout << "Enter author: ";
    cin >> b.author;

    cout << "Enter year: ";
    cin >> b.year;

    cout << "\"" << b.title << "\" by " << b.author << " (" << b.year << ")";

    return 0;
}
