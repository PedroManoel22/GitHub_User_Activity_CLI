import argparse


def build_parser() -> argparse.ArgumentParser:
    """Configura o parser de argumentos CLI."""
    parser = argparse.ArgumentParser(
        prog="GiThub User Activity",
        description="Atividade do usuário do GitHub via linha de comando (CLI)",
    )

    subparsers = parser.add_subparsers(
        dest="command", required=True, help="Comandos disponíveis"
    )

    # Comando: github-activity
    activity_parser = subparsers.add_parser(
        "github-activity", help="Retorna a atividade do usuário do GITHUB"
    )
    activity_parser.add_argument("username", type=str, help="Nome do usuário do GITHUB")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "github-activity":
        username = args.username.strip()
        if not username:
            print("ERRO: O nome de usuário não pode está vazio.")
            return

        print(f"Buscando atividades do usuário: {username}")


if __name__ == "__main__":
    main()
