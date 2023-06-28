# Neofis Python Developer Task

This project includes the implementation of five API endpoints as part of the Neofis Python Developer task. The APIs serve various functionalities and are described below.

## API Endpoints

1. **Register API**

   Endpoint: http://127.0.0.1:8000/api/register/
   
   This API allows users to register and create an account. Upon successful registration, users will be provided with an authentication token.

   ![Register API](https://drive.google.com/file/d/1aQO65F4076n0JP66EpsBg8kQ0XKfO6GP/view?usp=sharing)

2. **Login API**

   Endpoint: http://127.0.0.1:8000/api/login/
   
   Description: Returns the success message and token , if the login credentials are valid else throws respective error

   ![Endpoint 2 API](https://drive.google.com/file/d/1Uj0VGihp2H-jEfXGqvyLVMlunuHNuuDi/view?usp=sharing)

3. **Online Users API**

   Endpoint: http://127.0.0.1:8000/api/online-users
   
   Description: Provides a list of online users in the website.

   ![Endpoint 3 API](https://drive.google.com/file/d/1w0aDFMxB0zONn22FxCChS5ieJHp5kmBu/view?usp=sharing)

4. **Initiate chat API**

   Endpoint: http://127.0.0.1:8000/api/chat/start/<int id of user you want to connect>/
   
   Description: if you add the id (Primary Key/Int) of user you want to connect , it will check if the use if online and available and return a success message

   ![Endpoint 4 API](https://drive.google.com/file/d/1q6XTkRKOADwtGMauMo9uJGL8QBSA3K5S/view?usp=sharing)

5. **Suggest Friends API**

   Endpoint: http://127.0.0.1:8000/api/suggested-friends/<int id of user from 1 to 1000>
   
   Description: Suggest friends to the user from the list of 1000 user provided in teh assignment and give them a reccomandtaion of top 5 friends.

   ![Endpoint 5 API](https://drive.google.com/your-image-link)

## Setting up Google Drive for Image Storage

To access the images associated with the API endpoints, the images are stored in Google Drive. Follow the steps below to set up Google Drive for image storage:

1. Sign in to your Google account or create a new one if you don't have an account already.
2. Go to [Google Drive](https://drive.google.com) and create a new folder for storing the images.
3. Upload the images to the created folder.
4. Get the image link by right-clicking on the image file and selecting "Get link" or "Share."
5. Replace the respective image links in the API descriptions above with the actual image links from your Google Drive.

By following these steps, you will be able to access and display the associated images for each API endpoint.

Feel free to explore the code and modify it as needed. If you have any questions or need further assistance, please reach out to the Neofis development team.
