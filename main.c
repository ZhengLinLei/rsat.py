#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

#define NUM_HIJOS 10

int main() {
    pid_t pid;
    int i;
    pid_t hijos[NUM_HIJOS];

    // Crear hijos
    for (i = 0; i < NUM_HIJOS; i++) {
        pid = fork();
        if (pid == 0) {
            // Proceso hijo
            char archivo[20];
            sprintf(archivo, "FACTOR%d.py", i);
            execlp("python3", "python3", archivo, NULL);
            exit(0); // Salir del hijo después de ejecutar el script de Python
        } else if (pid < 0) {
            // Error al crear el proceso hijo
            perror("fork");
            exit(1);
        } else {
            // Almacenar el PID del hijo en el array
            hijos[i] = pid;
        }
    }

    for (i = 0; i < NUM_HIJOS; i++) {
        printf("FACTOR_GEN%d.py [PID %d]\n", i, hijos[i]);
    }

    // Esperar a que un hijo termine
    int status;
    pid = wait(&status);

    // Matar a los demás hijos
    for (i = 0; i < NUM_HIJOS; i++) {
        if (hijos[i] != pid) {
            kill(hijos[i], SIGKILL);
        }
    }

    // Mostrar el PID del hijo que terminó primero
    printf("El hijo con PID %d terminó primero.\n", pid);

    return 0;
}
