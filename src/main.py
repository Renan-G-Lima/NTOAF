from src.database import create_tables


def main() -> None:
    create_tables()
    print("Tabelas criadas com sucesso!")


if __name__ == "__main__":
    main()