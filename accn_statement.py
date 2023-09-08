from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import mysql.connector
def user_find(fname,lname):
    db_connection = mysql.connector.connect(
        host="127.0.0.1",      # Replace with your host
        user="root",  # Replace with your username
         password="database password",  # Replace with your password
        database="first create database in sql workbench"  # Replace with your database name
    )
    cursor = db_connection.cursor()
    sql_query = "SELECT * FROM Account_Money WHERE fname=%s AND  lname=%s"
    cursor.execute(sql_query,(fname,lname))
    result = cursor.fetchall()
    column_mapping = {
        "fname": "First Name",
        "lname": "Last Name",
        "dob": "Date of Birth",
        "gender": "Gender",
        "accn": "Account Number"
    }
    result_dict = {}
    for i in range(1, len(cursor.description)-1):
        column_name = cursor.description[i][0]
        if column_name in column_mapping:
            result_dict[column_mapping[column_name]] = result[0][i]

    cursor.close()
    db_connection.close()
    return result_dict

# Function to generate the PDF with user details
def generate_user_details_pdf(pdf_file, user_details):
    doc = SimpleDocTemplate(pdf_file, pagesize=letter,title = "APNA BANK INDIA")
    story = []

    # Create a table with user details
    data = [["User Details"]]
    for key, value in user_details.items():
        data.append([key, value])

    # Create a style for the table
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])

    # Create the table and apply the style
    user_table = Table(data)
    user_table.setStyle(style)

    # Add the table to the story
    story.append(user_table)

    # Build the PDF document from the story
    doc.build(story)

def generate_statement_user(fname,lname):
    user_details = user_find(fname,lname)
    pdf_file = "Bank_Statement.pdf"
    generate_user_details_pdf(pdf_file, user_details)
