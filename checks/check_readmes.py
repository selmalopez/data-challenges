import os
import re

class MissingReadmeError(Exception):
    def __init__(self, message):
        self.message = message

class ReadmeChecker():
    def __init__(self, modules_path):
        self.modules_path = modules_path

    def list_directory_content(self, path, pattern=None):
        if pattern is None:
            return [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
        return [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) and pattern.match(name)]

    def list_directory_files(self, path):
        return os.listdir(path)

    def run(self):
        directory_pattern = re.compile(r'([0|1]\d-)?[A-Z]')
        directories = self.list_directory_content(self.modules_path, directory_pattern)
        all_challenges = []
        for directory in directories:
            directory_path = os.path.join(self.modules_path, directory)
            topics = self.list_directory_content(directory_path, directory_pattern)
            challenges = []
            checkpoints_pattern = re.compile(r'^[^.]')
            if directory == '00-Setup':
                challenges = [
                    os.path.join(directory_path, name)
                    for name in self.list_directory_content(directory_path)
                ]
            else:
                for topic in topics:
                    path = f'{directory_path}/{topic}'
                    challenges.append(
                        [os.path.join(path, name) for name in self.list_directory_content(path, directory_pattern)]
                    )
                challenges = [item for sublist in challenges for item in sublist]
            for challenge in challenges:
                if 'README.md' in self.list_directory_files(challenge):
                    all_challenges.append(challenge)
                else:
                    raise MissingReadmeError(f'Missing README.md file in {challenge}')
        return all_challenges

if __name__ == "__main__":
    modules_path = os.path.dirname(os.path.dirname(__file__))
    paths = ReadmeChecker(modules_path).run()
    print(paths)
    print(len(paths))
