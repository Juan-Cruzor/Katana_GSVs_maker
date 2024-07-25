from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QLabel, QVBoxLayout, QLineEdit, QHBoxLayout, QPushButton
from PySide2.QtCore import Qt

from GSVs_creation_Tool import GSVsMaker

class GSVsToolViewInterface(QWidget):
    """GSV Maker Tool (GUI)."""
    def __init__(self):
        """View initializer.
           Attributes:
                 general_layout: Set the general layout of the window
                 setWindowTitle: Set the window title
        """
        super(GSVsToolViewInterface, self).__init__()
        # Set some main window's properties
        self.general_layout = QVBoxLayout()
        self.setLayout(self.general_layout)

        # Set the window's title
        self.setWindowTitle('GSVs Maker')

        # Create the buttons
        self.title_section()
        self.GSV_name_section()
        self.GSV_parameter_section
        self.okay_and_cancel

        # Set the signals and slots for the buttons
        self.create_methods()

    def title_section(self):
        """Function that creates the label with the name of the tool"""
        # Set this section layout
        display_section_layout = QVBoxLayout()
        name_label = QLabel("GSVs Tool")
        # Add the widget to the layout
        display_section_layout.addWidget(name_label)
        # Add this section layout to the general layout
        self.general_layout.addLayout(display_section_layout)

    def GSV_name_section(self):
            """Set the name of the GSV"""
            sub_layout = QHBoxLayout()
            name_label = QLabel("GSV name: ")
            self.name_parameter = QLineEdit()
            self.name_parameter_text = self.name_parameter.text()
            # Add the widget to the layout
            sub_layout.addWidget(name_label)
            sub_layout.addWidget(self.name_parameter)
            # Add this section layout to the general layout
            self.general_layout.addLayout(sub_layout)

    def GSV_parameter_section(self):
            """Set the parameters of the GSV"""
            sub_layout = QHBoxLayout()
            self.first_parameter = QLineEdit()
            self.second_parameter = QLineEdit()
            self.third_parameter = QLineEdit()
            self.first_parameter_text = self.first_parameter.text()
            self.second_parameter_text = self.second_parameter.text()
            self.third_parameter_text = self.third_parameter.text()
            # Add the widget to the layout
            sub_layout.addWidget(self.first_parameter)
            sub_layout.addWidget(self.second_parameter)
            sub_layout.addWidget(self.third_parameter)
            # Add this section layout to the general layout
            self.general_layout.addLayout(sub_layout)


    def GSV_parameter_section(self):
            """Set the parameters of the GSV"""
            sub_layout = QHBoxLayout()
            path = QLineEdit()
            self.path_text = path.text()
            name_label = QLabel("File: ")
            # Layout
            sub_layout.addWidget(path)
            sub_layout.addWidget(path)
            # Add this section layout to the general layout
            self.general_layout.addLayout(sub_layout)

    def okay_and_cancel(self):
            """Okay button to create the GSVs"""
            # Define this section layout
            okay_cancel_layout = QHBoxLayout()
            # Create the buttons
            self.okay_button = QPushButton("Make GSVs")
            self.cancel_button = QPushButton("Cancel")
            self.file_button = QPushButton("Load GSVs")
            # Add the widgets to the layout
            okay_cancel_layout.addWidget(self.okay_button)
            okay_cancel_layout.addWidget(self.file_button)
            okay_cancel_layout.addWidget(self.cancel_button)
            # Add this layout section to the general layout
            self.general_layout.addLayout(okay_cancel_layout)

    def create_methods(self):
        """This function creates some signals and slots
           to make the buttons work.
           The functions or actions the buttons are going to do
           are imported from the GSV tool"""
        
        self.okay_button.clicked.connect(lambda: GSVsMaker.execute(self.name_parameter_text,
                                                                self.first_parameter_text, 
                                                                self.second_parameter_text, 
                                                                self.third_parameter_text)
                                        )
        self.cancel_button.clicked.connect(self.close)
        self.file_button.clicked.connect(lambda: GSVsMaker.build(self.path_text))
   
    def main(self):
          """Function that runs the build function to build the dictionary"""
          pass

if __name__ == "__main__":

        User_Interface = GSVsToolViewInterface()
        User_Interface.main()
        User_Interface.show()

    
