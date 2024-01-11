import json
import os
import git
import argparse
from termcolor import colored
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError


def parse_config(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def print_status_message(status, message):
    colors = {
        'Local modifications': 'yellow',
        'Behind remote': 'red',
        'Up-to-date': 'green',
        'Ahead of remote': 'blue',
        'Error': 'magenta',
        'Not a git repository': 'cyan',
        'Updated': 'green',
        'Cloned': 'green'
    }
    print(colored('██', colors[status]), message)


def find_gitproject_file(start_path='.'):
    path = os.path.abspath(start_path)
    while os.path.split(path)[1]:
        potential_file = os.path.join(path, '.gitproject')
        if os.path.isfile(potential_file):
            return potential_file
        path = os.path.dirname(path)
    return None


def get_repo_status(repo_path):
    try:
        repo = git.Repo(repo_path)
    except InvalidGitRepositoryError:
        return 'Not a git repository', None
    except NoSuchPathError:
        return 'Not a git repository', None

    if repo.is_dirty(untracked_files=True):
        return 'Local modifications', None

    try:
        remote_ref = f'origin/{repo.active_branch.name}'
        repo.remote().fetch()
        local_commit = repo.head.commit
        remote_commit = repo.remote().refs[repo.active_branch.name].commit

        if local_commit.hexsha != remote_commit.hexsha:
            if repo.git.rev_list(f'{remote_commit.hexsha}..{local_commit.hexsha}'):
                return 'Ahead of remote', None
            return 'Behind remote', remote_ref

    except Exception as e:
        return f'Error: {str(e)}', None

    return 'Up-to-date', None


def clone_repo(url, path, branch='master', commit_hash=None):
    try:
        repo = git.Repo.clone_from(url, path, branch=branch)
        if commit_hash:
            repo.git.checkout(commit_hash)
    except GitCommandError as e:
        return f'Error: {e}'
    return 'Cloned'


def update_repo(repo_path, branch='master', commit_hash=None):
    try:
        repo = git.Repo(repo_path)
        repo.git.checkout(branch)
        if commit_hash:
            repo.git.checkout(commit_hash)
        else:
            repo.remote().pull(branch)
    except GitCommandError as e:
        return f'Error: {e}'
    return 'Updated'


def show_status(config):
    for module in config['modules']:
        status, _ = get_repo_status(module['path'])
        print_status_message(status, f"{module['name']}: {status}")


def update_modules(config):
    for module in config['modules']:
        status, remote_ref = get_repo_status(module['path'])
        branch = module.get('branch', 'master')
        commit_hash = module.get('commit')

        if status == 'Not a git repository':
            print(f"Cloning {module['name']}...")
            result = clone_repo(module['url'], module['path'], branch, commit_hash)
        else:
            print(f"Updating {module['name']}...")
            result = update_repo(module['path'], branch, commit_hash)

        print_status_message(result, f"{module['name']}: {result}")


def update_gitignore(config, gitignore_file='.gitignore'):
    paths_to_add = {m['path'] for m in config['modules']}
    try:
        with open(gitignore_file, 'r+') as file:
            existing_paths = set(file.read().splitlines())
            new_paths = paths_to_add - existing_paths

            if new_paths:
                file.write('\n' + '\n'.join(new_paths) + '\n')
                print("Updated .gitignore with new module paths.")
            else:
                print("No new paths to add to .gitignore.")
    except FileNotFoundError:
        with open(gitignore_file, 'w') as file:
            file.write('\n'.join(paths_to_add) + '\n')
        print(".gitignore created and updated with module paths.")


def main():
    parser = argparse.ArgumentParser(description='Manage project modules')

    # Group related arguments for better clarity.
    mode_group = parser.add_argument_group("mode", "Mode of operation")
    mode_group.add_argument("-s", "--status", action="store_true", help="Show status of modules")
    mode_group.add_argument("-u", "--update", action="store_true", help="Update modules")
    parser.add_argument("-g", "--gitignore", action="store_true", help="Update .gitignore with module paths")

    args = parser.parse_args()

    gitproject_file = find_gitproject_file()
    if not gitproject_file:
        print("Error: .gitproject file not found.")
        return

    project_root = os.path.dirname(gitproject_file)
    os.chdir(project_root)

    config = parse_config(gitproject_file)

    if args.status:
        show_status(config)
    elif args.update:
        update_modules(config)
    elif args.gitignore:
        update_gitignore(config)


if __name__ == "__main__":
    main()
