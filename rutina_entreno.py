# Este es un programa que sirve para generar una rutina de entreno (con estiramientos) a partir de unos días y horas
# Que el usuario proporciona al iniciar el programa
#Se recomienda ejecutar el programa en una terminal pura del sistema operativo correspondiente.
import os
from time import sleep
from random import shuffle
from copy import deepcopy


final_sprite = ("""
╔════════════════════════════════════════════════════════════════════════╗
║                  ▄▄▄███  TU RUTINA ESTA LISTA  ███▄▄▄                  ║
║                                                                        ║
║                     ██   █████  ██████    █    █████                   ║
║                    █  █  █    █   ██    ████  █                        ║
║                   ██████ █    █   ██   █    █  ████                    ║
║                   █    █ █    █   ██   █    █      █                   ║
║                   █    █ █████  ██████  ████  █████                    ║
║                                                                        ║
║            [==|=====|==]   ahora toca sudar   [==|=====|==]            ║
╚════════════════════════════════════════════════════════════════════════╝
""")

initial_sprite= ("""
╔════════════════════════════════════════════════════════════════════════╗
║            ▄▄▄███  GENERADOR DE RUTINAS DE ENTRENO  ███▄▄▄             ║
║                                                                        ║
║ █████  ██████ ██████ █    █ █    █ ██████ █    █ ██████ █████   ████   ║
║ █    █   ██   █      ██   █ █    █ █      ██   █   ██   █    █ █    █  ║
║ █████    ██   ████   █ ██ █ █    █ ████   █ ██ █   ██   █    █ █    █  ║
║ █    █   ██   █      █   ██  █  █  █      █   ██   ██   █    █ █    █  ║
║ █████  ██████ ██████ █    █   ██   ██████ █    █ ██████ █████   ████   ║
║                                                                        ║
║         [==|=====|==]   entrena listo, no duro   [==|=====|==]         ║
╚════════════════════════════════════════════════════════════════════════╝
""")
days_sprite = ("""
╔════════════════════════════════════════════════════════════════════════╗
║                       ─────  PASO 1 DE 2  ─────                        ║
║                                                                        ║
║                      █████     █     ██    █████                       ║
║                      █    █ ██████  █  █  █                            ║
║                      █    █   ██   ██████  ████                        ║
║                      █    █   ██   █    █      █                       ║
║                      █████  ██████ █    █ █████                        ║
║                                                                        ║
║                 ¿cuantos dias vas a pisar el gimnasio?                 ║
╚════════════════════════════════════════════════════════════════════════╝
""")

time_sprite = ("""
╔════════════════════════════════════════════════════════════════════════╗
║                       ─────  PASO 2 DE 2  ─────                        ║
║                                                                        ║
║            █    █ ██████ █    █ █    █ ██████  ████   █████            ║
║            ██  ██   ██   ██   █ █    █   ██   █    █ █                 ║
║            █ ██ █   ██   █ ██ █ █    █   ██   █    █  ████             ║
║            █    █   ██   █   ██ █    █   ██   █    █      █            ║
║            █    █ ██████ █    █  ████    ██    ████  █████             ║
║                                                                        ║
║                   ¿cuanto tiempo tienes cada sesion?                   ║
╚════════════════════════════════════════════════════════════════════════╝
""")

calentamiento_sprite = (r"""
╔════════════════════════════════════════════════════════════════════════╗
║           ─────  {} MINUTOS AL INICIO DE CADA SESION  ─────            ║
║                                                                        ║
║    ███  ██  █    ████ █  █ ████  ██  █   █ ████ ████ █  █ ████  ██     ║
║   █    █  █ █    █    ██ █  ██  █  █ ██ ██  ██  █    ██ █  ██  █  █    ║
║   █    ████ █    ███  █ ██  ██  ████ █ █ █  ██  ███  █ ██  ██  █  █    ║
║   █    █  █ █    █    █  █  ██  █  █ █   █  ██  █    █  █  ██  █  █    ║
║    ███ █  █ ████ ████ █  █  ██  █  █ █   █ ████ ████ █  █  ██   ██     ║
║                                                                        ║
║            \o/         o         \o/         o         \o/             ║
║             |         /|\         |         /|\         |              ║
║            / \        / \        / \        / \        / \             ║
║                                                                        ║
║                     muevete antes de moverlo todo                      ║
╚════════════════════════════════════════════════════════════════════════╝
""")

training_sprite=(r"""
╔════════════════════════════════════════════════════════════════════════╗
║                     ─────  TU PLAN SEMANAL  ─────                      ║
║                                                                        ║
║   ████ █  █ ████ ███  ████ █  █  ██  █   █ ████ ████ █  █ ████  ██     ║
║   █    ██ █  ██  █  █ █    ██ █ █  █ ██ ██  ██  █    ██ █  ██  █  █    ║
║   ███  █ ██  ██  ███  ███  █ ██ ████ █ █ █  ██  ███  █ ██  ██  █  █    ║
║   █    █  █  ██  █ █  █    █  █ █  █ █   █  ██  █    █  █  ██  █  █    ║
║   ████ █  █  ██  █  █ ████ █  █ █  █ █   █ ████ ████ █  █  ██   ██     ║
║                                                                        ║
║                 [==|==]           o           [==|==]                  ║
║                    |             /|\             |                     ║
║                   / \            / \            / \                    ║
║                                                                        ║
║                        una serie mas y lo dejo                         ║
╚════════════════════════════════════════════════════════════════════════╝
""")

