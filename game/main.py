import random

def choose_options():
    options = ("piedra", "papel", "tijera")
    user_gamer = input("Ingresa piedra, papel o tijera: ")
    user_gamer = user_gamer.lower()

    if not user_gamer in options:
        print("ingresa una opcion valida")
        return None, None

    pc_gamer = random.choice(options)
    print("user option -> ", user_gamer)
    print("computer option -> ", pc_gamer)
    return user_gamer, pc_gamer


def check_rules(user_gamer, pc_gamer, user_wins, pc_wins):
    if user_gamer == pc_gamer:
        print("hubo un empate")
        print("")
    elif user_gamer == "tijera" and pc_gamer == "papel":
        print("tijera le gana a papel")
        print("user_gamer GANA!")
        print("")
        user_wins += 1
    elif user_gamer == "papel" and pc_gamer == "piedra":
        print("papel le gana a piedra")
        print("user_gamer GANA!")
        print("")
        user_wins += 1
    elif user_gamer == "piedra" and pc_gamer == "tijera":
        print("piedra le gana a tijera")
        print("user_gamer GANA!")
        print("")
        user_wins += 1
    else:
        print(f"{pc_gamer} le gana a {user_gamer}")
        print("pc_gamer GANA")
        print("")
        pc_wins += 1
    return user_wins, pc_wins


def run_game():
    pc_wins = 0
    user_wins = 0
    rounds = 1

    while True:
        print("*" * 10)
        print("ROUND", rounds)
        print("*" * 10)
        print("pc_wins", pc_wins)
        print("user_wins", user_wins)

        user_gamer, pc_gamer = choose_options()
        user_wins, pc_wins = check_rules(user_gamer, pc_gamer, user_wins, pc_wins)
        rounds += 1
        
        if pc_wins == 2:
            print("El ganador es pc_gamer")
            break

        if user_wins == 2:
            print("El ganador es user_gamer")
            break


if __name__ == "__main__":
    run_game()