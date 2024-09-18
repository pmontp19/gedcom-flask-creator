# GEDCOM File Creator with Flask

This project is a simple web application built with **Flask** to generate **GEDCOM** files. It allows users to add people, define parent-child relationships, set a source for the data, and download a GEDCOM file with the provided information.

## Features

- **Add People**: Input first name, last name, birth date, and birthplace.
- **Dynamic Birthplace Input**: Users can either select from a predefined list of places or input a custom place. Custom places are added to the list dynamically.
- **Add Relationships**: Define husband-wife and parent-child relationships.
- **Source Management**: Set a data source and clear it when needed.
- **Remove Entries**: Easily remove people, relationships, or sources via the UI.
- **Download GEDCOM File**: Export the current state of the data to a GEDCOM file.
- **Responsive Design**: Works across devices with a two-column layout on wide screens and a single-column layout on mobile.

## Requirements

- **Python 3.x**
- **Flask**

## Installation

1. Clone this repository or download it to your local machine:

   ```bash
   git clone https://github.com/your-username/gedcom-flask-creator.git
   cd gedcom-flask-creator
   ```

2.  Create and activate a virtual environment (optional but recommended):

    `python3 -m venv env source env/bin/activate`
    
3.  Install the dependencies:
    
    `pip install flask`
    

Running the Application
-----------------------

1.  Once the dependencies are installed, you can run the application:
    
    `python app.py`
    
2.  Open your web browser and go to:
    
    `http://127.0.0.1:5000/`
    

Usage
-----

1.  **Add a Person**:
    
    *   Enter the first name, last name, birth date, and select or type the birthplace.
    *   The birth date uses an HTML5 date picker, and the birthplace can be either selected from a list or entered as free text.
    *   The birthplace input will dynamically add new places to the predefined list.
2.  **Add Relationships**:
    
    *   After adding people, you can define relationships (Husband-Wife or Parent-Child) between them.
    *   Select from the people you’ve already added.
3.  **Remove People or Relationships**:
    
    *   Each person or relationship added has a "Remove" button next to it.
    *   Simply click "Remove" to delete the person or relationship from the list.
4.  **Set or Clear Source**:
    
    *   You can add a data source to track the origin of the data.
    *   A "Clear Source" button is available to remove the current source.
5.  **Download GEDCOM**:
    
    *   Click "Download GEDCOM File" to export the current data in GEDCOM format.

GEDCOM File Structure
---------------------

*   Each person will have an `INDI` entry with their name, birth date, and other details.
*   Relationships between parents and children will be included as `FAM` entries.
*   The source specified will be included as a `SOUR` field for each person and family.

Contributions
-------------

Contributions are welcome to improve the project. If you would like to contribute:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/new-feature`).
3.  Commit your changes (`git commit -m 'Add new feature'`).
4.  Push the branch (`git push origin feature/new-feature`).
5.  Open a pull request.

Roadmap
-------

* **Persistent Storage**: Implement a persistent data storage system (e.g., SQLite or a JSON file) to retain data between sessions.
* **Validation**: Add more advanced validation for relationships and data entry.
* **Extended GEDCOM Export**: Implement support for additional GEDCOM tags and features.

License
-------

This project is licensed under the MIT License.