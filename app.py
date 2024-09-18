from flask import Flask, render_template, request, redirect, url_for, send_file, flash
import io
import re

app = Flask(__name__)
app.secret_key = 'secret_key'

# Data structure for people and relationships
people = []
relationships = []
parent_child_relationships = []  # New list to store parent-child relationships
sour = None  # Variable to store the source
birth_places = ['Barcelona', 'Tarragona', 'Reus', 'Vilanova i la Geltrú']

# Function to validate date format (now not required for 'date' input)
def validate_date(date):
    return re.match(r"\d{4}-\d{2}-\d{2}", date)

@app.route('/')
def index():
    return render_template('index.html', people=people, relationships=relationships, 
                           parent_child_relationships=parent_child_relationships, sour=sour, 
                           birth_places=birth_places)

@app.route('/add_person', methods=['POST'])
def add_person():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    birth_date = request.form['birth_date']
    birth_place = request.form['birth_place']  # Capture birth place from dropdown
    sex = request.form['sex']  # Capture sex of the person

    if not first_name or not last_name or not birth_date or not sex or not birth_place:
        flash("All fields are required!", "error")
        return redirect(url_for('index'))

    if birth_place not in birth_places:
        birth_places.append(birth_place)

    people.append({
        'id': len(people) + 1,
        'first_name': first_name,
        'last_name': last_name,
        'birth_date': birth_date,
        'birth_place': birth_place,
        'sex': sex
    })
    flash("Person added successfully!", "success")
    return redirect(url_for('index'))

@app.route('/add_relationship', methods=['POST'])
def add_relationship():
    husband_id = int(request.form['husband'])
    wife_id = int(request.form['wife'])
    relationship_type = request.form['relationship_type']

    if husband_id == wife_id:
        flash("Husband and wife cannot be the same person!", "error")
        return redirect(url_for('index'))

    relationships.append({
        'husband': husband_id,
        'wife': wife_id,
        'relationship_type': relationship_type
    })
    flash("Relationship added successfully!", "success")
    return redirect(url_for('index'))

# New route to add parent-child relationships
@app.route('/add_parent_child', methods=['POST'])
def add_parent_child():
    parent_id = int(request.form['parent'])
    child_id = int(request.form['child'])

    if parent_id == child_id:
        flash("Parent and child cannot be the same person!", "error")
        return redirect(url_for('index'))

    parent_child_relationships.append({
        'parent': parent_id,
        'child': child_id
    })
    flash("Parent-child relationship added successfully!", "success")
    return redirect(url_for('index'))

# Route to delete a person
@app.route('/delete_person/<int:person_id>', methods=['POST'])
def delete_person(person_id):
    global people
    people = [p for p in people if p['id'] != person_id]
    flash("Person removed successfully!", "success")
    return redirect(url_for('index'))

# Route to delete a relationship
@app.route('/delete_relationship/<int:relationship_index>', methods=['POST'])
def delete_relationship(relationship_index):
    if 0 <= relationship_index < len(relationships):
        del relationships[relationship_index]
        flash("Relationship removed successfully!", "success")
    return redirect(url_for('index'))

# Route to delete a source
@app.route('/clear_source', methods=['POST'])
def clear_source():
    global sour
    sour = None
    flash("Source cleared successfully!", "success")
    return redirect(url_for('index'))


@app.route('/set_source', methods=['POST'])
def set_source():
    global sour
    sour = request.form['sour']
    flash("Source set successfully!", "success")
    return redirect(url_for('index'))

@app.route('/download_gedcom')
def download_gedcom():
    gedcom = io.StringIO()
    gedcom.write("0 HEAD\n1 SOUR FlaskGEDCOM\n1 GEDC\n2 VERS 5.5.5\n2 FORM LINEAGE-LINKED\n1 CHAR UTF-8\n")

    if sour:
        gedcom.write(f"1 SOUR {sour}\n")

    for person in people:
        gedcom.write(f"0 @I{person['id']}@ INDI\n")
        gedcom.write(f"1 NAME {person['first_name']} /{person['last_name']}/\n")
        gedcom.write(f"1 SEX {person['sex']}\n")
        gedcom.write(f"1 BIRT\n2 DATE {person['birth_date']}\n2 PLAC {person['birth_place']}\n")
        if sour:
            gedcom.write(f"1 SOUR {sour}\n")

    for relationship in relationships:
        husband = relationship['husband']
        wife = relationship['wife']
        rel_type = relationship['relationship_type']
        gedcom.write(f"0 @F{husband}{wife}@ FAM\n")
        gedcom.write(f"1 HUSB @I{husband}@\n")
        gedcom.write(f"1 WIFE @I{wife}@\n")
        gedcom.write(f"1 MARR\n2 TYPE {rel_type}\n")
        if sour:
            gedcom.write(f"1 SOUR {sour}\n")

    for pc_relationship in parent_child_relationships:
        parent = pc_relationship['parent']
        child = pc_relationship['child']
        gedcom.write(f"0 @F{parent}{child}@ FAM\n")
        gedcom.write(f"1 HUSB @I{parent}@\n")
        gedcom.write(f"1 CHIL @I{child}@\n")

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
