from flask import Flask, render_template, request, redirect, url_for, send_file, flash
import io
import re

app = Flask(__name__)
app.secret_key = 'secret_key'

# Data structure for people and relationships
people = []
relationships = []
sour = None  # Variable to store the source

# Function to validate date format DD/MM/YYYY
def validate_date(date):
    return re.match(r"\d{2}/\d{2}/\d{4}", date)

@app.route('/')
def index():
    return render_template('index.html', people=people, relationships=relationships, sour=sour)

@app.route('/add_person', methods=['POST'])
def add_person():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    birth_date = request.form['birth_date']

    # Data validation
    if not first_name or not last_name or not birth_date:
        flash("All fields are required!", "error")
        return redirect(url_for('index'))
    
    if not validate_date(birth_date):
        flash("The date must be in the format DD/MM/YYYY!", "error")
        return redirect(url_for('index'))

    # Add person to the list
    people.append({
        'id': len(people) + 1,
        'first_name': first_name,
        'last_name': last_name,
        'birth_date': birth_date
    })
    flash("Person added successfully!", "success")
    return redirect(url_for('index'))

@app.route('/add_relationship', methods=['POST'])
def add_relationship():
    parent_id = int(request.form['parent'])
    child_id = int(request.form['child'])

    if parent_id == child_id:
        flash("Parent and child cannot be the same person!", "error")
        return redirect(url_for('index'))

    # Add relationship
    relationships.append({
        'parent': parent_id,
        'child': child_id
    })
    flash("Relationship added successfully!", "success")
    return redirect(url_for('index'))

@app.route('/set_source', methods=['POST'])
def set_source():
    global sour
    sour = request.form['sour']  # Assign source to global variable
    flash("Source set successfully!", "success")
    return redirect(url_for('index'))

@app.route('/download_gedcom')
def download_gedcom():
    # Generate the GEDCOM file
    gedcom = io.StringIO()
    gedcom.write("0 HEAD\n1 SOUR FlaskGEDCOM\n1 GEDC\n2 VERS 5.5.1\n2 FORM LINEAGE-LINKED\n1 CHAR UTF-8\n")

    if sour:
        gedcom.write(f"1 SOUR {sour}\n")  # Add source if set

    # Add people to GEDCOM
    for person in people:
        gedcom.write(f"0 @I{person['id']}@ INDI\n")
        gedcom.write(f"1 NAME {person['first_name']} /{person['last_name']}/\n")
        gedcom.write(f"1 BIRT\n2 DATE {person['birth_date']}\n")
        if sour:
            gedcom.write(f"1 SOUR {sour}\n")  # Add source for each person

    # Add relationships (parents and children)
    for relationship in relationships:
        parent = relationship['parent']
        child = relationship['child']
        gedcom.write(f"0 @F{parent}{child}@ FAM\n")
        gedcom.write(f"1 HUSB @I{parent}@\n")
        gedcom.write(f"1 CHIL @I{child}@\n")
        if sour:
            gedcom.write(f"1 SOUR {sour}\n")  # Add source for each relationship

    gedcom.write("0 TRLR\n")
    gedcom.seek(0)

    return send_file(
        io.BytesIO(gedcom.getvalue().encode('utf-8')),
        mimetype='text/plain',
        as_attachment=True,
        download_name='output.ged'
    )

if __name__ == '__main__':
    app.run(debug=True)
