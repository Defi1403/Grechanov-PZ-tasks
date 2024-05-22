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
    mov ebx, [a]
    
    mov ecx, [b] 
    
    mov eax, ebx
    mul ecx
    mul [dvoika]
    cmp ebx, ecx
    jl if
    jmp else
if:
    mov ebx, eax
    ret
else:
    mov ecx, eax
    ret
    
    mov  edx, ebx
    mov  edx, 1
    mov  ebx, 1
    mov  eax, 4
    int 0x80

    mov  edx, ecx
    mov  edx, 1
    mov  ebx, 1
    mov  eax, 4
    int 0x80

section .data
a db 3
b db 4
dvoika db 2    mov esi, ebx  ; выводим b в консоль
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
