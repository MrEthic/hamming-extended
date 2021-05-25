from src import Message
import click

head = "===================================================\n" \
       "      Simulation Code Hamming\n" \
       "==================================================="


@click.command()
@click.option("-L", "--size", default="26", help="Taille du message", show_default=True)
@click.option("-e", "--error", default=0.05, help="Taux d'erreur voulu", show_default=True)
@click.option("-D", "--demo", default="0", help="Forcer une erreur par bloc", show_default=True)
def main(size, error, demo):
    m = Message.random(int(size))
    print(head)
    print(f"Taux d'erreur : {error}")
    print(f"Mode démo : {demo}\n")
    print("Message à transmettre :\n")
    m.print_message()
    print("\nMessage étendu :\n")
    m.print_extended()
    print("\nChunk de transmition :\n")
    m.print_encoded()
    m.add_error(error, force_demo=bool(int(demo)))
    print("\nMessage transmit :\n")
    m.print_encoded()
    print("\nErreur detecté :\n")
    m.print_error()


if __name__ == "__main__":
    main()
