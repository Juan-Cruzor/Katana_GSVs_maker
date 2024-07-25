import NodegraphAPI
import json
import os



# Standard toolkit logger
logger = sgtk.platform.get_logger(__name__)


class GSVsMaker():
    """Class to create GSVs from a JSON file.
        Args:
            dictionary[Dict]: Dictionary with the keys(GSVs) and values of the GSV.
            IsFile[Boolean]: If it is false the dictionary is coming from the values in the UI.
    """
    def __init__(self, dictionary, IsFile):
        super(GSVsMaker, self).__init__()
        
        self._dictionary = dictionary
        self._isFile = IsFile

        
    def build(self, filepath):
            """Function to open a json file from a provided path.

            Args:
                Filepath[Dict]: Json file to create the CSVs from.
            """

            if not os.path.exists(filepath):
                raise FileNotFoundError(
                    "build function filepath <{}> doesn't exists.".format(filepath)
                )

            with open(filepath, "r") as GSVsDict:
                file = json.load(GSVsDict)


    def setup_gsvs(self):
        """Function to get the dictionary"""

        for gsv_name, gsv_values in self._dictionary.items():
            self.make_gsv(gsv_name, gsv_values)

        return


    def make_gsv(self, key_in_dictionary, values_dictionary):
        """
        Create a graph state variable with the given keys in the JSON file and with the given values of the dictionary in the JSON file.
        Delete the value if it already exists.

        Args:
            key_in_dictionary[str]: Name of the GSV.
            values_in_dictionary[list]: List of values of the GSV.

        """
        # Returns NodegraphAPI.GroupNode type. Which lets us use the parameters class methods  .
        GSVs = NodegraphAPI.GetRootNode().getParameter('variables')
        # Returns the group child by name, or None if not found.
        found_GSV = GSVs.getChild(key_in_dictionary)
        if found_GSV:
            GSVs.deleteChild(found_GSV)

        new_gsv = GSVs.createChildGroup(key_in_dictionary)
        new_gsv.createChildNumber('enable', 1)
        new_gsv.createChildString('value', values_dictionary[0])
        # Creating the contents of the dictionary.
        new_gsv_param = new_gsv.createChildStringArray('options', len(values_dictionary))
        # Zip function to iterate over two lists
        for option_param, option_value in zip(new_gsv_param.getChildren(), values_dictionary):
            option_param.setValue(option_value, 0)
        
        return

    def create_dictionary(self, name_GSV, parameter_1, parameter_2, parameter_3):
        """Get the input of the QLineEdit
         
            Args:
                name_GSV[str]: Name gotten from the UI
                parameters[list]: List of the values
        """
        parameters = list((parameter_1, parameter_2, parameter_3))
        
        self._dictionary = {name_GSV: parameters}

    def execute(self, name_GSV, parameter_1, parameter_2, parameter_3):
        """Function that creates the dictionary and starts the execution of the make_GSV"""
        self.create_dictionary(name_GSV, parameter_1, parameter_2, parameter_3)
        self.setup_gsvs()