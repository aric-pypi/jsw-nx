from ruamel import yaml

# https://blog.csdn.net/BreezePython/article/details/108770195

class Yaml:
    @classmethod
    def stringify(cls, data):
        return yaml.dump(
            data,
            allow_unicode=True,
            default_flow_style=False,
            line_break=True,
            Dumper=yaml.RoundTripDumper
        )

    @classmethod
    def parse(cls, data):
        return yaml.load(data, Loader=yaml.RoundTripLoader)
