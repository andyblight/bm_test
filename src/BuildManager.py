# BuildDefinition and related classes

class PackageBuildOptions:
    """The PackageBuildOptions class defines the path to the package definition file, the version of the package to build and any build options to use during the build."""
    def __init__ (self):
        self.path = ""
        self.version = ""
        self.options = ""


class BuildDefinition:
    """The BuildDefinition class has the global build variables and paths and a list of the packages with their build options"""
    def __init__ (self):
        self.default_shell = "dash"
        self.root_build_directory = "."
        self.local_src_directory = ""
        self.local_prebuilt_directory = ""
        self.package_list = []

class PackageDefinition:
    """The PackageDefinition class.
    TBD  """
    def __init__(self)
        # Functional variables
        # A list of BuildStage objects
        self.build_stages = []
        # Optional variables
        
        
class BuildStage:
    def __init__(self):
        self.name = ""
        # List of Dependecy objects 
        self.dependencies = []
        self.action = ""

class Dependecy:
    def __init__(self, package, build_stage_name):
        # A single PackageDefinition object
        self.package = package
        # The name object from a BuildStage object in the PackageDefinition object defined by self.package
        self.build_stage_name = build_stage_name
