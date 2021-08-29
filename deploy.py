import click
import os
from pathlib import Path

@click.group()
def cli():
    pass


@click.command(help="convention pep8")
@click.option("--pep8", default=True, help="mise en forme des differents fichiers, convention pep8")
def autopep8(pep8: bool):
    if pep8:
        p = Path('.')
        py_file_to_pep8 = list(p.glob('Mahanalobis_Detection_Outliers/*.py'))

        for py_file in py_file_to_pep8:
            command = f"black {py_file}"
            os.system(command)


@click.command(help="lancement des tests")
@click.option("--test", default=True, help="Effectue les tests avec pytest")
def lancement_test(test: bool):
    if test:
        command = f"pytest"
        os.system(command)


@click.command(help="package la solution")
@click.option("--packaging", default=True, help="Similaire au librarie")
def packaging_solution(packaging: bool):
    if packaging:
        step = "python3 setup.py bdist_wheel"
        os.system(f"{step}")
    else:
        pass

@click.command(help="push la solution sur git ou gitlab")
@click.option("--push", default=True, help="d'abord set le git")
def push_to_git(push: bool):
    if push:
        message_commit = str(input("Git message :"))
        step_1 = "git add ."
        step_2 = f'git commit -m "{message_commit}"'
        setp_3 = "git push"

        all_step_packaging = [step_1, step_2, setp_3]

        for step in all_step_packaging:
            os.system(f"{step}")
    else:
        pass


@click.command(help="Execute toutes les action en un fois")
@click.option(
    "--global_",
    default=True,
    help="convention_code -> packaging_solution -> push_to_git",
)
def global_CI(global_: bool):
    if global_:
        global_commande = []

        p = Path('.')
        py_file_to_pep8 = list(p.glob('Mahanalobis_Detection_Outliers/*.py'))
        for py_file in py_file_to_pep8:
            command_0 = f"black {py_file}"
            global_commande.append(command_0)

        command_1 = "pytest"
        
        command_2 = "python3 setup.py bdist_wheel"

        message_commit = str(input("Git message :"))
        command_3 = "git add ."
        command_4 = f'git commit -m "{message_commit}"'
        command_5 = "git push"

        global_commande.extend([command_1, command_2, command_3, command_4, command_5])

        for command in global_commande:
            os.system(command)

    else:
        pass


cli.add_command(packaging_solution)
cli.add_command(push_to_git)
cli.add_command(global_CI)
cli.add_command(autopep8)
cli.add_command(lancement_test)



if __name__ == "__main__":
    cli()
