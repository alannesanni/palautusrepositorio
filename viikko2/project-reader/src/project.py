class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, authors, license):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.authors=authors
        self.license=license

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        dep="\n".join(f"- {i}" for i in self.dependencies)
        dev_dep="\n".join(f"- {i}" for i in self.dev_dependencies)
        aut="\n".join(f"- {i}" for i in self.authors)
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}"
            "\n " 
            f"\nAuthors: \n{aut}" 
            "\n "
            f"\nDependencies: \n{dep}"
            "\n "
            f"\nDevelopment dependencies: \n{dev_dep}"
        )
