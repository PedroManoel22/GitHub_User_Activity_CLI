import json
import urllib.error
import urllib.request


def fetch_github_activity(username: str) -> None:
    """Busca e exibe as últimas atividades públicas de um usuário no GitHub."""
    url = f"https://api.github.com/users/{username}/events/public"

    # O GitHub EXIGE o cabeçalho User-Agent em todas as requisições via API
    headers = {"User-Agent": "github-activity-cli"}
    req = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode("utf-8"))

            if not data:
                print(f"Nenhuma atividade recente encontrada para '{username}'.")
                return

            print(f"\n--- ÚLTIMAS ATIVIDADES DE @{username} ---")

            # Percorremos os 10 eventos mais recentes
            for event in data[:10]:
                event_type = event.get("type")
                repo_name = event.get("repo", {}).get("name")

                if event_type == "PushEvent":
                    payload = event.get("payload", {})
                    commits = payload.get("commits", [])

                    commits_count = max(
                        len(commits),
                        payload.get("size", 0),
                        payload.get("distinct_size", 0),
                    )

                    if commits_count > 0:
                        print(f"- Fez push de {commits_count} commit(s) em {repo_name}")

                    else:
                        print(f"- Sincronizou/atualizou uma branch em {repo_name}")

                elif event_type == "IssuesEvent":
                    action = event.get("payload", {}).get("action")
                    print(f"- {action.capitalize()} uma issue em {repo_name}")

                elif event_type == "WatchEvent":
                    print(f"- Deu star no repositório {repo_name}")

                elif event_type == "CreateEvent":
                    ref_type = event.get("payload", {}).get("ref_type")
                    print(f"- Criou um(a) {ref_type} em {repo_name}")

                else:
                    # Fallback para outros tipos de eventos (PRs, Forks, etc.)
                    print(f"- Realizou {event_type} em {repo_name}")

    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(
                f"\n\033[31mERRO: Usuário '{username}' não foi encontrado no GitHub.\n\033[m"
            )
        else:
            print(
                f"\n\033[31mERRO: A API do GitHub retornou o código HTTP {e.code}.\n\033[m"
            )
    except urllib.error.URLError:
        print(
            "\n\033[31mERRO: Não foi possível conectar à internet. Verifique sua conexão.\n\033[m"
        )
