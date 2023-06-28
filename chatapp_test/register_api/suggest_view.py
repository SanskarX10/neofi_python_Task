import json
from operator import itemgetter
from django.http import JsonResponse
from django.views import View


with open(r'C:\projects\new_trail\chatapp_test\register_api\user_data\users.json', 'r', encoding='utf=8') as file:
    json_data = json.load(file)


class SuggestedFriendsAPI(View):

    def get(self, request, user_id):

        for user in json_data['users']:
            if user['id'] == user_id:
                user_data = user
                break
            else:
                user_data = None

        if user_data is None:
            return JsonResponse({'detail': 'User not found.'}, status=404)
        
        similarity_scores = [(user, calculate_similarity(user['interests'], user_data['interests'])) for user in json_data['users']]
        similarity_scores.sort(key=itemgetter(1), reverse=True)

        recommended_friends = similarity_scores[1:6]

        response_data = {
            'users': [
                {
                    'id': friend[0]['id'],
                    'name': friend[0]['name'],
                    'age': friend[0]['age'],
                    'interests': friend[0]['interests']
                } for friend in recommended_friends
            ]
        }

        return JsonResponse(response_data, status=200)


def calculate_similarity(interests1, interests2):
    common_interests = set(interests1.keys()).intersection(set(interests2.keys()))
    similarity_score = sum(min(interests1[interest], interests2[interest]) for interest in common_interests)

    return similarity_score
