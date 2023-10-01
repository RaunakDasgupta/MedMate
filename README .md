# MedMate- Urine Strip Analyzer

A web application that analyzes an image of a urine strip and returns the RGB values (ordered from top to bottom) for:

Urobilinogen

Bilirubin

Ketone

Blood

Protein

Nitrite

Leukocytes

Glucose

Specicifc Gravity

pH


Tech Stack and Methodology
----------

### Frontend

The Frontend is built with HTML and CSS.

### Backend

The Backend is built using Django.


#### Methodology



The main methodology that has been used can be divided into 2 parts :-

1. **Resizing** - to get the relevant portion of the image.
2. **Segmentation** - to break down into small segments of each test case and find the needed values.

## Installation

1. Clone this repository using

   ```
   git clone https://github.com/RaunakDasgupta/MedMate
   ```

2. Navigate to the backend folder,install the required dependencies and start the webserver on port 8000

   ```
   cd backend
   pip install -r requirements.txt
   ```

3. Start the server
    
   ```
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
   ```

4. Once you have started the server, navigate to the **home**   route. Click on **Upload Your Test** to be redirected to the upload screen. For testing the home screen, nagivate to:

   ```
   http://localhost:8000/home/
   ```
5. Once you are at the **upload** route, select the image of your urine test in the box provided on the screen, aand it return the list of RGB values. For testing the results on uploading an image, navigate to:
   ```
   http://localhost:8000/upload/
   ```


## Authors

- [@RaunakDasgupta](https://www.github.com/RaunakDasgupta)
