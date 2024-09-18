# GEDCOM File Creator with Flask

This project is a simple web application built with **Flask** to generate **GEDCOM** files. It allows users to add people, define parent-child relationships, set a source for the data, and download a GEDCOM file with the provided information.

## Features

- Add individuals with first name, last name, and birth date.
- Define parent-child relationships.
- Add a source of information for the entire dataset.
- Export all data into a GEDCOM file that can be used in genealogical tools like Webtrees.

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

### Adding People

1.  In the main form, enter the details for each person (first name, last name, and birth date in the format DD/MM/YYYY).
2.  Click "Add Person".

### Defining Relationships

1.  Once you have added people, you can select two people to define a parent-child relationship.
2.  Select a parent and a child from the dropdown menus and click "Add Relationship".

### Setting a Source

1.  In the "Set Source" section, enter the source of the information (e.g., "Civil Registry of Barcelona").
2.  Click "Set Source". This information will be added to each entry in the GEDCOM.

### Exporting the GEDCOM File

1.  After you have added all people and relationships, you can download the GEDCOM file.
2.  Click on "Download GEDCOM File" to obtain the `output.ged` file.

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

License
-------

This project is licensed under the MIT License.