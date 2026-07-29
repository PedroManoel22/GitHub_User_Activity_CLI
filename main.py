import argparse

from github_api import fetch_github_activity


def build_parser() -> argparse.ArgumentParser:
    """Configura o parser de argumentos CLI."""
    parser = argparse.ArgumentParser(
        prog="github-activity",
        description="Atividade do usuário do GitHub via linha de comando (CLI)",
    )

    parser.add_argument("username", type=str, help="Nome do usuário do GITHUB")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    username = args.username.strip()

    if not username:
        print("ERRO: O nome de usuário não pode estar vazio.")
        return

    print(f"Buscando atividades do usuário: {username}")
    fetch_github_activity(username)


if __name__ == "__main__":
    main()
