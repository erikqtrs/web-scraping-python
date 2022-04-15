from bs4 import BeautifulSoup

with open('../webpage/main.html') as html_file:
    content = html_file.read()

soup = BeautifulSoup(content, 'lxml')

courses = soup.find_all('h5')
 
for course in courses:
    course_name = course.text
    print( course_name ) 