#Зертханалық жұмыс №5 — DevOps

# Тақырып
Жүйелік шақырулар және ядро ​​режимдері(strace, open/read/write/close).

# Мақсаты
- Жүйелік қоңыраулар қалай жұмыс істейтінін біліңіз.
- strace көмегімен оларды бақылауды үйреніңіз.
- Файлдармен жұмыс істеу үшін C және Python тілінде бағдарламалар жазу.
---

# 1. Анализ strace

### ls
- execve — запуск процесса.
- openat — открыть каталог.
- read — прочитать данные.
- write — вывод в stdout.

### cat /etc/passwd
- openat("/etc/passwd") — открыть файл.
- read — чтение содержимого.
- write — печать содержимого.
- close — закрыть файл.

### echo "Hello World"
- execve("/bin/echo")
- write(1, "Hello World\n", 12)
- exit_group()

### touch newfile.txt
- openat("newfile.txt", O_CREAT|O_WRONLY, 0666) — создать файл.
- close() — закрыть.
- futimens() — изменить атрибуты.

---

## 2. Программы

### C (c_code/file_ops.c)
```c
#include <fcntl.h>
#include <unistd.h>
#include <string.h>
#include <stdio.h>

int main() {
    int fd;
    char text[] = "Hello from C!\n";
    char buffer[100];

    fd = open("example.txt", O_CREAT | O_RDWR, 0644);
    write(fd, text, strlen(text));
    lseek(fd, 0, SEEK_SET);

    int n = read(fd, buffer, sizeof(buffer)-1);
    buffer[n] = '\0';
    printf("Файлдан оқылды: %s\n", buffer);

    close(fd);
    return 0;
}