txt_sprite=(r"""
    ________________________________________________________________
    |                                                            \
    |                                                             \
    |                                                              |
    |  ████ █   █ ████    ███ █  █  ██  ███  ███   ██  ███   ██    |
    |   ██   █ █   ██    █    █  █ █  █ █  █ █  █ █  █ █  █ █  █   |
    |   ██    █    ██    █ ██ █  █ ████ ███  █  █ ████ █  █ █  █   |
    |   ██   █ █   ██    █  █ █  █ █  █ █ █  █  █ █  █ █  █ █  █   |
    |   ██  █   █  ██     ███  ██  █  █ █  █ ███  █  █ ███   ██    |
    |                                                              |
    |     ____________________________________________________     |
    |     ____________________________________________________     |
    |     ____________________________________________________     |
    |     ____________________________________________________     |
    |                                                              |
    |______________________________________________________________|
""")

einstein_sprite=(r"""
       -''--.
       _`>   `\.-'<
    _.'     _     '._
  .'   _.='   '=._   '.
  >_   / /_\ /_\ \   _<
    / (  \o/\\o/  ) \
    >._\ .-,_)-. /_.<
        /__/ \__\ 
          '---'     E=mc^2

""")


def assign_exercises(training_days, training_minutes,exercises_training_time):

    exercise_number = ((training_minutes -exercises_training_time)// 5)
    exercise_list, calentamiento_list = get_exercise_list()

    # get muscular groups name and shuffle it
    training = {}
    muscular_groups = list(exercise_list)
    shuffle(muscular_groups)

    #get warn up
    diccionario_warn_up = get_warn_up(calentamiento_list, exercises_training_time)

    for day in range(training_days):
        training.update({"Día_{}".format(day+1): {}})

    for index, valor in enumerate(muscular_groups):
        distribute_muscular_groups = index % training_days
        training["Día_{}".format(distribute_muscular_groups+1)].update({muscular_groups[index]: []})
    training = assign_exercises_to_days(exercise_number, training, exercise_list)
    return training, diccionario_warn_up


def get_warn_up(calentamiento_list, exercises_training_time):
    # get the 10 minutes warn-up
    exercises_training = int(exercises_training_time/5)
    warn_up_groups = list(calentamiento_list)
    copy_warn_up = deepcopy(calentamiento_list)
    shuffle(warn_up_groups)
    warn_up = []
    for x in range(exercises_training):
        distribute_warn_up = x % len(warn_up_groups)

        name_warn_up = copy_warn_up[warn_up_groups[distribute_warn_up]]
        if not name_warn_up:
            copy_warn_up[warn_up_groups[distribute_warn_up]] = (deepcopy(calentamiento_list[warn_up_groups[distribute_warn_up]]))
            shuffle(name_warn_up)

        warn_up.append(name_warn_up.pop())

    diccionario_warn_up = {"calentamiento({} minutos x día)".format(exercises_training_time): warn_up}
    return diccionario_warn_up


def assign_exercises_to_days(exercise_number, training, exercise_list):

    for day_name, groups in training.items():

        processed_exercises = list(groups.keys())

        copy_exercise_list = deepcopy(exercise_list)

        for clave in copy_exercise_list.values():
            shuffle(clave)

        # Repartir ejercicios

        for exercise in range(exercise_number):
            number_exercise = exercise%len(processed_exercises)
            name_exercise_group = processed_exercises[number_exercise]

            if not copy_exercise_list[name_exercise_group]:
                copy_exercise_list[name_exercise_group] = deepcopy(exercise_list[name_exercise_group])
                shuffle(copy_exercise_list[name_exercise_group])

            new_exercise = copy_exercise_list[name_exercise_group].pop()
            groups[name_exercise_group].append(new_exercise)

    return training



def get_exercise_list():
    exercise_list = {}
    training_list = {}
    actual_list = exercise_list
    with open("rutina-entreno.txt", "r",  encoding='utf-8') as ejercicios:
        content = ejercicios.read()
        processed_content = content.strip().splitlines()
        for line in processed_content:
            line_processed = line.strip()

            if ":" in line_processed:
                actual_list = training_list
                last_key = line_processed
                training_list.update({line_processed: []})
            elif line_processed == "":
                pass
            elif "," not in line_processed and actual_list is exercise_list:
                last_key = line_processed
                actual_list.update({line_processed: []})
            else:
                actual_list[last_key].append(line_processed)

        exercise_list = {group_exercise: exercise for group_exercise, exercise in exercise_list.items() if exercise}
        return exercise_list, training_list


def get_training_days(min_training_days, max_training_days):
    sleep(1)
    limpiar_terminal()
    print(days_sprite)
    days = None
    while not days:
        try:
            days = int(input("\n[min: {}] [max: {}]: "
                             .format(min_training_days, max_training_days)))
            if days == 0:
                days = 1
        except ValueError:
            print("\nValor incorrecto, introduzca un número")
            days = None

    #Comprueba si el número introducido está dentro de los límites
    print("\nComprobando si la respuesta introducida esta dentro de los límites...")
    sleep(1)

    if days < min_training_days:
        print("Se han introducido muy pocos días, se cambiará por el mínimo de {} días".format(min_training_days))
        days = min_training_days
        sleep(0.5)
        input("pulsa Enter para continuar: ")
        return days
    elif days > max_training_days:
        print("Se han introducido demasiados días, se cambiará por el máximo de {} días".format(max_training_days))
        days = max_training_days
        sleep(0.5)
        input("pulsa Enter para continuar: ")
        return days
    print("La respuesta está dentro de los límites :=)")
    sleep(0.5)
    input("pulsa Enter para continuar: ")
    return days


def get_training_minutes(min_training_minutes, max_training_minutes):
    sleep(1)
    limpiar_terminal()
    print(time_sprite)
    minutes = None
    max_training_hours = int(max_training_minutes / 60)
    while not minutes:
        try:
            minutes = int(input("\n[min: {}] [max: {} ({}h)]: "
                                   .format(min_training_minutes, max_training_minutes, max_training_hours)))
            if minutes == 0:
                minutes = 0
        except ValueError:
            print("Valor incorrecto, introduzca un número")
            minutes = None

    #Comprobar el tiempo introducido
    print("\nComprobando si la respuesta introducida esta dentro de los límites...")
    sleep(1)
    if minutes < min_training_minutes:
        print("Se ha introducido muy poco tiempo, se cambiará por el mínimo de {} minutos"
              .format(min_training_minutes))
        minutes = min_training_minutes
        sleep(0.5)
        input("pulsa Enter para continuar: ")
        return minutes
    elif minutes > max_training_minutes:
        print("Se ha introducido demasiado tiempo, se cambiará por el máximo de {} horas ({} minutos)"
              .format(max_training_hours, max_training_minutes))
        minutes = max_training_minutes
        sleep(0.5)
        input("pulsa Enter para continuar: ")
        return minutes
    print("La respuesta está dentro de los límites :=)")
    sleep(0.5)
    input("pulsa Enter para continuar: ")
    return minutes


def final_format(warn_up,exercises,exercises_training_time):
    text = []

    for calentamiento, warns_ups in warn_up.items():
        text.append(calentamiento_sprite.format(exercises_training_time)+"\n")
        text.append("*" * 40)
        text.append("{}:".format(calentamiento.upper().replace("_", " ")))
        text.append("*" * 40 + "\n")
        for index, exercise_group in enumerate(warns_ups, start=1):
            text.append("\t{} - {}".format(index,exercise_group))
            text.append("\n")
    text.append(training_sprite + "\n")
    for day, training in exercises.items():
        text.append("=" * 40)
        text.append("{}:".format(day.upper().replace("_", " ")))
        text.append("=" * 40 + "\n")
        for exercise_group in training:
            text.append("\t{}".format(exercise_group.upper()))
            for index, exercise in enumerate(training[exercise_group], start=1):
                text.append("\t\t{} - {}".format(index, exercise))
        text.append("\n")

    while True:
        save_to_txt = input("¿Quieres guardar el resultado en un .txt? [S/N]: ")
        if save_to_txt.upper() == "S":
            file_name = "resultado.txt"
            with open(file_name, "w",  encoding='utf-8') as file:
                file.write("\n".join(text))
                sleep(0.5)
            print("Guardando el archivo...")
            sleep(1)
            limpiar_terminal()
            print(txt_sprite)
            print("Archivo guardado correctamente como {} en la carpeta del programa".format(file_name))
            input("pulsa Enter para ver la rutina por terminal: ")
            print("\n".join(text))
            return
        elif save_to_txt.upper() == "N":
            sleep(0.5)
            print("No se ha guardado el archivo")
            sleep(1)
            limpiar_terminal()
            print("\n".join(text))
            return
        else:
            print("Respuesta incorrecta, introduzca [S/N]")


def limpiar_terminal():
    # Si es Windows ('nt')
    if os.name == 'nt':
        os.system('cls')
    # Si es Linux o Mac
    else:
        os.system('clear')


def main():
    min_training_days = 2
    max_training_days = 5
    min_training_minutes = 50
    max_training_minutes = 300
    exercises_training_time = 10
    limpiar_terminal()
    print(initial_sprite)
    sleep(1)
    training_days = get_training_days(min_training_days, max_training_days)
    training_minutes = get_training_minutes(min_training_minutes, max_training_minutes)

    exercises, warn_up = assign_exercises(training_days,training_minutes, exercises_training_time)
    limpiar_terminal()
    print(einstein_sprite)
    print("\nCalculando resultado...")
    sleep(1)
    final_format(warn_up, exercises, exercises_training_time)
    input("\nPresione ENTER para acabar: ")
    limpiar_terminal()
    print(final_sprite)
if __name__ == "__main__":
    main()