# Создание базового класса "Транспортное средство" и его наследование для создания классов "Автомобиль" и "Мотоцикл".
# В классе "Транспортное средство" будут общие свойства, такие как максимальная скорость и количество колес,
# а классы-наследники будут иметь свои уникальные свойства и методы.

class Vehicle:
    def __init__(self, max_speed, num_wheels):
        self.max_speed = max_speed
        self.num_wheels = num_wheels

class Car(Vehicle):
    def __init__(self, max_speed, num_wheels, num_passengers):
        super().__init__(max_speed, num_wheels)
        self.num_passengers = num_passengers

class Motorcycle(Vehicle):
    def __init__(self, max_speed, num_wheels, engine_type):
        super().__init__(max_speed, num_wheels)
        self.engine_type = engine_type

car = Car(200, 4, 5)
motorcycle = Motorcycle(120, 2, "бензиновый")

print("Максимальная скорость автомобиля:", car.max_speed)
print("Количество колес мотоцикла:", motorcycle.num_wheels)
print("Тип двигателя мотоцикла:", motorcycle.engine_type)

section .text
    global _start

_start:
    mov eax, 2  ; a = 2
    mov ebx, 3  ; b = 3
    cmp eax, ebx  ; сравниваем a и b
    jge swap     ; если a >= b, переходим к swap
    jmp end      ; в противном случае переходим к end

swap:
    push eax     ; сохраняем a в стек
    push ebx     ; сохраняем b в стек
    mov eax, ebx ; a = b
    pop ebx      ; восстанавливаем b из стека
    pop edi      ; восстанавливаем a из стека
    mov edx, eax ; edx = a
    mul ebx      ; edx = a * b
    mov eax, edx ; eax = a * b
    mul 2        ; eax = 2 * (a * b)
    mov ebx, eax ; b = 2 * (a * b)
    mov eax, edx ; a = 2 * (a * b)

end:
    mov esi, eax  ; выводим a в консоль
    mov edi, MSG_A
    call write_int
    
    mov esi, ebx  ; выводим b в консоль
    mov edi, MSG_B
    call write_int

    mov eax, 0     ; код выхода из программы
    ret

section .data
MSG_A: db "a = %d"
MSG_B: db "b = %d", 10

section .bss
; Нет данных bss

section .rodata
; Нет данных rodata
