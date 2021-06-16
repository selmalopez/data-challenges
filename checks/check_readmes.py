import os
import re

class MissingReadmeError(Exception):
    def __init__(self, message):
        self.message = message

class ReadmeChecker():
    def list_directory_content(self, path, pattern=None):
        if pattern is None:
            return os.listdir(path)
        return [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) and pattern.match(name)]

    def run(self):
        directory_pattern = re.compile('[0|1]\d')
        directories = self.list_directory_content('.', directory_pattern)
        all_challenges = []
        for directory in directories:
            topics = self.list_directory_content(directory, directory_pattern)
            if directory == '00-Setup':
                challenges = [os.path.join(directory, topic) for topic in topics]
            else:
                for topic in topics:
                    path = f'{directory}/{topic}'
                    challenges = [os.path.join(path, name) for name in self.list_directory_content(f'{directory}/{topic}', directory_pattern)]
            for challenge in challenges:
                if 'README.md' in self.list_directory_content(challenge):
                    all_challenges.append(challenge)
                else:
                    raise MissingReadmeError(f'Missing README.md file in {challenge}')
        return all_challenges

if __name__ == "__main__":
    paths = ReadmeChecker().run()
    print(paths)
    print(len(paths))
