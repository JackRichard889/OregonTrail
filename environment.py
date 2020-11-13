class Environment:
    def __init__(self, name: str, texture, length: int):
        self.name = name
        self.texture = texture
        self.length = length


class EnvironmentRegistry:
    def __init__(self):
        self.__environments = []

    def add_environment(self, environment):
        self.__environments.append(environment)
        return len(self.__environments) - 1

    def get_environment(self, index):
        return self.__environments[index]

    def get_array(self):
        return self.__environments

    def get_length(self):
        length = 0
        for env in self.__environments:
            length += env.length * 100
        return length
