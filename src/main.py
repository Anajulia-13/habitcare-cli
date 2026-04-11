from src.habits import add_habit, list_habits, complete_habit


def menu():
    print("\n=== HabitCare CLI ===")
    print("1. Adicionar hábito")
    print("2. Listar hábitos")
    print("3. Concluir hábito")
    print("4. Sair")


while True:
    menu()
    op = input("Escolha: ")

    if op == "1":
        name = input("Nome do hábito: ")
        add_habit(name)
        print("Hábito adicionado com sucesso!")

    elif op == "2":
        habits = list_habits()
        if not habits:
            print("Nenhum hábito cadastrado.")
        else:
            for i, h in enumerate(habits):
                status = "✔" if h["done"] else "✘"
                print(f"{i} - {h['name']} [{status}]")

    elif op == "3":
        index = int(input("Número do hábito: "))
        complete_habit(index)
        print("Hábito concluído!")

    elif op == "4":
        print("Encerrando...")
        break

    else:
        print("Opção inválida.")