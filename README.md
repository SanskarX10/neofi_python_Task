# Neofis Python Developer Task

This project includes the implementation of five API endpoints as part of the Neofis Python Developer task. The APIs serve various functionalities and are described below.

## API Endpoints

1. **Register API**

   Endpoint: http://127.0.0.1:8000/api/register/
   
   This API allows users to register and create an account. Upon successful registration, users will be provided with an authentication token.

   ![Register API](https://drive.google.com/uc?export=view&id=1aQO65F4076n0JP66EpsBg8kQ0XKfO6GP)

2. **Login API**

   Endpoint: http://127.0.0.1:8000/api/login/
   
   Description: Returns the success message and token , if the login credentials are valid else throws respective error

   ![Endpoint 2 API](https://drive.google.com/uc?export=view&id=1Uj0VGihp2H-jEfXGqvyLVMlunuHNuuDi)

3. **Online Users API**

   Endpoint: http://127.0.0.1:8000/api/online-users
   
   Description: Provides a list of online users in the website.

   ![Endpoint 3 API](https://drive.google.com/uc?export=view&id=1w0aDFMxB0zONn22FxCChS5ieJHp5kmBu)

4. **Initiate chat API**

   Endpoint: http://127.0.0.1:8000/api/chat/start/<int id of user you want to connect>/
   
   Description: if you add the id (Primary Key/Int) of user you want to connect , it will check if the use if online and available and return a success message

   ![Endpoint 4 API](https://drive.google.com/uc?export=view&id=1q6XTkRKOADwtGMauMo9uJGL8QBSA3K5S)

5. **Suggest Friends API**

   Endpoint: http://127.0.0.1:8000/api/suggested-friends/<int id of user from 1 to 1000>
   
   Description: Suggest friends to the user from the list of 1000 user provided in teh assignment and reccomands them five friends suggested by algorithm based on their interests
   #### Reccomendation algo:
      ### User Data
      The algorithm reads user data from a JSON file containing user information and their interests.
      
      ### Similarity Calculation
      The algorithm calculates the similarity score between the interests of the specified user and all other users. It finds common interests between two users and computes the similarity score as the sum of the minimum value between their interests for each common interest.
      
      ### Recommendation Generation
      The similarity scores are sorted in descending order to determine the most similar users. The top 5 recommended friends (excluding the user themselves) are selected from the sorted list.
      
      ### Response Format
      The API returns a JSON response containing the details (id, name, age, and interests) of the recommended friends. If the user with the specified `user_id` is not found, a JSON response with a "User not found" error message is returned with a status code of 404.

   ![Endpoint 5 API](https://drive.google.com/uc?export=view&id=16xnit6w0CT-EyNpnQ4SmjTidaWsyTpYo)
g
