import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, QSplitter
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import folium
import os

class MapWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Map GUI")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()
        self.setLayout(layout)

        # Create a QSplitter to separate the sidebar and map
        splitter = QSplitter(self)
        layout.addWidget(splitter)

        # Create a sidebar widget
        sidebar_widget = QWidget()
        sidebar_layout = QVBoxLayout(sidebar_widget)

        # Create a button
        button = QPushButton("Click Me")
        sidebar_layout.addWidget(button)

        # Create a text edit for the description
        description = QTextEdit()
        description.setPlainText("This is the description sidebar.")
        sidebar_layout.addWidget(description)

        # Add the sidebar widget to the splitter
        splitter.addWidget(sidebar_widget)

        # Create a Folium map
        map_obj = folium.Map(location=[51.5074, -0.1278], zoom_start=10)

        # Save the map as HTML file in the program directory
        map_file = os.path.join(os.path.dirname(__file__), "map.html")
        map_obj.save(map_file)

        # Create a web view to display the map
        web_view = QWebEngineView()
        splitter.addWidget(web_view)

        # Load the saved HTML file in the web view
        web_view.load(QUrl.fromLocalFile(map_file))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    map_widget = MapWidget()
    map_widget.show()
    sys.exit(app.exec_())
