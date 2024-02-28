#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <signal.h>
#include <sys/stat.h>
#include <fcntl.h>

#define NUM_HIJOS 8

int main(int argc, char *argv[]) {

    if (argc != 2) {
        fprintf(stderr, "Uso: %s <número>\n", argv[0]);
        exit(1);
    }

    pid_t pid;
    int i;
    pid_t hijos[NUM_HIJOS];

    // Crear ./log si no existe
    if (access("./log", F_OK) == -1) {
        if (mkdir("./log", 0777) == -1) {
            perror("mkdir");
            exit(1);
        }
    }

    // Crear hijos
    for (i = 0; i < NUM_HIJOS; i++) {
        pid = fork();
        if (pid == 0) {
            // Proceso hijo
            char archivo[50];
            char log[30];
            sprintf(log, "./log/factor%d.log", i+1);
            int fd = open(log, O_WRONLY | O_CREAT | O_TRUNC, 0644);
            if (fd == -1) {
                perror("open");
                exit(1);
            }
            dup2(fd, 1);
            dup2(fd, 2);
            close(fd);
            sprintf(archivo, "FACTOR_GEN%d.py", i+1);
            execlp("python3", "python3", archivo, argv[1], NULL);
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
        printf("FACTOR_GEN%d.py [PID %d]\n", i+1, hijos[i]);
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
